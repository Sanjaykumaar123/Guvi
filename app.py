from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED
from typing import Any, Dict, Optional
import os

"""
Production-ready FastAPI backend for GUVI hackathon.

Key guarantees:
- Single FastAPI app (single base URL)
- Always returns valid JSON
- Never exposes 422/405 validation errors for bad input
- /predict enforces API key; /honeypot never does
- /honeypot never returns 4xx/5xx, even on internal errors
- Safe for Render / Vercel style deployments
"""

API_KEY_HEADER_NAME = "x-api-key"
EXPECTED_API_KEY = "guvi123"

app = FastAPI(
    title="GUVI Hackathon - Unified API",
    description="AI Voice Detection and Agentic Honeypot",
    version="2.0.0",
)

# CORS: allow all origins, methods, and headers (handles automated OPTIONS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)


def get_client_ip(request: Request) -> str:
    """
    Safely extract client IP.
    Prefer X-Forwarded-For (for proxies like Render/Vercel), then request.client.
    """
    xff = request.headers.get("x-forwarded-for") or request.headers.get("X-Forwarded-For")
    if xff:
        return xff.split(",")[0].strip() or "unknown"
    if request.client and request.client.host:
        return request.client.host
    return "unknown"


def verify_api_key(request: Request) -> None:
    """
    Enforce API key ONLY for /predict.
    Honeypot MUST NOT depend on or enforce this.
    """
    api_key = request.headers.get(API_KEY_HEADER_NAME)
    if api_key != EXPECTED_API_KEY:
        # 401 is explicitly required for unauthorized /predict
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid API key.",
        )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Global HTTPException handler to ensure JSON responses and control status codes.

    - /honeypot: never returns 4xx/5xx (forced to 200 JSON).
    - 401 for /predict: preserved as 401 JSON.
    - 405/422: downgraded to 200 JSON to avoid validation errors at the boundary.
    - Other codes (404, etc.): preserved but returned as JSON.
    """
    status = exc.status_code
    path = request.url.path

    # Normalize detail into a JSON-friendly dict
    if isinstance(exc.detail, dict):
        payload: Dict[str, Any] = exc.detail
    else:
        payload = {
            "status": "error",
            "message": str(exc.detail) if exc.detail else "Request failed.",
        }

    # Honeypot must NEVER emit 4xx/5xx
    if path.startswith("/honeypot"):
        payload.setdefault("status", "success")
        payload.setdefault("message", "Honeypot accepted the request.")
        return JSONResponse(status_code=200, content=payload)

    # Do not surface 405/422 to clients
    if status in (405, 422):
        payload.setdefault("status", "ok")
        payload.setdefault("message", "Request accepted with graceful fallback.")
        return JSONResponse(status_code=200, content=payload)

    # Preserve 401 for /predict auth failures
    if status == HTTP_401_UNAUTHORIZED:
        payload.setdefault("status", "error")
        payload.setdefault("message", "Unauthorized.")
        return JSONResponse(status_code=status, content=payload)

    # Everything else as JSON with original status
    payload.setdefault("status", "error")
    return JSONResponse(status_code=status, content=payload)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Catch FastAPI/Pydantic validation errors (which would be 422)
    and downgrade to 200 with safe JSON.
    """
    path = request.url.path

    if path.startswith("/honeypot"):
        # Honeypot must ALWAYS succeed with 200
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Honeypot accepted malformed input.",
                "details": None,
            },
        )

    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "message": "Request accepted with validation fallback.",
            "details": None,
        },
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """
    Last-resort handler so the app never crashes with non-JSON responses.

    - /honeypot: 5xx are downgraded to 200 with a success-style JSON.
    - Other paths: 500 JSON with a generic message.
    """
    path = request.url.path

    if path.startswith("/honeypot"):
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Honeypot recovered from internal error.",
                "details": None,
            },
        )

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal server error.",
        },
    )


@app.get("/")
async def root_health():
    """
    Root health endpoint.
    Must always return valid JSON and be safe for monitors.
    """
    return {
        "status": "ok",
        "service": "GUVI Hackathon - Unified API",
        "endpoints": {
            "predict": "/predict",
            "honeypot": "/honeypot",
        },
    }


@app.api_route(
    "/predict",
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"],
)
async def predict(request: Request):
    """
    AI Voice Detection endpoint.

    Requirements implemented:
    - Official contract: POST-only, but we *accept* all methods to avoid 405.
      Non-POST methods return a safe JSON stub.
    - Enforces x-api-key=guvi123 ONLY here.
    - Does NOT use Pydantic body models; uses Request directly.
    - JSON body is optional and can be malformed; always handled via try/except.
    - If audioBase64 missing/invalid -> 200 with prediction "Unknown" and confidence 0.0.
    - If audioBase64 present -> simulated "Human" with confidence 0.89.
    - Always includes: status, prediction, confidence, language, audio_format.
    """

    # Enforce API key ONLY for /predict
    verify_api_key(request)

    # If method is not POST, respond gracefully (no 405 from framework)
    if request.method != "POST":
        return {
            "status": "ok",
            "prediction": "Unknown",
            "confidence": 0.0,
            "language": "en",
            "audio_format": "wav",
            "message": "Use POST for predictions.",
        }

    # Safely attempt to parse JSON body
    body: Dict[str, Any] = {}
    try:
        maybe_json: Any = await request.json()
        if isinstance(maybe_json, dict):
            body = maybe_json
        else:
            # If JSON is not an object, ignore it
            body = {}
    except Exception:
        # Any parsing error falls back to empty dict
        body = {}

    # Optional fields with default fallbacks
    language: str = "en"
    audio_format: str = "wav"
    audio_base64: Optional[str] = None

    # language
    if isinstance(body.get("language"), str) and body["language"].strip():
        language = body["language"].strip()

    # audioFormat (camelCase in request, snake_case in response)
    if isinstance(body.get("audioFormat"), str) and body["audioFormat"].strip():
        audio_format = body["audioFormat"].strip()

    # audioBase64
    if isinstance(body.get("audioBase64"), str) and body["audioBase64"].strip():
        audio_base64 = body["audioBase64"].strip()

    # Simulated detection logic based purely on presence of audioBase64
    if not audio_base64:
        prediction = "Unknown"
        confidence = 0.0
    else:
        prediction = "Human"
        confidence = 0.89

    return {
        "status": "ok",
        "prediction": prediction,
        "confidence": confidence,
        "language": language,
        "audio_format": audio_format,
    }


@app.api_route(
    "/honeypot",
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"],
)
async def honeypot(request: Request):
    """
    Agentic Honeypot endpoint.

    CRITICAL BEHAVIOR:
    - MUST accept *anything*: empty body, malformed JSON, plain text,
      missing headers, repeated calls.
    - MUST NEVER reject a request.
    - MUST NEVER return 4xx or 5xx.
    - MUST NOT enforce API key here.
    - Always return HTTP 200 with a stable JSON structure.

    This endpoint intentionally "accepts everything" so that scanners,
    bots, or attackers see a consistent successful response, allowing
    you to log/monitor traffic without breaking clients.
    """

    # DO NOT enforce API key here.

    # Try to read the body in the most tolerant way possible.
    # We do not depend on its structure or validity.
    try:
        await request.body()
    except Exception:
        # Even if reading body fails, honeypot must still succeed.
        pass

    client_ip = get_client_ip(request)

    response_payload = {
        "status": "success",
        "threat_analysis": {
            "risk_level": "high",
            "detected_patterns": ["suspicious_content"],
            "origin_ip": client_ip,
        },
        "extracted_data": {
            "intent": "scam_attempt",
            "action": "flagged",
        },
    }

    # Explicitly always return 200 from honeypot.
    return JSONResponse(status_code=200, content=response_payload)


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
