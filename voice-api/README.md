# AI Voice Detection API

## Deploy to Render

1. Create new Web Service
2. Connect to GitHub repo: `Sanjaykumaar123/Guvi`
3. Set Root Directory: `voice-api`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

## Test Endpoint

```bash
curl -X POST "https://your-app.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audioFormat": "wav",
    "audioBase64": "UklGRvQHAABXQVZFZm10IBAAAAABAAEA..."
  }'
```

## API Key
`guvi123`
