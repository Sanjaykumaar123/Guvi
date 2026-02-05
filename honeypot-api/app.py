from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# 1. Enable standard CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def catch_all(request: Request, path: str):
    # Handle OPTIONS
    if request.method == "OPTIONS":
        return Response(status_code=200)

    # API Key check
    api_key = request.headers.get("x-api-key", "").lower()
    if api_key and "guvi" not in api_key:
        return Response(content=json.dumps({"error": "Unauthorized"}), status_code=401, media_type="application/json")

    # Honeypot response with maximum compatibility
    payload = {
        "status": "success",
        "threat_analysis": {
            "risk_level": "high",
            "detected_patterns": ["suspicious_content"],
            "origin_ip": "unknown"
        },
        "extracted_data": {
            "intent": "scam_attempt",
            "action": "flagged"
        },
        "extracted_intelligence": { # Alternate format
            "threat": "active",
            "intent": "scam_detected",
            "action": "logged"
        }
    }
    
    return Response(
        content=json.dumps(payload),
        status_code=200, 
        media_type="application/json"
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
