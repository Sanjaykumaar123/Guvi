import requests
import json

url = "https://guvi1-ten.vercel.app/honeypot"

print("=== Simulating GUVI Tester Requests ===\n")

# Test 1: Exactly as GUVI might send it
print("Test 1: POST with Content-Type: application/json but NO body")
response = requests.post(
    url,
    headers={
        "x-api-key": "guvi123",
        "Content-Type": "application/json"
    }
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}\n")

# Test 2: With empty JSON object
print("Test 2: POST with empty JSON object")
response = requests.post(
    url,
    headers={
        "x-api-key": "guvi123",
        "Content-Type": "application/json"
    },
    data="{}"
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}\n")

# Test 3: With null body
print("Test 3: POST with null")
response = requests.post(
    url,
    headers={
        "x-api-key": "guvi123",
        "Content-Type": "application/json"
    },
    data="null"
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}\n")

# Test 4: With invalid JSON
print("Test 4: POST with invalid JSON")
response = requests.post(
    url,
    headers={
        "x-api-key": "guvi123",
        "Content-Type": "application/json"
    },
    data="{"
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}\n")

# Test 5: With text/plain
print("Test 5: POST with text/plain")
response = requests.post(
    url,
    headers={
        "x-api-key": "guvi123",
        "Content-Type": "text/plain"
    },
    data="test"
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}\n")

print("\n=== Summary ===")
print("If ALL tests above return 200 OK, then your endpoint is perfect.")
print("The GUVI tester error is likely a bug on their end.")
