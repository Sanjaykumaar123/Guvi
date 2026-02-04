import requests

url = "https://guvi1-success.vercel.app/honeypot"
headers = {"x-api-key": "guvi123"}

print(f"Testing: {url}")
print(f"Headers: {headers}\n")

# Test 1: Valid request
print("=== Test 1: Valid POST ===")
response = requests.post(url, headers=headers, json={})
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# Test 2: No body
print("=== Test 2: No body ===")
response = requests.post(url, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# Test 3: Invalid JSON
print("=== Test 3: Invalid JSON ===")
response = requests.post(url, headers=headers, data="invalid")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# Test 4: Multiple rapid requests
print("=== Test 4: 10 Rapid Requests ===")
for i in range(10):
    response = requests.post(url, headers=headers, json={})
    print(f"Request {i+1}: {response.status_code}")
