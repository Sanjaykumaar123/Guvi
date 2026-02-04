# 🧪 Testing Your Deployed API on GUVI Platform

## Your Deployment Details

**Deployed URL:** `https://guvi-unified-api.onrender.com`

---

## How to Fill the GUVI Endpoint Tester Form

Based on the screenshot, here's exactly what to enter in each field:

### 1. **Headers** ✅
```
x-api-key
```

### 2. **x-api-key** ✅
```
guvi123
```

### 3. **Endpoint URL** ✅
```
https://guvi-unified-api.onrender.com/predict
```

### 4. **Request Body** ✅

#### **Language:**
```
en
```

#### **Audio Format:**
```
wav
```

#### **Audio Base64 Format:**
For testing, you can use this small sample base64 audio (440Hz tone, 1 second):
```
UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAAB9AAACABAAZGF0YQAAAAA=
```

Or generate a proper one using the Python script below.

---

## 🎯 Quick Test with Python

If you want to generate a valid base64 audio sample:

```python
import base64
import wave
import struct
import math

# Generate 1 second of 440Hz tone
sample_rate = 44100
duration = 1
frequency = 440

samples = []
for i in range(sample_rate * duration):
    value = int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate))
    samples.append(value)

# Write to WAV file
filename = "test_audio.wav"
with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    for sample in samples:
        wav_file.writeframes(struct.pack('h', sample))

# Read and encode to base64
with open(filename, "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode('utf-8')
    print("Base64 Audio (copy this):")
    print(audio_base64)
```

---

## 🧪 Test with cURL (Alternative)

```bash
curl -X POST "https://guvi-unified-api.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audio_format": "wav",
    "audio_base64": "UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAAB9AAACABAAZGF0YQAAAAA="
  }'
```

---

## ✅ Expected Response

If everything works correctly, you should get:

```json
{
  "prediction": "AI",
  "confidence": 0.87,
  "language": "en",
  "audio_format": "wav",
  "status": "success"
}
```

Or:

```json
{
  "prediction": "Human",
  "confidence": 0.73,
  "language": "en",
  "audio_format": "wav",
  "status": "success"
}
```

---

## ⚠️ Important Notes

1. **Render Free Tier:** Your app might be sleeping. The first request may take 30-60 seconds to wake up.
2. **Timeout:** If you get a timeout, wait a moment and try again.
3. **API Key:** Make sure you include `x-api-key: guvi123` in the headers.

---

## 🔍 Troubleshooting

### If you get "Unauthorized" error:
- Check that you've added the header `x-api-key` with value `guvi123`

### If you get timeout:
- Wait 1-2 minutes for Render to wake up the service
- Try the health check first: `https://guvi-unified-api.onrender.com/`

### If you get "Invalid base64" error:
- Make sure the base64 string has no line breaks or spaces
- Use the sample base64 provided above

---

## 🎉 Testing Steps

1. **Wake up the service** (optional but recommended):
   - Visit: `https://guvi-unified-api.onrender.com/` in your browser
   - Wait for response (may take 30-60 seconds first time)

2. **Fill the GUVI form** with the values above

3. **Click "Test Endpoint"**

4. **Wait for response** (first request may be slow)

5. **Verify success** - You should see a JSON response with prediction and confidence

---

Good luck with your testing! 🚀
