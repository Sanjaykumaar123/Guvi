# Environment Variables Guide

## 📋 Overview

By default, the API uses **hardcoded values** as per GUVI requirements:
- **API Key:** `guvi123` (hardcoded in `main.py`)
- **Host:** `0.0.0.0`
- **Port:** `8000`

**No .env file is required** for the hackathon submission.

---

## 🔧 Optional: Using Environment Variables

If you want to make the API key and other settings configurable (for production use), follow these steps:

### 1. Create .env file

Copy the example file:
```bash
copy .env.example .env
```

Or on Linux/Mac:
```bash
cp .env.example .env
```

### 2. Update .env with your values

```env
API_KEY=your_secret_key_here
HOST=0.0.0.0
PORT=8000
ENVIRONMENT=production
LOG_LEVEL=INFO
```

### 3. Install python-dotenv

```bash
pip install python-dotenv
```

### 4. Update main.py to use environment variables

Add at the top of `main.py`:

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Use environment variable with fallback to hardcoded value
VALID_API_KEY = os.getenv("API_KEY", "guvi123")
```

---

## 🚀 Deployment Environment Variables

When deploying to cloud platforms, you can set environment variables directly:

### Render
1. Go to your service dashboard
2. Click **"Environment"** tab
3. Add variables:
   - `API_KEY` = `guvi123`
   - `PORT` = (auto-set by Render)

### Railway
1. Go to your project
2. Click **"Variables"** tab
3. Add: `API_KEY` = `guvi123`

### HuggingFace Spaces
1. Go to Settings → Repository secrets
2. Add: `API_KEY` = `guvi123`

### Vercel
```bash
vercel env add API_KEY
# Enter: guvi123
```

---

## ⚠️ Security Notes

1. **Never commit .env files** to Git (already in .gitignore)
2. **Use strong API keys** in production (not "guvi123")
3. **Rotate keys regularly** in production environments
4. **Use different keys** for development and production

---

## 📝 Current Setup (Hackathon)

For the GUVI hackathon submission:
- ✅ API key is hardcoded: `guvi123`
- ✅ No .env file needed
- ✅ Works out of the box
- ✅ Meets all requirements

**You don't need to change anything for the hackathon!**

---

## 🔄 Future Enhancements

If you continue developing this project after the hackathon, consider:

1. **Environment-based configuration**
   - Development, staging, production environments
   - Different API keys per environment

2. **Database configuration**
   - Store API keys in database
   - User authentication system
   - Multiple API keys per user

3. **Rate limiting**
   - Limit requests per API key
   - Prevent abuse

4. **API key management**
   - Key generation endpoint
   - Key revocation
   - Key expiration

---

**For now, the hardcoded setup is perfect for the hackathon! 🎉**
