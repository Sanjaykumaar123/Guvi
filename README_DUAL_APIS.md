# GUVI x HCL Hackathon - Dual API Submission

This repository contains **two separate APIs** for the GUVI x HCL Hackathon:

## 📁 Project Structure

```
guvi/
├── voice-api/          # AI Voice Detection API
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
└── honeypot-api/       # Agentic Honeypot API
    ├── app.py
    ├── requirements.txt
    └── README.md
```

## 🚀 Deployment Instructions

### Voice Detection API

**Render Settings:**
- Root Directory: `voice-api`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

**Endpoint:** `POST /predict`
**API Key:** `guvi123`

### Honeypot API

**Render Settings:**
- Root Directory: `honeypot-api`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

**Endpoint:** `POST /honeypot`
**API Key:** `guvi123`

## 🧪 Testing

Each API folder contains its own README with specific testing instructions.

## 📝 Notes

- Both APIs use the same API key: `guvi123`
- Both APIs are production-ready and follow best practices
- Deploy each API as a separate Render service
