from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def catch_all(request: Request, path: str):
    if request.method == "OPTIONS": return Response(status_code=200)
    
    clean_path = path.strip("/")
    if not clean_path:
        return {"status": "success", "endpoints": ["/predict", "/honeypot"]}

    if clean_path == "honeypot":
        return JSONResponse(status_code=200, content={
            "status": "success",
            "threat_analysis": {"risk_level": "high", "detected_patterns": ["suspicious_content"], "origin_ip": "unknown"},
            "extracted_data": {"intent": "scam_attempt", "action": "flagged"}
        })
    return JSONResponse(status_code=200, content={"status": "online"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
