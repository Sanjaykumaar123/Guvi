
import requests
import json

URL = "https://guvifinal.vercel.app/honeypot"
HEADERS = {"x-api-key": "guvi123"}

def test(name, data=None, json_data=None, headers=None):
    if headers is None:
        headers = HEADERS
    
    print(f"--- Testing {name} ---")
    try:
        if json_data is not None:
            r = requests.post(URL, headers=headers, json=json_data)
        else:
            r = requests.post(URL, headers=headers, data=data)
        
        print(f"Status: {r.status_code}")
        print(f"Response: {r.text}")
    except Exception as e:
        print(f"Error: {e}")
    print()

print(f"Testing Remote URL: {URL}\n")

# 1. Standard valid request
test("Valid JSON", json_data={"foo": "bar"})

# 2. Empty body
test("Empty Body", data="")

# 3. Invalid JSON string
test("Invalid JSON", data="{ bad json")

# 4. No Headers
test("No Headers", headers={}, json_data={})

# 5. OPTIONS
print("--- Testing OPTIONS ---")
try:
    r = requests.options(URL)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
