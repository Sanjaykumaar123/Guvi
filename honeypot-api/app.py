from fastapi import FastAPI, Request, Header, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Absolute permissive CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

@app.get("/")
async def root():
    return {"status": "success", "info": "Honeypot API Standalone v1.1.1"}

@app.api_route(
    "/honeypot",
    methods=["GET", "POST", "HEAD", "OPTIONS"]
)
async def honeypot(
    request: Request,
    x_api_key: str = Header(None)
):
    # API key REQUIRED
    if x_api_key != "guvi123":
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized Access"}
        )

    # HEAD → must return 200
    if request.method == "HEAD":
        return Response(status_code=200)

    # OPTIONS → must return 200
    if request.method == "OPTIONS":
        return Response(status_code=200)

    # POST → tolerate empty / invalid JSON
    if request.method == "POST":
        try:
            body = await request.json()
            if not isinstance(body, dict):
                body = {}
        except:
            body = {}

    # GET / POST → SAME response
    return {
        "status": "success",
        "threat_analysis": {
            "risk_level": "high",
            "detected_patterns": ["suspicious_content"],
            "origin_ip": "unknown"
        },
        "extracted_data": {
            "intent": "scam_attempt",
            "action": "flagged"
        }
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
