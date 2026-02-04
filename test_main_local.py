
import subprocess
import time
import json
import sys
import urllib.request
import urllib.error

print(f"Starting local unified server with {sys.executable}...")
# Start server using main.py
proc = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8003"],
    cwd=r"c:\Users\Sanjay Kumaar\guvi"
)

def make_request(url, headers=None, data=None):
    if headers is None:
        headers = {}
    
    req = urllib.request.Request(url, headers=headers)
    if data is not None:
        if isinstance(data, str):
            req.data = data.encode('utf-8')
        else:
            req.data = data # Assuming bytes
            
    try:
        with urllib.request.urlopen(req) as response:
            return response.status, response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')
    except Exception as e:
        return 0, str(e)

try:
    print("Waiting for server to start...")
    time.sleep(5)
    
    url = "http://127.0.0.1:8003/honeypot"
    headers = {"x-api-key": "guvi123", "Content-Type": "application/json"}
    
    print("\n--- Test 1: Empty Body ---")
    status, body = make_request(url, headers, "")
    print(f"Status: {status}")
    print(f"Response: {body}")

    print("\n--- Test 2: Invalid JSON ---")
    status, body = make_request(url, headers, "{invalid_json")
    print(f"Status: {status}")
    print(f"Response: {body}")

    print("\n--- Test 3: Valid JSON ---")
    status, body = make_request(url, headers, json.dumps({"key": "value"}))
    print(f"Status: {status}")
    print(f"Response: {body}")

finally:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except:
        proc.kill()
    print("\nServer stopped.")
