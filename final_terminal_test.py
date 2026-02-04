import requests
import json
import sys

def run_test(url, api_key):
    print(f"🚀 Starting Final Verification for: {url}")
    print("-" * 50)
    
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    
    # 1. Test Root
    try:
        r = requests.get(url, timeout=10)
        print(f"Root (/) Status: {r.status_code}")
        print(f"Root Response: {r.text}")
    except Exception as e:
        print(f"Root Test Failed: {e}")

    # 2. Test Honeypot
    honeypot_url = f"{url.rstrip('/')}/honeypot"
    print(f"\nTesting Honeypot: {honeypot_url}")
    try:
        # Test with empty body (as GUVI tester often does)
        r = requests.post(honeypot_url, headers=headers, data="", timeout=10)
        print(f"Honeypot Status: {r.status_code}")
        print(f"Honeypot Response: {json.dumps(r.json(), indent=2)}")
    except Exception as e:
        print(f"Honeypot Test Failed: {e}")

    # 3. Test Predict
    predict_url = f"{url.rstrip('/')}/predict"
    print(f"\nTesting Predict: {predict_url}")
    payload = {
        "language": "en",
        "audioFormat": "wav",
        "audioBase64": "SGVsbG8="
    }
    try:
        r = requests.post(predict_url, headers=headers, json=payload, timeout=10)
        print(f"Predict Status: {r.status_code}")
        print(f"Predict Response: {json.dumps(r.json(), indent=2)}")
    except Exception as e:
        print(f"Predict Test Failed: {e}")

    print("-" * 50)
    print("✅ Final Verification Complete!")

if __name__ == "__main__":
    # If URL provided as argument use it, otherwise use the likely Vercel URL
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        # Placeholder - user will likely provide or I'll use the one from context if found
        target_url = "https://guvipro.vercel.app" 
    
    run_test(target_url, "guvi123")
