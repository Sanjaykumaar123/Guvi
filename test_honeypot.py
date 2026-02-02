"""
Test the Honeypot Endpoint Locally
This script tests the /honeypot endpoint to ensure it works correctly
"""

import requests
import json

# Test locally first
LOCAL_URL = "http://localhost:8000/honeypot"
DEPLOYED_URL = "https://guvi-qigw.onrender.com/honeypot"

def test_honeypot(url, description):
    """Test the honeypot endpoint"""
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"URL: {url}")
    print(f"{'='*60}\n")
    
    # Test 1: With valid API key
    print("Test 1: Valid API Key")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "guvi123"
    }
    
    try:
        response = requests.post(url, headers=headers, json={}, timeout=10)
        print(f"✅ Status Code: {response.status_code}")
        print(f"📊 Response:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 2: Without API key (should fail)
    print(f"\n{'-'*60}")
    print("Test 2: Missing API Key (should return 401)")
    try:
        response = requests.post(url, json={}, timeout=10)
        print(f"✅ Status Code: {response.status_code}")
        print(f"📊 Response:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 3: With invalid API key (should fail)
    print(f"\n{'-'*60}")
    print("Test 3: Invalid API Key (should return 401)")
    headers_invalid = {
        "Content-Type": "application/json",
        "x-api-key": "wrong_key"
    }
    try:
        response = requests.post(url, headers=headers_invalid, json={}, timeout=10)
        print(f"✅ Status Code: {response.status_code}")
        print(f"📊 Response:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("\n🍯 HONEYPOT ENDPOINT TESTING")
    print("="*60)
    
    # Test deployed endpoint
    test_honeypot(DEPLOYED_URL, "Deployed Honeypot Endpoint (Render)")
    
    print(f"\n\n{'='*60}")
    print("✅ TESTING COMPLETE!")
    print("="*60)
    print("\nFor GUVI Honeypot Tester, use:")
    print(f"  URL: {DEPLOYED_URL}")
    print(f"  API Key: guvi123")
    print(f"  Header: x-api-key")
