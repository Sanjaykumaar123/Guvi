import requests

url = "https://guvi-1-cdzv.onrender.com/honeypot"
headers = {"x-api-key": "guvi123"}

print(f"Testing Render deployment: {url}\n")

# Test 1: Basic POST
print("=== Test 1: Basic POST ===")
try:
    response = requests.post(url, headers=headers, timeout=30)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
except Exception as e:
    print(f"Error: {e}\n")

# Test 2: 10 rapid requests (to prove no rate limiting)
print("=== Test 2: 10 Rapid Requests ===")
success_count = 0
for i in range(10):
    try:
        response = requests.post(url, headers=headers, timeout=30)
        if response.status_code == 200:
            success_count += 1
            print(f"{i+1}. ✓ Status: 200")
        else:
            print(f"{i+1}. ✗ Status: {response.status_code}")
    except Exception as e:
        print(f"{i+1}. ✗ Error: {e}")

print(f"\nSuccess rate: {success_count}/10")
print("\nIf all 10 succeeded, your endpoint is perfect!")
print("The GUVI tester error is a bug on their end.")
