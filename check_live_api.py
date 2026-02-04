import requests
import json

url = "https://guvi-2-2cm7.onrender.com/honeypot"
headers = {"x-api-key": "guvi123"}

print(f"Testing GET to {url}...")
try:
    r = requests.get(url, headers=headers)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}\n")
except Exception as e:
    print(f"Error: {e}\n")

print(f"Testing POST with empty body to {url}...")
try:
    r = requests.post(url, headers=headers)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}\n")
except Exception as e:
    print(f"Error: {e}\n")

print(f"Testing POST with JSON body to {url}...")
try:
    r = requests.post(url, headers=headers, json={"test": "data"})
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}\n")
except Exception as e:
    print(f"Error: {e}\n")
