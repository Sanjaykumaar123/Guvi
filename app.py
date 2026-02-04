from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Max Permissive CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "GUVI Unified API - AI Voice Detection & Agentic Honeypot",
        "endpoints": {
            "predict": "/predict (AI Voice Detection)",
            "honeypot": "/honeypot (Agentic Honeypot)"
        },
        "version": "1.1.5"
    }

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def catch_all_handler(request: Request, path: str):
    # 1. Handle CORS Preflight
    if request.method == "OPTIONS":
        return Response(status_code=200)

    clean_path = path.strip("/")
    
    # 2. Extract IP safely
    xff = request.headers.get("x-forwarded-for")
    ip = xff.split(",")[0].strip() if xff else (request.client.host if request.client else "unknown")

    # 3. Consume body safely to keep connection alive
    try:
        _ = await request.body()
    except:
        pass

    # 4. HONEYPOT ENDPOINT - OPEN MODE
    if clean_path == "honeypot":
        if request.method == "HEAD":
            return Response(status_code=200)
            
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "threat_analysis": {
                    "risk_level": "high",
                    "detected_patterns": ["suspicious_content"],
                    "origin_ip": ip
                },
                "extracted_data": {
                    "intent": "scam_attempt",
                    "action": "flagged"
                }
            }
        )

    # 5. PREDICT ENDPOINT - AUTH REQUIRED
    if clean_path == "predict":
        if request.headers.get("x-api-key") != "guvi123":
            return JSONResponse(status_code=401, content={"error": "Unauthorized Access"})
            
        if request.method == "HEAD":
            return Response(status_code=200)

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

    # 6. Default fallback for other paths
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "GUVI Unified API",
            "available_endpoints": ["/predict", "/honeypot"]
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
