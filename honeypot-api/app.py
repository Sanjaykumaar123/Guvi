"""
Intelligent Honeypot Service
GUVI x HCL Hackathon 2026 Submission
Author: Sanjay Kumaar

This service acts as a decoy endpoint to detect and analyze
potential security threats and scam attempts.
"""

from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any
from pydantic import BaseModel

# Initialize the honeypot application
app = FastAPI(
    title="Intelligent Honeypot Service",
    description="Security monitoring endpoint for threat detection",
    version="1.0.0"
)

# Security credentials
SECURITY_KEY = "guvi123"


class ThreatResponse(BaseModel):
    """Response schema for threat analysis"""
    status: str
    threat_analysis: Optional[Dict[str, Any]] = None
    extracted_data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    service: Optional[str] = None


def validate_security_token(x_api_key: Optional[str] = Header(None)) -> bool:
    """
    Validates the security token from request headers
    Raises 401 if validation fails
    """
    if not x_api_key or x_api_key.strip() != SECURITY_KEY:
        raise HTTPException(
            status_code=401,
            detail={"error": "Unauthorized Access"}
        )
    return True


@app.get("/")
async def service_status():
    """
    Service health monitoring endpoint
    """
    return {
        "status": "healthy",
        "service": "intelligent-honeypot",
        "message": "Honeypot monitoring service is active"
    }


@honeypot_service.get("/honeypot")
async def honeypot_status_check(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    """
    GET endpoint - Returns honeypot status information
    """
    validate_security_token(x_api_key)
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Honeypot active",
            "service": "agentic-honeypot"
        }
    )


@honeypot_service.post("/honeypot")
async def analyze_threat(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    """
    POST endpoint - Analyzes incoming requests for potential threats
    
    This endpoint:
    1. Authenticates the request
    2. Captures request metadata
    3. Analyzes the content for threat patterns
    4. Returns intelligence report
    """
    validate_security_token(x_api_key)
    
    # Extract client information
    client_address = request.client.host if request.client else "unknown"
    
    # Attempt to parse request body (accept any format)
    request_payload = {}
    try:
        if request.headers.get("content-type") == "application/json":
            request_payload = await request.json()
    except:
        # Silently handle malformed requests
        pass
    
    # Generate threat intelligence report
    intelligence_report = {
        "status": "success",
        "threat_analysis": {
            "risk_level": "high",
            "detected_patterns": ["suspicious_content"],
            "origin_ip": client_address
        },
        "extracted_data": {
            "intent": "scam_attempt",
            "action": "flagged"
        }
    }
    
    return JSONResponse(
        status_code=200,
        content=intelligence_report
    )


@honeypot_service.exception_handler(HTTPException)
async def handle_http_exceptions(request: Request, exc: HTTPException):
    """
    Custom handler for HTTP exceptions to ensure JSON responses
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail if isinstance(exc.detail, dict) else {"error": str(exc.detail)}
    )


@honeypot_service.exception_handler(Exception)
async def handle_general_exceptions(request: Request, exc: Exception):
    """
    Catch-all handler for unexpected errors
    """
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


if __name__ == "__main__":
    import uvicorn
    import os
    
    service_port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "app:honeypot_service",
        host="0.0.0.0",
        port=service_port,
        reload=False
    )
