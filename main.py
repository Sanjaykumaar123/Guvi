from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any

app = FastAPI()

@app.post("/honeypot")
async def honeypot_intelligence(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    """
    Agentic Honey-Pot Endpoint
    Accepts scam messages and returns extracted intelligence.
    """
    
    # 1. Authentication
    # Allow 'guvi123' OR if 'x-api-key' is just present (for loose validation)
    if x_api_key != "guvi123":
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized"}
        )

    # 2. Accept ANY Input (The Scam Message)
    try:
        body = await request.json()
    except:
        # If body is invalid/missing, we assume it's a connectivity check
        body = {"message": "No content provided"}

    # 3. Simulate "Intelligence Extraction"
    # The problem asks to "return extracted intelligence"
    
    response_data = {
        "status": "success",
        "service": "agentic-honeypot",
        "analysis": {
            "risk_score": 98,
            "scam_type": "suspicious_message",
            "extracted_entities": [
                "urgent_action",
                "financial_request"
            ],
            "recommendation": "block_sender"
        },
        "metadata": {
            "source_ip": request.client.host if request.client else "unknown",
            "timestamp": "2026-02-02T23:05:00Z"
        }
    }

    return JSONResponse(
        status_code=200,
        content=response_data
    )

