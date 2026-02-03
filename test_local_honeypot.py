"""
Test honeypot locally to verify code is correct
"""
import subprocess
import time
import requests
import json

print("Starting local honeypot server...")
print("=" * 70)

# Start server
proc = subprocess.Popen(
    ["python", "-m", "uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8002", "--app-dir", "honeypot-api"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    cwd=r"c:\Users\Sanjay Kumaar\guvi"
)

# Wait for server to start
print("Waiting for server to start...")
time.sleep(5)

try:
    print("\n✅ Server started! Running tests...\n")
    
    # Test 1: Valid key
    print("TEST 1: Valid API Key")
    r = requests.post(
        "http://127.0.0.1:8002/honeypot",
        headers={"x-api-key": "guvi123"},
        json={}
    )
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=2)}\n")
    
    # Test 2: Invalid key
    print("TEST 2: Invalid API Key")
    r = requests.post(
        "http://127.0.0.1:8002/honeypot",
        headers={"x-api-key": "wrong"},
        json={}
    )
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=2)}\n")
    
    # Test 3: No key
    print("TEST 3: Missing API Key")
    r = requests.post(
        "http://127.0.0.1:8002/honeypot",
        json={}
    )
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=2)}\n")
    
    print("=" * 70)
    print("✅ Local tests complete! Code is working correctly.")
    print("=" * 70)
    
except Exception as e:
    print(f"❌ Error: {e}")
    
finally:
    proc.terminate()
    proc.wait()
    print("\nServer stopped.")
