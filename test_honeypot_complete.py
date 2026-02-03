"""
Comprehensive Honeypot API Test Script
Tests all three critical scenarios for GUVI validation
"""

import requests
import json

# Configuration
HONEYPOT_URL = "https://guvi-honeypot-new.onrender.com/honeypot"
VALID_API_KEY = "guvi123"
INVALID_API_KEY = "wrong_key"

print("=" * 70)
print("HONEYPOT API - COMPREHENSIVE TEST SUITE")
print("=" * 70)

# Test 1: Valid API Key (Expect 200 OK)
print("\n📝 TEST 1: Valid API Key - Should Return 200 OK")
print("-" * 70)
try:
    response = requests.post(
        HONEYPOT_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": VALID_API_KEY
        },
        json={}
    )
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        print("✅ TEST 1 PASSED: Valid authentication works!")
    else:
        print(f"❌ TEST 1 FAILED: Expected 200, got {response.status_code}")
except Exception as e:
    print(f"❌ TEST 1 FAILED: {e}")

# Test 2: Invalid/Missing API Key (Expect 401 Unauthorized)
print("\n📝 TEST 2: Invalid API Key - Should Return 401 Unauthorized")
print("-" * 70)
try:
    response = requests.post(
        HONEYPOT_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": INVALID_API_KEY
        },
        json={}
    )
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 401:
        print("✅ TEST 2 PASSED: Invalid key properly rejected!")
    else:
        print(f"❌ TEST 2 FAILED: Expected 401, got {response.status_code}")
except Exception as e:
    print(f"❌ TEST 2 FAILED: {e}")

# Test 3: Missing API Key (Expect 401 Unauthorized)
print("\n📝 TEST 3: Missing API Key - Should Return 401 Unauthorized")
print("-" * 70)
try:
    response = requests.post(
        HONEYPOT_URL,
        headers={
            "Content-Type": "application/json"
        },
        json={}
    )
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 401:
        print("✅ TEST 3 PASSED: Missing key properly rejected!")
    else:
        print(f"❌ TEST 3 FAILED: Expected 401, got {response.status_code}")
except Exception as e:
    print(f"❌ TEST 3 FAILED: {e}")

# Test 4: Malformed Request Body (Expect Controlled Error)
print("\n📝 TEST 4: Malformed Request - Should Handle Gracefully")
print("-" * 70)
try:
    response = requests.post(
        HONEYPOT_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": VALID_API_KEY
        },
        data="invalid json {{{{"  # Intentionally malformed
    )
    print(f"✅ Status Code: {response.status_code}")
    
    # Should either accept it (200) or return controlled error (400/422)
    if response.status_code in [200, 400, 422]:
        print(f"✅ TEST 4 PASSED: Malformed request handled gracefully!")
        try:
            print(f"✅ Response: {json.dumps(response.json(), indent=2)}")
        except:
            print(f"✅ Response: {response.text}")
    else:
        print(f"⚠️ TEST 4 WARNING: Unexpected status {response.status_code}")
except Exception as e:
    print(f"⚠️ TEST 4 WARNING: {e}")

# Test 5: GET Request (If supported)
print("\n📝 TEST 5: GET Request - Check if supported")
print("-" * 70)
try:
    response = requests.get(
        HONEYPOT_URL,
        headers={
            "x-api-key": VALID_API_KEY
        }
    )
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        print("✅ TEST 5 PASSED: GET request supported!")
    else:
        print(f"ℹ️ TEST 5 INFO: GET not supported or different behavior")
except Exception as e:
    print(f"ℹ️ TEST 5 INFO: {e}")

# Summary
print("\n" + "=" * 70)
print("TEST SUITE COMPLETE")
print("=" * 70)
print("\n🎯 CRITICAL TESTS FOR GUVI:")
print("   1. Valid API Key → 200 OK ✓")
print("   2. Invalid API Key → 401 Unauthorized ✓")
print("   3. Missing API Key → 401 Unauthorized ✓")
print("\nIf all three critical tests passed, your honeypot is ready for GUVI!")
print("=" * 70)
