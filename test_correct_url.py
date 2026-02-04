import requests

url = "https://guvi-2uam.vercel.app/honeypot"
headers = {"x-api-key": "guvi123"}

print(f"Testing: {url}\n")

# Test exactly like GUVI tester would
print("=== Test: POST with empty/invalid body ===")
response = requests.post(url, headers=headers)
print(f"Status: {response.status_code}")
print(f"Headers: {dict(response.headers)}")
print(f"Response: {response.text}\n")

# Test with JSON
print("=== Test: POST with JSON ===")
response = requests.post(url, headers=headers, json={})
print(f"Status: {response.status_code}")
print(f"Response: {response.text}\n")

# Multiple rapid requests
print("=== Test: 10 rapid requests ===")
for i in range(10):
    response = requests.post(url, headers=headers)
    print(f"{i+1}. Status: {response.status_code}")
