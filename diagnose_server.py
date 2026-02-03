import requests
import json

URL = "https://guvi-qigw.onrender.com/honeypot"
HEADERS = {"x-api-key": "guvi123", "Content-Type": "application/json"}

print("🔍 DIAGNOSTIC TEST FOR GUVI HONEYPOT")
print("="*60)

# Test 1: POST with JSON body (Simulating 'Intelligence' request)
print("\n1. Testing POST with JSON Body...")
try:
    data = {"message": "You have won a lottery"}
    response = requests.post(URL, headers=HEADERS, json=data)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:200]}")
except Exception as e:
    print(f"   ERROR: {e}")

# Test 2: POST with Empty Body
print("\n2. Testing POST with Empty Body...")
try:
    response = requests.post(URL, headers=HEADERS)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:200]}")
except Exception as e:
    print(f"   ERROR: {e}")

# Test 3: POST with Invalid JSON (Text)
print("\n3. Testing POST with Malformed Body...")
try:
    response = requests.post(URL, headers=HEADERS, data="This is not JSON")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:200]}")
except Exception as e:
    print(f"   ERROR: {e}")

# Test 4: Root Health Check
print("\n4. Testing Root Health Check (GET /)...")
try:
    response = requests.get("https://guvi-qigw.onrender.com/")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:200]}")
except Exception as e:
    print(f"   ERROR: {e}")
