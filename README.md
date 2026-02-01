# AI Voice Detection API - Deployment Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

---

## 📡 API Documentation

### Endpoint: POST /predict

**Headers:**
- `x-api-key: guvi123` (Required)

**Request Body (JSON):**
```json
{
  "language": "en",
  "audio_format": "mp3",
  "audio_base64": "<base64-encoded-audio-string>"
}
```

**Success Response (200):**
```json
{
  "prediction": "AI",
  "confidence": 0.87,
  "language": "en",
  "audio_format": "mp3",
  "status": "success"
}
```

**Error Response - Unauthorized (401):**
```json
{
  "error": "Unauthorized"
}
```

**Error Response - Invalid Data (400):**
```json
{
  "error": "Invalid base64 audio data: <error details>"
}
```

---

## 🧪 Testing the API

### Using cURL

**1. First, encode an audio file to base64:**

On Linux/Mac:
```bash
base64 -i sample.mp3 -o audio_base64.txt
```

On Windows (PowerShell):
```powershell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("sample.mp3")) | Out-File audio_base64.txt
```

**2. Test the API:**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA..."
  }'
```

**3. Test without API key (should fail):**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA..."
  }'
```

Expected response:
```json
{
  "error": "Unauthorized"
}
```

### Using Python Requests

```python
import requests
import base64

# Read and encode audio file
with open("sample.mp3", "rb") as audio_file:
    audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')

# Make API request
url = "http://localhost:8000/predict"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "guvi123"
}
data = {
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": audio_base64
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

### Using Postman

1. Create a new POST request to `http://localhost:8000/predict`
2. Add header: `x-api-key: guvi123`
3. Select Body → raw → JSON
4. Paste the request JSON with your base64 audio
5. Click Send

---

## ☁️ Deployment Instructions

### Deploy to Render

1. **Create a new Web Service on Render**
   - Connect your GitHub repository
   - Or upload your code directly

2. **Configure the service:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Environment Variables:**
   - None required (API key is hardcoded as per requirements)

4. **Deploy!**
   - Render will automatically deploy your API
   - You'll get a URL like: `https://your-app.onrender.com`

### Deploy to Railway

1. **Create a new project on Railway**
   - Connect your GitHub repository

2. **Railway will auto-detect FastAPI**
   - No configuration needed!
   - It will automatically use the correct start command

3. **Get your deployment URL**
   - Railway provides a public URL automatically

### Deploy to HuggingFace Spaces

1. **Create a new Space**
   - Select "Docker" as the SDK

2. **Create a Dockerfile:**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 7860

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

3. **Push your code to the Space**
   - Upload `main.py`, `requirements.txt`, and `Dockerfile`

4. **Access your API**
   - HuggingFace will provide a public URL

### Deploy to Vercel (Serverless)

1. **Create `vercel.json`:**

```json
{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

2. **Install Vercel CLI:**
```bash
npm i -g vercel
```

3. **Deploy:**
```bash
vercel
```

---

## 🔧 Environment Configuration

### For Production Deployment

**Modify `main.py` line 177:**

Change:
```python
reload=True  # Auto-reload on code changes (disable in production)
```

To:
```python
reload=False  # Disabled for production
```

### Using Environment Variables (Optional Enhancement)

If you want to make the API key configurable:

```python
import os

VALID_API_KEY = os.getenv("API_KEY", "guvi123")
```

Then set environment variable in your deployment platform:
```
API_KEY=guvi123
```

---

## 📊 API Health Check

Visit the root endpoint to check if the API is running:

```bash
curl http://localhost:8000/
```

Response:
```json
{
  "message": "AI Voice Detection API is running",
  "version": "1.0.0",
  "endpoints": {
    "predict": "/predict (POST)"
  },
  "status": "healthy"
}
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (Windows)
taskkill /PID <process_id> /F

# Or use a different port
uvicorn main:app --host 0.0.0.0 --port 8080
```

### Module Not Found Error
```bash
# Ensure you're in the correct directory
cd c:/Users/Sanjay Kumaar/guvi

# Reinstall dependencies
pip install -r requirements.txt
```

### Base64 Encoding Issues
- Ensure no newlines in base64 string
- Use `base64.b64encode().decode('utf-8')` in Python
- Remove any whitespace or line breaks

---

## 📝 Notes for GUVI Endpoint Tester

✅ **API Key:** `guvi123` (hardcoded as required)  
✅ **Endpoint:** `POST /predict`  
✅ **Response Format:** JSON only (no HTML)  
✅ **Error Handling:** All errors return JSON  
✅ **Required Fields:** language, audio_format, audio_base64  
✅ **Prediction Values:** "AI" or "Human"  
✅ **Deployment Ready:** Works on Render, Railway, HuggingFace  

---

## 🚀 Next Steps for Production

To integrate a real ML model:

1. Train your model (CNN/RNN/Transformer)
2. Save the model file (e.g., `model.pth`, `model.h5`)
3. Uncomment ML imports in `requirements.txt`
4. Replace the `predict_audio()` function with actual inference
5. Add feature extraction (MFCC, spectrograms, etc.)

Example model integration:
```python
import torch
import torchaudio

def predict_audio(audio_path, language, audio_format):
    # Load model
    model = torch.load('voice_detection_model.pth')
    model.eval()
    
    # Load and preprocess audio
    waveform, sample_rate = torchaudio.load(audio_path)
    
    # Extract features (MFCC, etc.)
    features = extract_features(waveform, sample_rate)
    
    # Run inference
    with torch.no_grad():
        output = model(features)
        prediction = "AI" if output > 0.5 else "Human"
        confidence = float(output)
    
    return {
        "prediction": prediction,
        "confidence": confidence,
        "language": language,
        "audio_format": audio_format,
        "status": "success"
    }
```

---

**Good luck with your GUVI x HCL Hackathon! 🎉**
