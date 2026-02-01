# Sample cURL commands for testing the API

# ============================================
# 1. HEALTH CHECK
# ============================================
curl http://localhost:8000/


# ============================================
# 2. VALID REQUEST (You need to replace the base64 string with actual audio)
# ============================================
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA//tQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWGluZwAAAA8AAAACAAADhAC7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7u7//////////////////////////////////////////////////////////////////8AAAAATGF2YzU4LjEzAAAAAAAAAAAAAAAAJAAAAAAAAAAAA4S+FqVmAAAAAAD/+9DEAAAP8Uy0AABpNwAAA0gAAAAATEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"
  }'


# ============================================
# 3. MISSING API KEY (Should return 401)
# ============================================
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA"
  }'


# ============================================
# 4. INVALID API KEY (Should return 401)
# ============================================
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: wrong_key" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA"
  }'


# ============================================
# 5. MISSING REQUIRED FIELD (Should return 422)
# ============================================
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audio_format": "mp3"
  }'


# ============================================
# 6. INVALID BASE64 (Should return 400)
# ============================================
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -H "x-api-key: guvi123" \
  -d '{
    "language": "en",
    "audio_format": "mp3",
    "audio_base64": "invalid_base64_data!!!"
  }'


# ============================================
# HOW TO ENCODE YOUR OWN AUDIO FILE
# ============================================

# On Linux/Mac:
# base64 -i your_audio.mp3 | tr -d '\n' > audio_base64.txt

# On Windows PowerShell:
# [Convert]::ToBase64String([IO.File]::ReadAllBytes("your_audio.mp3")) | Out-File -NoNewline audio_base64.txt

# Then use the content of audio_base64.txt in your curl command
