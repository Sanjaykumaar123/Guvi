import requests
import json

url = "https://guvifinal.vercel.app/honeypot"

print(f"Testing: {url}\n")

headers = {
    "x-api-key": "guvi123",
    "Content-Type": "application/json"
}

scenarios = [
    ("Standard POST", {"test": "data"}),
    ("Empty JSON", {}),
    ("Null Body", None),
    ("Invalid JSON Content-Type but text body", "this is not json"),
]

for name, body in scenarios:
    print(f"--- {name} ---")
    try:
        if name == "Invalid JSON Content-Type but text body":
            response = requests.post(url, headers=headers, data=body)
        elif body is None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, json=body)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    print()
