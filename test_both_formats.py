"""
Test script to verify both snake_case and camelCase work
"""

import requests
import json

# Your live API URL
API_URL = "http://localhost:8000/predict"
API_KEY = "guvi123"

# Sample base64 audio (short snippet)
SAMPLE_AUDIO = "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA"

print("="*60)
print("Testing GUVI API - Both Formats")
print("="*60)

# Test 1: snake_case (GUVI format)
print("\n1. Testing snake_case format (audio_format, audio_base64)...")
response1 = requests.post(
    API_URL,
    headers={
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    },
    json={
        "language": "en",
        "audio_format": "mp3",
        "audio_base64": SAMPLE_AUDIO
    }
)
print(f"Status: {response1.status_code}")
print(f"Response: {json.dumps(response1.json(), indent=2)}")

# Test 2: camelCase format
print("\n2. Testing camelCase format (audioFormat, audioBase64)...")
response2 = requests.post(
    API_URL,
    headers={
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    },
    json={
        "language": "en",
        "audioFormat": "mp3",
        "audioBase64": SAMPLE_AUDIO
    }
)
print(f"Status: {response2.status_code}")
print(f"Response: {json.dumps(response2.json(), indent=2)}")

print("\n" + "="*60)
if response1.status_code == 200 and response2.status_code == 200:
    print("✅ SUCCESS! Both formats work correctly!")
else:
    print("❌ One or both formats failed")
print("="*60)
