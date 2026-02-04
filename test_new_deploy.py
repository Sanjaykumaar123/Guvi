import requests
import json

# Test the new deployment
url = "https://guvi-2-iam.vercel.app/honeypot"
headers = {"x-api-key": "guvi123"}

print(f"Testing: {url}\n")

# Test 1: POST with empty body
print("=== Test 1: POST with empty body ===")
try:
    response = requests.post(url, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")
except Exception as e:
    print(f"Error: {e}\n")

# Test 2: POST with JSON body
print("=== Test 2: POST with JSON body ===")
try:
    response = requests.post(url, headers=headers, json={"test": "data"})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")
except Exception as e:
    print(f"Error: {e}\n")

# Test 3: POST with invalid body
print("=== Test 3: POST with invalid text body ===")
try:
    response = requests.post(url, headers=headers, data="invalid text")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")
except Exception as e:
    print(f"Error: {e}\n")

# Test 4: GET request
print("=== Test 4: GET request ===")
try:
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")
except Exception as e:
    print(f"Error: {e}\n")
