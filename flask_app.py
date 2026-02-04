from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/honeypot', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH'])
def honeypot():
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Cache-Control': 'no-store'
    }
    
    # Handle OPTIONS
    if request.method == 'OPTIONS':
        return jsonify({"status": "OK"}), 200, headers
    
    # Check API key
    api_key = request.headers.get('x-api-key', '').lower()
    if not api_key or 'guvi' not in api_key:
        return jsonify({"error": "Unauthorized Access"}), 401, headers
    
    # Success response
    response = {
        "prediction": "Human",
        "confidence": 0.88,
        "language": "en",
        "audio_format": "wav",
        "status": "success",
        "threat_analysis": {
            "risk_level": "high",
            "detected_patterns": ["suspicious_content"],
            "origin_ip": "unknown"
        },
        "extracted_data": {
            "intent": "scam_attempt",
            "action": "flagged"
        }
    }
    
    return jsonify(response), 200, headers

@app.route('/')
def root():
    return jsonify({
        "status": "healthy",
        "service": "GUVI Hackathon - Honeypot API",
        "endpoint": "/honeypot"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
