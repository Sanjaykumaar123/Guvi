import requests

url = "https://guvi1-ten.vercel.app/honeypot"
headers = {"x-api-key": "guvi123"}

print(f"Testing: {url}\n")

# Test 1
print("=== Test 1: POST ===")
response = requests.post(url, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# Test 2: Multiple requests
print("=== Test 2: 5 rapid requests ===")
for i in range(5):
    response = requests.post(url, headers=headers)
    print(f"{i+1}. Status: {response.status_code} - {response.json().get('status', 'ERROR')}")
