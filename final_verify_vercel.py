import requests
import json

# Replace with the actual URL from your Vercel dashboard
BASE_URL = "https://guvi-one.vercel.app" # Using the name from the screenshot pattern
API_KEY = "guvi123"

def test_endpoint(path, method="POST", payload=None):
    url = f"{BASE_URL}{path}"
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    print(f"Testing {method} {url}...")
    try:
        if method == "POST":
            response = requests.post(url, headers=headers, json=payload, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

print("=== FINAL VERIFICATION ===\n")

# 1. Health Check
test_endpoint("/", method="GET")
print("-" * 30)

# 2. Honeypot Test (Empty Body)
test_endpoint("/honeypot", method="POST", payload={})
print("-" * 30)

# 3. Honeypot Test (Malformed JSON - simulated by dict)
test_endpoint("/honeypot", method="POST", payload={"bad": "data"})
print("-" * 30)

# 4. Predict Test (Mock)
test_endpoint("/predict", method="POST", payload={
    "language": "en",
    "audioFormat": "wav",
    "audioBase64": "SGVsbG8="
})
