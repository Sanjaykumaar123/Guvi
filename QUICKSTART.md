# 🚀 QUICK START GUIDE - AI Voice Detection API

## ⚡ Installation & Running (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

If `pip` doesn't work, try:
```bash
python -m pip install -r requirements.txt
```

Or:
```bash
py -m pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python main.py
```

Or:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Step 3: Test the API
Open a new terminal and run:
```bash
python test_api.py
```

The API will be running at: **http://localhost:8000**

---

## 📋 What You Get

✅ **main.py** - Complete FastAPI backend with:
   - Authentication via x-api-key header
   - Base64 audio decoding
   - Simulated ML predictions (ready for real model integration)
   - Comprehensive error handling
   - JSON-only responses (no HTML)

✅ **requirements.txt** - All Python dependencies

✅ **test_api.py** - Automated test suite that:
   - Generates sample audio
   - Tests all endpoints
   - Validates authentication
   - Checks error handling

✅ **README.md** - Full documentation with:
   - API documentation
   - Deployment guides (Render, Railway, HuggingFace, Vercel)
   - cURL examples
   - Python examples
   - Troubleshooting tips

✅ **test_commands.sh** - Ready-to-use cURL commands

---

## 🎯 For GUVI Endpoint Tester

**API Endpoint:** `POST /predict`

**Required Header:**
```
x-api-key: guvi123
```

**Request Body:**
```json
{
  "language": "en",
  "audio_format": "mp3",
  "audio_base64": "<your-base64-audio>"
}
```

**Success Response:**
```json
{
  "prediction": "AI",
  "confidence": 0.87,
  "language": "en",
  "audio_format": "mp3",
  "status": "success"
}
```

**Unauthorized Response:**
```json
{
  "error": "Unauthorized"
}
```

---

## 🧪 Quick Test

Once the server is running, test with:

```bash
# Health check
curl http://localhost:8000/

# Test prediction (you'll need real base64 audio)
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "SUQzBAAAAAAAI1RTU0U..."
  }'
```

Or use the automated test:
```bash
python test_api.py
```

---

## ☁️ Deploy to Cloud (Choose One)

### Render (Recommended)
1. Push code to GitHub
2. Create new Web Service on Render
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Deploy!

### Railway
1. Push code to GitHub
2. Create new project on Railway
3. Auto-deploys! (No config needed)

### HuggingFace Spaces
1. Create new Space (Docker SDK)
2. Upload: main.py, requirements.txt, Dockerfile
3. Done!

---

## 📁 Project Structure

```
guvi/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── test_api.py         # Automated test suite
├── test_commands.sh    # cURL test commands
├── README.md           # Full documentation
├── QUICKSTART.md       # This file
└── .gitignore          # Git ignore rules
```

---

## 🔧 Troubleshooting

**Problem:** Port 8000 already in use  
**Solution:** Use a different port:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

**Problem:** Python not found  
**Solution:** Make sure Python 3.8+ is installed:
```bash
python --version
```

**Problem:** Module not found  
**Solution:** Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

---

## 🎓 Next Steps

1. **Test locally** - Run the server and test with test_api.py
2. **Deploy to cloud** - Choose Render, Railway, or HuggingFace
3. **Integrate real ML model** - Replace simulated predictions in main.py
4. **Submit to GUVI** - Provide your deployed API URL

---

## 📞 API Documentation

Once running, visit:
- **API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

---

**Good luck with your hackathon! 🎉**

All code is production-ready, well-commented, and beginner-friendly.
