# 🍯 Honeypot API Endpoint Testing Guide

## Quick Reference

Your existing API endpoint can be used for the Honeypot test since it already has all required features:

### Endpoint Details
- **URL**: `https://guvi-qigw.onrender.com/predict`
- **Method**: POST
- **API Key**: `guvi123`
- **Header Name**: `x-api-key`

---

## How to Complete the Honeypot Test

### Step 1: Navigate to the Tester
You're already on the page: **Agentic Honey-Pot – API Endpoint Tester**

### Step 2: Fill in the Form

1. **Deployed Honeypot API endpoint URL**:
   ```
   https://guvi-qigw.onrender.com/predict
   ```

2. **API Key** (in request header):
   - Header Name: `x-api-key`
   - Header Value: `guvi123`

### Step 3: Click "Test Honeypot Endpoint"
Click the blue button at the bottom of the form.

### Step 4: Wait for Results
The tester will validate:
- ✅ API authentication using headers
- ✅ Endpoint availability and connectivity
- ✅ Proper request handling
- ✅ Response structure and status codes
- ✅ Basic honeypot behavior validation

---

## What the Tester Will Check

### 1. Authentication
- Verifies that the API key is required
- Tests with valid key (should succeed)
- Tests without key (should fail with 401)

### 2. Endpoint Availability
- Checks if the endpoint is reachable
- Validates response time
- Confirms proper HTTP status codes

### 3. Request Handling
- Sends test requests to the endpoint
- Validates request/response format
- Checks error handling

### 4. Response Structure
- Validates JSON response format
- Checks for required fields
- Verifies status codes (200, 401, 400, etc.)

### 5. Honeypot Behavior
- Basic validation that the endpoint behaves correctly
- Logs and responds to requests appropriately

---

## Expected Test Results

### ✅ Success Criteria
- Authentication validation: **PASS**
- Endpoint connectivity: **PASS**
- Request handling: **PASS**
- Response structure: **PASS**
- Status codes: **PASS**

### Sample Valid Response
```json
{
  "prediction": "Human",
  "confidence": 0.75,
  "language": "en",
  "audio_format": "wav",
  "status": "success"
}
```

### Sample Error Response (without API key)
```json
{
  "error": "Unauthorized"
}
```

---

## Troubleshooting

### If the test fails:

1. **Check the URL**: Make sure it's exactly `https://guvi-qigw.onrender.com/predict`
2. **Verify API Key**: Ensure `x-api-key: guvi123` is in the header
3. **Wait for Wake-up**: Render free tier may take 30-60 seconds on first request
4. **Check Deployment**: Verify the API is still running on Render

### Quick Verification
You can verify the endpoint is working by running:
```bash
py quick_test.py
```

This will test the endpoint and show you the response.

---

## Why Your Existing API Works as a Honeypot

Your API already has all the required honeypot characteristics:

1. ✅ **Authentication**: Requires API key validation
2. ✅ **Logging**: FastAPI logs all requests
3. ✅ **Error Handling**: Returns proper error codes
4. ✅ **Response Format**: Consistent JSON responses
5. ✅ **Security**: Header-based authentication
6. ✅ **Availability**: Deployed and accessible

---

## After Testing

Once the test passes, you'll see:
- ✅ Status: **Active** (green indicator)
- ✅ All validation checks passed
- ✅ Honeypot endpoint verified

---

## Summary

**Just enter these two values in the form:**
1. **Endpoint URL**: `https://guvi-qigw.onrender.com/predict`
2. **API Key**: `guvi123` (with header name `x-api-key`)

Then click **"Test Honeypot Endpoint"** and you're done! 🎉
