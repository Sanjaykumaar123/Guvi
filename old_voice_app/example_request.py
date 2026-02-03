"""
Simple example showing how to make a request to the API
This generates a tiny audio sample and sends it to the API
"""

import requests
import base64
import json
import wave
import struct
import math

def create_test_audio():
    """Create a minimal WAV file for testing"""
    # Generate 1 second of 440Hz tone (A note)
    sample_rate = 44100
    duration = 1
    frequency = 440
    
    samples = []
    for i in range(sample_rate * duration):
        value = int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate))
        samples.append(value)
    
    # Write to WAV file
    filename = "example_audio.wav"
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for sample in samples:
            wav_file.writeframes(struct.pack('h', sample))
    
    return filename

def test_api_request():
    """Send a test request to the API"""
    
    print("=" * 60)
    print("AI Voice Detection API - Example Request")
    print("=" * 60)
    
    # Step 1: Create test audio
    print("\n1. Creating test audio file...")
    audio_file = create_test_audio()
    print(f"   ✅ Created: {audio_file}")
    
    # Step 2: Read and encode audio
    print("\n2. Encoding audio to base64...")
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    print(f"   ✅ Encoded {len(audio_bytes)} bytes")
    
    # Step 3: Prepare request
    print("\n3. Preparing API request...")
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
    print(f"   ✅ URL: {url}")
    print(f"   ✅ Headers: {headers}")
    
    # Step 4: Send request
    print("\n4. Sending request to API...")
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        
        print(f"\n   Status Code: {response.status_code}")
        print(f"\n   Response:")
        print(json.dumps(response.json(), indent=2))
        
        if response.status_code == 200:
            print("\n   ✅ SUCCESS! API is working correctly.")
            result = response.json()
            print(f"\n   📊 Prediction: {result['prediction']}")
            print(f"   📊 Confidence: {result['confidence']}")
        else:
            print("\n   ❌ Request failed!")
            
    except requests.exceptions.ConnectionError:
        print("\n   ❌ ERROR: Could not connect to API")
        print("   Make sure the server is running:")
        print("   → python main.py")
    except Exception as e:
        print(f"\n   ❌ ERROR: {str(e)}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_api_request()
