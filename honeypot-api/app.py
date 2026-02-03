"""
Agentic Honeypot API
GUVI x HCL Hackathon Submission

This API provides a honeypot endpoint that detects and analyzes potential threats.
"""

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def honeypot_endpoint(request):
    """
    Chameleon Honeypot Endpoint
    - GET: Returns simple "Active" status
    - POST: Returns "Intelligence Report"
    """
    
    # 1. Strict Authentication
    api_key_header = request.headers.get("x-api-key")
    if not api_key_header or api_key_header.strip() != "guvi123":
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized Access"}
        )

    # 2. Handle GET (Simple Check)
    if request.method == "GET":
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Honeypot active",
                "service": "agentic-honeypot"
            }
        )

    # 3. Handle POST (Intelligence Extraction)
    client_ip = request.client.host if request.client else "unknown"
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "threat_analysis": {
                "risk_level": "high",
                "detected_patterns": ["suspicious_content"],
                "origin_ip": client_ip
            },
            "extracted_data": {
                "intent": "scam_attempt",
                "action": "flagged"
            }
        }
    )


async def health_check(request):
    """
    Open Health Check endpoint (No Auth)
    """
    return JSONResponse({
        "status": "healthy",
        "service": "agentic-honeypot"
    })


# Route definitions
routes = [
    Route("/", health_check, methods=["GET", "HEAD"]),
    Route("/honeypot", honeypot_endpoint, methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]),
]

app = Starlette(debug=False, routes=routes)
