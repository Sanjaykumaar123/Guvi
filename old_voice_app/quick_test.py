"""
Quick test script for the deployed API
"""
import requests
import json

# Read the base64 audio
with open("audio_base64.txt", "r") as f:
    audio_base64 = f.read().strip()

# API details
url = "https://guvi-qigw.onrender.com/predict"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "guvi123"
}
data = {
    "language": "en",
    "audio_format": "wav",
    "audio_base64": audio_base64
}

print("🚀 Testing deployed API...")
print(f"URL: {url}")
print(f"Headers: {headers}")
print(f"Audio size: {len(audio_base64)} characters\n")

try:
    response = requests.post(url, json=data, headers=headers, timeout=60)
    
    print(f"✅ Status Code: {response.status_code}")
    print(f"📊 Response:")
    print(json.dumps(response.json(), indent=2))
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
