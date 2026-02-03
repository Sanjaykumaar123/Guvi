"""
Test the minimal honeypot endpoint
"""

import requests
import json

URL = "https://guvi-qigw.onrender.com/honeypot"

print("Testing Honeypot Endpoint")
print("=" * 60)

# Test 1: With valid API key
print("\nTest 1: Valid API Key")
response = requests.get(URL, headers={"x-api-key": "guvi123"})
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 2: Without API key
print("\nTest 2: No API Key")
response = requests.get(URL)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 3: Wrong API key
print("\nTest 3: Wrong API Key")
response = requests.get(URL, headers={"x-api-key": "wrong"})
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

print("\n" + "=" * 60)
print("For GUVI: Use GET /honeypot with header x-api-key: guvi123")
