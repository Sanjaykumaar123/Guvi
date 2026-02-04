import requests

url = "https://guvifinal.vercel.app/honeypot"

print("--- Test GET ---")
r1 = requests.get(url)
print(f"Status: {r1.status_code}, Body: {r1.text}")

print("\n--- Test POST (Empty) ---")
r2 = requests.post(url)
print(f"Status: {r2.status_code}, Body: {r2.text}")

print("\n--- Test POST (Malformed JSON) ---")
r3 = requests.post(url, headers={"Content-Type": "application/json"}, data='{"bad": json}')
print(f"Status: {r3.status_code}, Body: {r3.text}")

print("\n--- Test POST (Plain Text) ---")
r4 = requests.post(url, data="this is just text")
print(f"Status: {r4.status_code}, Body: {r4.text}")
