# Deploy to Render - Complete Guide

## Step 1: Prepare Your Repository

Your code is ready! Just commit the Procfile:

```bash
git add Procfile
git commit -m "Add Procfile for Render"
git push
```

## Step 2: Create Render Account & Deploy

1. **Go to**: https://render.com
2. **Sign up/Login** (use GitHub to connect your repo)
3. Click **"New +"** → **"Web Service"**
4. **Connect your repository**: `Sanjaykumaar123/Guvi`
5. **Configure the service**:

### Configuration Settings:

| Setting | Value |
|---------|-------|
| **Name** | `guvi-honeypot` (or any name you like) |
| **Region** | Singapore (closest to India) |
| **Branch** | `main` |
| **Root Directory** | (leave blank) |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` |

6. Click **"Create Web Service"**

## Step 3: Wait for Deployment

- Render will automatically build and deploy your app
- This takes about 2-3 minutes
- You'll see build logs in real-time
- Once it shows "Live", your app is ready!

## Step 4: Get Your URL

Your URL will be: `https://guvi-honeypot.onrender.com/honeypot`

(Replace `guvi-honeypot` with whatever name you chose)

## Step 5: Test Your Endpoint

Use this URL in the GUVI tester:
- **URL**: `https://guvi-honeypot.onrender.com/honeypot`
- **Header**: `x-api-key: guvi123`

## Why Render is Better for This:

✅ **No rate limits** on free tier
✅ **No request quotas** 
✅ **Always-on** (doesn't sleep like some platforms)
✅ **Faster cold starts** than Vercel for Python
✅ **Better for APIs** that get tested repeatedly

## Troubleshooting:

If deployment fails:
- Check the build logs in Render dashboard
- Make sure `requirements.txt` is committed
- Verify the start command is correct

## After Deployment:

Once deployed, your endpoint will work consistently without the "5 times then fail" issue you had with Vercel!
