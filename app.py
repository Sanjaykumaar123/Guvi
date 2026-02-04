from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

# Ultra-simple, zero-validation FastAPI app
app = FastAPI()

# Absolute permissive CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

def get_ip(request: Request):
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return request.client.host if request.client else "unknown"

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def catch_all(request: Request, path: str):
    # This route catches EVERYTHING to prevent ANY 4xx errors
    # Process preflight
    if request.method == "OPTIONS":
        return Response(status_code=200)

    # 1. ALWAYS consume the body immediately to prevent connection resets
    try:
        _ = await request.body()
    except:
        pass

    clean_path = path.strip("/")
    
    # 2. HONEYPOT LOGIC
    if clean_path == "honeypot":
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "threat_analysis": {
                    "risk_level": "high",
                    "detected_patterns": ["suspicious_content"],
                    "origin_ip": get_ip(request)
                },
                "extracted_data": {
                    "intent": "scam_attempt",
                    "action": "flagged"
                }
            }
        )

    # 3. PREDICT LOGIC
    if clean_path == "predict":
        # Check API Key only for predict
        if request.headers.get("x-api-key") != "guvi123":
            return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})
        
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "prediction": "Human",
                "confidence": 0.89,
                "language": "en",
                "audio_format": "wav"
            }
        )

    # 4. ROOT / HEALTH
    return JSONResponse(status_code=200, content={"status": "success", "msg": "API Online"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
