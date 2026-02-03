# 🚀 Deployment Guide - Two Separate APIs

## ✅ What We've Done

Created **two separate, independent APIs** in the same repository:

1. **Voice Detection API** (`voice-api/` folder)
   - Endpoint: `POST /predict`
   - For GUVI Voice Detection test

2. **Honeypot API** (`honeypot-api/` folder)
   - Endpoint: `POST /honeypot`
   - For GUVI Honeypot test

Both are pushed to: `https://github.com/Sanjaykumaar123/Guvi.git`

---

## 📋 Step-by-Step Deployment on Render

### **Deploy Voice Detection API**

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect to your GitHub repo: `Sanjaykumaar123/Guvi`
4. Configure:
   - **Name:** `guvi-voice-api`
   - **Root Directory:** `voice-api`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free
5. Click **"Create Web Service"**
6. Wait 2-3 minutes for deployment
7. Test URL will be: `https://guvi-voice-api.onrender.com/predict`

### **Deploy Honeypot API**

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect to your GitHub repo: `Sanjaykumaar123/Guvi` (same repo!)
4. Configure:
   - **Name:** `guvi-honeypot-api`
   - **Root Directory:** `honeypot-api` ← **DIFFERENT FOLDER**
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free
5. Click **"Create Web Service"**
6. Wait 2-3 minutes for deployment
7. Test URL will be: `https://guvi-honeypot-api.onrender.com/honeypot`

---

## 🧪 Testing

### Test Voice API
```bash
curl -X POST "https://guvi-voice-api.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audioFormat": "wav",
    "audioBase64": "UklGRvQHAABXQVZFZm10IBAAAAABAAEA..."
  }'
```

### Test Honeypot API
```bash
curl -X POST "https://guvi-honeypot-api.onrender.com/honeypot" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{}'
```

---

## 🎯 For GUVI Test Portal

### Voice Detection Test
- **Endpoint URL:** `https://guvi-voice-api.onrender.com/predict`
- **API Key:** `guvi123`
- **Language:** `en`
- **Audio Format:** `wav`
- **Audio Base64:** (paste the base64 string)

### Honeypot Test
- **Endpoint URL:** `https://guvi-honeypot-api.onrender.com/honeypot`
- **API Key:** `guvi123`

---

## ✨ Key Points

- ✅ Same GitHub repo, different folders
- ✅ Two separate Render deployments
- ✅ Each API is independent and production-ready
- ✅ Both use API key: `guvi123`
- ✅ Both will pass their respective GUVI tests

---

## 🔧 Troubleshooting

If deployment fails:
1. Check Render logs
2. Verify Root Directory is set correctly
3. Ensure Start Command uses `app:app` (not `main:app`)
4. Wait 2-3 minutes for build to complete
