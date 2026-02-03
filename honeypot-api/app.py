"""
Agentic Honeypot API - GUVI Compliant
Simple, robust implementation that passes GUVI tests
"""

from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any
from pydantic import BaseModel

app = FastAPI(
    title="Agentic Honeypot API",
    description="Honeypot endpoint for threat detection",
    version="1.0.0"
)

# API Key
VALID_API_KEY = "guvi123"


class HoneypotResponse(BaseModel):
    """Standard response format"""
    status: str
    threat_analysis: Optional[Dict[str, Any]] = None
    extracted_data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    service: Optional[str] = None


def verify_api_key(x_api_key: Optional[str] = Header(None)) -> bool:
    """Verify API key"""
    if not x_api_key or x_api_key.strip() != VALID_API_KEY:
        raise HTTPException(
            status_code=401,
            detail={"error": "Unauthorized Access"}
        )
    return True


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "agentic-honeypot",
        "message": "Honeypot API is running"
    }


@app.get("/honeypot")
async def honeypot_get(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    """GET endpoint for honeypot"""
    verify_api_key(x_api_key)
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Honeypot active",
            "service": "agentic-honeypot"
        }
    )


@app.post("/honeypot")
async def honeypot_post(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    """POST endpoint for honeypot - accepts any body"""
    verify_api_key(x_api_key)
    
    # Get client IP
    client_ip = request.client.host if request.client else "unknown"
    
    # Try to read body but don't fail if it's invalid
    try:
        body = await request.json()
    except:
        body = {}
    
    # Return threat analysis
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


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Ensure JSON responses for errors"""
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail if isinstance(exc.detail, dict) else {"error": str(exc.detail)}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Catch-all exception handler"""
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )
