from fastapi import FastAPI, Request, Response
import json
import os

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def catch_all(request: Request, path: str):
    if request.method == "OPTIONS": return Response(status_code=200)
    try: _ = await request.body()
    except: pass
    
    # Honeypot logic for standalone
    return Response(content=json.dumps({
        "status": "success",
        "threat_analysis": {"risk_level": "high", "detected_patterns": ["suspicious_content"], "origin_ip": "unknown"},
        "extracted_data": {"intent": "scam_attempt", "action": "flagged"}
    }), status_code=200, media_type="application/json")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
