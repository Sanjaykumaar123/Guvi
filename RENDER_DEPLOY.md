# Deploy to Render (No Rate Limits)

## Quick Steps:

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repo: `Sanjaykumaar123/Guvi`
4. Configure:
   - **Name**: `guvi-honeypot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: `Free`

5. Click "Create Web Service"

6. Wait 2-3 minutes for deployment

7. Your URL will be: `https://guvi-honeypot.onrender.com/honeypot`

8. Use this URL in the GUVI tester with API key: `guvi123`

## Why Render?
- No request limits on free tier
- Better for APIs that get tested repeatedly
- More stable than Vercel for this use case
