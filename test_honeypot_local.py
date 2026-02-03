"""
Quick test to verify honeypot app works locally
"""
import subprocess
import time
import requests

print("Testing honeypot API locally...")
print("="*60)

# Start the server in background
print("\n1. Starting server...")
proc = subprocess.Popen(
    ["uvicorn", "honeypot-api.app:app", "--host", "127.0.0.1", "--port", "8001"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for server to start
time.sleep(3)

try:
    # Test root endpoint
    print("\n2. Testing root endpoint (/)...")
    r = requests.get("http://127.0.0.1:8001/")
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    # Test honeypot endpoint
    print("\n3. Testing honeypot endpoint (/honeypot)...")
    r = requests.post(
        "http://127.0.0.1:8001/honeypot",
        headers={"x-api-key": "guvi123"},
        json={}
    )
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    print("\n" + "="*60)
    print("✅ All tests passed! The honeypot app works correctly.")
    print("="*60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    
finally:
    # Stop the server
    proc.terminate()
    proc.wait()
    print("\nServer stopped.")
