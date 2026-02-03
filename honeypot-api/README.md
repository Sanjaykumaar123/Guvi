# Intelligent Honeypot Service

## Overview
A security monitoring endpoint designed to detect, analyze, and log potential threats and scam attempts.

## Author
Sanjay Kumaar - GUVI x HCL Hackathon 2026

## Purpose
This honeypot service acts as a decoy endpoint that:
- Authenticates incoming requests
- Captures threat intelligence
- Analyzes suspicious patterns
- Returns controlled responses

## Technology Stack
- **Framework**: FastAPI (Python)
- **Deployment**: Render
- **Security**: Token-based authentication

## API Endpoints

### GET /honeypot
Returns honeypot status

**Headers:**
```
x-api-key: guvi123
```

**Response:**
```json
{
  "status": "success",
  "message": "Honeypot active",
  "service": "agentic-honeypot"
}
```

### POST /honeypot
Analyzes incoming requests for threats

**Headers:**
```
x-api-key: guvi123
Content-Type: application/json
```

**Response:**
```json
{
  "status": "success",
  "threat_analysis": {
    "risk_level": "high",
    "detected_patterns": ["suspicious_content"],
    "origin_ip": "xxx.xxx.xxx.xxx"
  },
  "extracted_data": {
    "intent": "scam_attempt",
    "action": "flagged"
  }
}
```

## Local Development

### Setup
```bash
cd honeypot-api
pip install -r requirements.txt
```

### Run
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Deployment on Render

1. Create Web Service
2. Link GitHub repository
3. Settings:
   - **Root Directory**: `honeypot-api`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:honeypot_service --host 0.0.0.0 --port $PORT`

## Live Service
🔗 https://guvi-honeypot-new.onrender.com/honeypot

## Testing
```bash
curl -X POST https://guvi-honeypot-new.onrender.com/honeypot \
  -H "x-api-key: guvi123" \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Security Features
- ✅ API key authentication
- ✅ Request validation
- ✅ Threat pattern detection
- ✅ IP tracking
- ✅ Controlled error responses
