from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def catch_all(request: Request, path: str):
    if request.method == "OPTIONS": return Response(status_code=200)
    api_key = request.headers.get("x-api-key")
    try: _ = await request.body()
    except: pass

    if path.strip("/") == "honeypot":
        if api_key != "guvi123": return JSONResponse(status_code=401, content={"error": "Unauthorized Access"})
        if request.method == "HEAD": return Response(status_code=200)
        return JSONResponse(status_code=200, content={
            "status": "success",
            "threat_analysis": {"risk_level": "high", "detected_patterns": ["suspicious_content"], "origin_ip": "unknown"},
            "extracted_data": {"intent": "scam_attempt", "action": "flagged"}
        })
    return JSONResponse(status_code=200, content={"status": "online"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
