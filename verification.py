import requests
import time
import subprocess
import os
import sys

def test_api():
    base_url = "http://127.0.0.1:8000"
    
    print("--- 1. Testing Root / ---")
    try:
        r = requests.get(f"{base_url}/")
        print(f"Status: {r.status_code}, Body: {r.json()}")
    except Exception as e:
        print(f"FAILED: {e}")

    print("\n--- 2. Testing /predict with NO API KEY ---")
    r = requests.post(f"{base_url}/predict", json={"audioBase64": "test"})
    print(f"Status: {r.status_code} (Expected 401), Body: {r.json()}")

    print("\n--- 3. Testing /predict with VALID API KEY ---")
    r = requests.post(f"{base_url}/predict", 
                      headers={"x-api-key": "guvi123"}, 
                      json={"audioBase64": "SGVsbG8="})
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

    print("\n--- 4. Testing /predict with MISSING audioBase64 ---")
    r = requests.post(f"{base_url}/predict", 
                      headers={"x-api-key": "guvi123"}, 
                      json={"language": "fr"})
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

    print("\n--- 5. Testing /predict with MALFORMED JSON ---")
    r = requests.post(f"{base_url}/predict", 
                      headers={"x-api-key": "guvi123", "Content-Type": "application/json"}, 
                      data="{'invalid': json}")
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

    print("\n--- 6. Testing /honeypot with NO API KEY (GET) ---")
    r = requests.get(f"{base_url}/honeypot")
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

    print("\n--- 7. Testing /honeypot with PLAIN TEXT (POST) ---")
    r = requests.post(f"{base_url}/honeypot", data="This is plain text scam message")
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

    print("\n--- 8. Testing /honeypot with DELETE method ---")
    r = requests.delete(f"{base_url}/honeypot")
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

    print("\n--- 9. Testing /predict with WRONG METHOD (GET) ---")
    r = requests.get(f"{base_url}/predict", headers={"x-api-key": "guvi123"})
    print(f"Status: {r.status_code} (Expected 200), Body: {r.json()}")

if __name__ == "__main__":
    test_api()
