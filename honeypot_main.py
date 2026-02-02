"""
GUVI x HCL Hackathon - Agentic Honey-Pot API
Minimal FastAPI backend for honeypot endpoint testing
"""

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
import os

# Initialize FastAPI app
app = FastAPI(title="Agentic Honeypot API")

# Valid API key
VALID_API_KEY = "guvi123"


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "healthy", "service": "agentic-honeypot"}


@app.get("/honeypot")
async def honeypot_endpoint(x_api_key: Optional[str] = Header(None)):
    """
    Honeypot endpoint for GUVI testing
    
    Headers:
        x-api-key: Authentication key (required)
    
    Returns:
        JSON response with honeypot status
    """
    
    # Verify API key
    if not x_api_key or x_api_key != VALID_API_KEY:
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized"}
        )
    
    # Return success response
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "service": "agentic-honeypot",
            "message": "Honeypot endpoint active",
            "threat_detected": False
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Catch all exceptions and return JSON"""
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("honeypot_main:app", host="0.0.0.0", port=port, reload=False)
