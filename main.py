from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.api_route("/honeypot", methods=["GET", "POST"])
async def honeypot(request: Request):
    api_key = request.headers.get("x-api-key")

    if api_key != "guvi123":
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized"}
        )

    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "service": "agentic-honeypot",
            "message": "Honeypot endpoint active",
            "threat_detected": False
        }
    )
