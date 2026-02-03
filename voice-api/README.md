# Voice Authenticity Detection Service

## Overview
This service provides an API endpoint to analyze audio samples and determine whether they are AI-generated or naturally spoken by humans.

## Author
Sanjay Kumaar - GUVI x HCL Hackathon 2026

## Technology Stack
- **Framework**: FastAPI (Python)
- **Deployment**: Render
- **Authentication**: API Key-based

## API Endpoint

### POST /predict
Analyzes audio samples for voice authenticity

**Headers:**
```
x-api-key: guvi123
Content-Type: application/json
```

**Request Body:**
```json
{
  "language": "en",
  "audioFormat": "mp3",
  "audioBase64": "<base64-encoded-audio-data>"
}
```

**Response:**
```json
{
  "prediction": "AI" or "Human",
  "confidence": 0.85,
  "language": "en",
  "audio_format": "mp3",
  "status": "success"
}
```

## Supported Audio Formats
- MP3
- WAV
- OGG
- FLAC
- M4A

## Local Development

### Installation
```bash
cd voice-api
pip install -r requirements.txt
```

### Run Server
```bash
uvicorn app:service --host 0.0.0.0 --port 8000
```

## Deployment on Render

1. Create new Web Service
2. Connect to GitHub repository
3. Configure:
   - **Root Directory**: `voice-api`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:service --host 0.0.0.0 --port $PORT`

## Live API
🔗 https://guvi-qigw.onrender.com/predict

## Testing
```bash
curl -X POST https://guvi-qigw.onrender.com/predict \
  -H "x-api-key: guvi123" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "en",
    "audioFormat": "mp3",
    "audioBase64": "..."
  }'
```
