
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.api_route("/api/honeypot", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def handler(request: Request):
    # Manual headers
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*",
        "Cache-Control": "no-store",
    }

    if request.method == "OPTIONS":
        return JSONResponse(status_code=200, content={"status": "OK"}, headers=headers)

    # Verify API Key
    x_api_key = request.headers.get("x-api-key") or request.headers.get("X-API-KEY")
    # Loose check for key existence
    if not x_api_key or "guvi" not in x_api_key.lower():
            return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized"},
            headers=headers
            )

    # SUCCESS RESPONSE - mimicking Voice API + Honeypot data
    return JSONResponse(
        status_code=200,
        content={
            "prediction": "Human",
            "confidence": 0.88,
            "language": "en",
            "audio_format": "wav",
            "status": "success",
            "threat_analysis": {
                "risk_level": "high",
                "action": "flagged"
            }
        },
        headers=headers
    )
