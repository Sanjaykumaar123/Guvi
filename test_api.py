"""
Test script for AI Voice Detection API
Generates a sample audio file and tests the API endpoint
"""

import requests
import base64
import json
import wave
import struct
import math

def generate_sample_audio(filename="test_audio.wav", duration=2, frequency=440):
    """
    Generate a simple sine wave audio file for testing
    This simulates a real audio file without needing external dependencies
    """
    sample_rate = 44100
    num_samples = duration * sample_rate
    
    # Generate sine wave
    samples = []
    for i in range(num_samples):
        value = int(32767 * math.sin(2 * math.pi * frequency * i / sample_rate))
        samples.append(value)
    
    # Write to WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes per sample
        wav_file.setframerate(sample_rate)
        
        for sample in samples:
            wav_file.writeframes(struct.pack('h', sample))
    
    print(f"✅ Generated test audio file: {filename}")
    return filename


def test_api(api_url="http://localhost:8000", audio_file="test_audio.wav"):
    """
    Test the AI Voice Detection API with various scenarios
    """
    print("\n" + "="*60)
    print("🧪 AI Voice Detection API - Test Suite")
    print("="*60 + "\n")
    
    # Read and encode audio file
    try:
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        print(f"✅ Loaded audio file: {audio_file} ({len(audio_bytes)} bytes)")
        print(f"   Base64 length: {len(audio_base64)} characters\n")
    except FileNotFoundError:
        print(f"❌ Error: Audio file '{audio_file}' not found")
        print("   Generating a sample audio file...\n")
        audio_file = generate_sample_audio()
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    
    # Test 1: Valid request with correct API key
    print("Test 1: Valid Request with Correct API Key")
    print("-" * 60)
    
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "guvi123"
    }
    
    data = {
        "language": "en",
        "audio_format": "wav",
        "audio_base64": audio_base64
    }
    
    try:
        response = requests.post(f"{api_url}/predict", json=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✅ Test 1 PASSED\n")
        else:
            print("❌ Test 1 FAILED\n")
    except Exception as e:
        print(f"❌ Test 1 FAILED: {str(e)}\n")
    
    # Test 2: Missing API key
    print("Test 2: Missing API Key (Should Return 401)")
    print("-" * 60)
    
    headers_no_key = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(f"{api_url}/predict", json=data, headers=headers_no_key)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 401 and "Unauthorized" in str(response.json()):
            print("✅ Test 2 PASSED\n")
        else:
            print("❌ Test 2 FAILED\n")
    except Exception as e:
        print(f"❌ Test 2 FAILED: {str(e)}\n")
    
    # Test 3: Invalid API key
    print("Test 3: Invalid API Key (Should Return 401)")
    print("-" * 60)
    
    headers_wrong_key = {
        "Content-Type": "application/json",
        "x-api-key": "wrong_key_123"
    }
    
    try:
        response = requests.post(f"{api_url}/predict", json=data, headers=headers_wrong_key)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 401 and "Unauthorized" in str(response.json()):
            print("✅ Test 3 PASSED\n")
        else:
            print("❌ Test 3 FAILED\n")
    except Exception as e:
        print(f"❌ Test 3 FAILED: {str(e)}\n")
    
    # Test 4: Invalid base64
    print("Test 4: Invalid Base64 Data (Should Return 400)")
    print("-" * 60)
    
    invalid_data = {
        "language": "en",
        "audio_format": "mp3",
        "audio_base64": "this_is_not_valid_base64!!!"
    }
    
    try:
        response = requests.post(f"{api_url}/predict", json=invalid_data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 400:
            print("✅ Test 4 PASSED\n")
        else:
            print("❌ Test 4 FAILED\n")
    except Exception as e:
        print(f"❌ Test 4 FAILED: {str(e)}\n")
    
    # Test 5: Missing required field
    print("Test 5: Missing Required Field (Should Return 422)")
    print("-" * 60)
    
    incomplete_data = {
        "language": "en",
        "audio_format": "mp3"
        # Missing audio_base64
    }
    
    try:
        response = requests.post(f"{api_url}/predict", json=incomplete_data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 422:
            print("✅ Test 5 PASSED\n")
        else:
            print("❌ Test 5 FAILED\n")
    except Exception as e:
        print(f"❌ Test 5 FAILED: {str(e)}\n")
    
    # Test 6: Health check endpoint
    print("Test 6: Health Check Endpoint")
    print("-" * 60)
    
    try:
        response = requests.get(f"{api_url}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✅ Test 6 PASSED\n")
        else:
            print("❌ Test 6 FAILED\n")
    except Exception as e:
        print(f"❌ Test 6 FAILED: {str(e)}\n")
    
    # Test 7: Different audio formats
    print("Test 7: Different Audio Formats")
    print("-" * 60)
    
    formats_to_test = ["mp3", "wav", "ogg", "flac"]
    
    for fmt in formats_to_test:
        test_data = {
            "language": "en",
            "audio_format": fmt,
            "audio_base64": audio_base64
        }
        
        try:
            response = requests.post(f"{api_url}/predict", json=test_data, headers=headers)
            result = "✅" if response.status_code == 200 else "❌"
            print(f"{result} Format '{fmt}': Status {response.status_code}")
        except Exception as e:
            print(f"❌ Format '{fmt}': {str(e)}")
    
    print("\n✅ Test 7 COMPLETED\n")
    
    print("="*60)
    print("🎉 Test Suite Completed!")
    print("="*60)


if __name__ == "__main__":
    import sys
    
    # Check if API URL is provided as argument
    api_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    
    print(f"\n🎯 Testing API at: {api_url}")
    print("   Make sure the API server is running!\n")
    
    # Generate sample audio and run tests
    test_api(api_url)
