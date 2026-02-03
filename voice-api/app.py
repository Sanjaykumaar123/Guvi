"""
Voice Authenticity Detection Service
Created for GUVI x HCL Hackathon 2026
Author: Sanjay Kumaar

This service analyzes audio samples to determine if they are
synthetically generated or naturally spoken by humans.
"""

from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator, ConfigDict
import base64
import os
import tempfile
import random
from typing import Optional
import logging

# Setup application logger
log_handler = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create FastAPI application instance
service = FastAPI(
    title="Voice Authenticity Detector",
    description="Analyzes audio to distinguish between AI-synthesized and human voices",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Authentication credentials
AUTH_TOKEN = "guvi123"

# Acceptable audio file extensions
ALLOWED_AUDIO_TYPES = ["mp3", "wav", "ogg", "flac", "m4a"]


class VoiceAnalysisRequest(BaseModel):
    """
    Schema for incoming voice analysis requests
    Accepts both snake_case and camelCase field names for flexibility
    """
    model_config = ConfigDict(populate_by_name=True)
    
    language: str = Field(..., description="ISO language code (e.g., 'en', 'hi', 'ta', 'es')")
    audio_format: str = Field(..., alias="audioFormat", description="File extension (mp3, wav, ogg, flac, m4a)")
    audio_base64: str = Field(..., alias="audioBase64", description="Base64-encoded audio content")

    @field_validator('audio_format')
    @classmethod
    def check_format_validity(cls, format_value):
        """Validates that the audio format is in our supported list"""
        normalized_format = format_value.lower().strip()
        if normalized_format not in ALLOWED_AUDIO_TYPES:
            raise ValueError(
                f"Format '{format_value}' not supported. "
                f"Please use one of: {', '.join(ALLOWED_AUDIO_TYPES)}"
            )
        return normalized_format

    @field_validator('audio_base64')
    @classmethod
    def check_base64_content(cls, encoded_data):
        """Ensures the base64 audio data is not empty"""
        if not encoded_data or not encoded_data.strip():
            raise ValueError("Audio data cannot be empty")
        return encoded_data.strip()


class AnalysisResult(BaseModel):
    """Schema for successful analysis responses"""
    prediction: str
    confidence: float
    language: str
    audio_format: str
    status: str = "success"


def authenticate_request(x_api_key: Optional[str] = Header(None)) -> bool:
    """
    Validates the API key provided in request headers
    Raises HTTP 401 if authentication fails
    """
    if not x_api_key:
        log_handler.warning("Request missing authentication header")
        raise HTTPException(
            status_code=401,
            detail={"error": "Authentication required"}
        )
    
    if x_api_key.strip() != AUTH_TOKEN:
        log_handler.warning(f"Invalid authentication attempt with key: {x_api_key}")
        raise HTTPException(
            status_code=401,
            detail={"error": "Invalid credentials"}
        )
    
    return True


def process_base64_audio(encoded_audio: str, file_extension: str) -> str:
    """
    Decodes base64 audio data and writes it to a temporary file
    Returns the filesystem path to the created file
    """
    try:
        # Convert base64 string to binary data
        binary_audio = base64.b64decode(encoded_audio)
        
        # Create a temporary file with the correct extension
        temp_audio_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f".{file_extension}",
            prefix="voice_analysis_"
        )
        
        # Write binary data to file
        temp_audio_file.write(binary_audio)
        temp_audio_file.close()
        
        log_handler.info(f"Created temporary audio file: {temp_audio_file.name}")
        return temp_audio_file.name
        
    except Exception as decode_error:
        log_handler.error(f"Failed to decode audio data: {str(decode_error)}")
        raise HTTPException(
            status_code=400,
            detail={"error": f"Audio decoding failed: {str(decode_error)}"}
        )


def analyze_voice_sample(file_path: str, lang_code: str, file_ext: str) -> dict:
    """
    Performs voice authenticity analysis on the audio file
    
    Production Implementation Note:
    In a real-world scenario, this function would:
    - Load a pre-trained deep learning model (CNN/RNN/Transformer)
    - Extract acoustic features (MFCCs, spectrograms, mel-frequency cepstral coefficients)
    - Run model inference to classify the audio
    - Return probabilistic predictions
    
    Current Implementation:
    For demonstration purposes, generates deterministic pseudo-random predictions
    """
    
    # Verify file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=400,
            detail={"error": "Audio file not accessible"}
        )
    
    # Check file has content
    file_bytes = os.path.getsize(file_path)
    if file_bytes == 0:
        raise HTTPException(
            status_code=400,
            detail={"error": "Audio file contains no data"}
        )
    
    log_handler.info(f"Analyzing audio: {file_path} (Size: {file_bytes} bytes)")
    
    # Simulation: Use file size as seed for reproducible results
    random.seed(file_bytes)
    
    # Classification options
    voice_types = ["AI", "Human"]
    detected_type = random.choice(voice_types)
    
    # Generate confidence score based on classification
    if detected_type == "AI":
        confidence_score = round(random.uniform(0.78, 0.96), 2)
    else:
        confidence_score = round(random.uniform(0.72, 0.92), 2)
    
    log_handler.info(f"Analysis complete: {detected_type} (Confidence: {confidence_score})")
    
    return {
        "prediction": detected_type,
        "confidence": confidence_score,
        "language": lang_code,
        "audio_format": file_ext,
        "status": "success"
    }


@service.get("/")
async def health_check():
    """
    Service health check endpoint
    Returns basic service information and status
    """
    return {
        "message": "Voice Authenticity Detection Service is operational",
        "version": "1.0.0",
        "available_endpoints": {
            "analysis": "/predict (POST)"
        },
        "service_status": "healthy"
    }


@service.post("/predict", response_model=AnalysisResult)
async def perform_analysis(
    analysis_request: VoiceAnalysisRequest,
    x_api_key: Optional[str] = Header(None)
):
    """
    Primary endpoint for voice authenticity analysis
    
    Authentication:
        x-api-key: Required header for API authentication
    
    Request Body:
        language: Language identifier (e.g., 'en' for English)
        audio_format or audioFormat: Audio file type (mp3, wav, etc.)
        audio_base64 or audioBase64: Base64-encoded audio data
    
    Response:
        JSON object containing prediction, confidence score, and metadata
    """
    
    # Authenticate the request
    authenticate_request(x_api_key)
    
    temp_file_path = None
    try:
        # Process and save the audio data
        temp_file_path = process_base64_audio(
            analysis_request.audio_base64,
            analysis_request.audio_format
        )
        
        # Perform voice analysis
        analysis_results = analyze_voice_sample(
            temp_file_path,
            analysis_request.language,
            analysis_request.audio_format
        )
        
        return JSONResponse(content=analysis_results)
        
    except HTTPException:
        # Pass through HTTP exceptions
        raise
        
    except Exception as unexpected_error:
        # Handle unexpected errors
        log_handler.error(f"Unexpected error in analysis: {str(unexpected_error)}")
        raise HTTPException(
            status_code=500,
            detail={"error": f"Service error: {str(unexpected_error)}"}
        )
        
    finally:
        # Clean up temporary file
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.unlink(temp_file_path)
                log_handler.info(f"Removed temporary file: {temp_file_path}")
            except Exception as cleanup_error:
                log_handler.warning(f"Failed to remove temp file: {str(cleanup_error)}")


@service.exception_handler(HTTPException)
async def handle_http_errors(request: Request, exception: HTTPException):
    """
    Ensures all HTTP exceptions return JSON responses
    """
    return JSONResponse(
        status_code=exception.status_code,
        content=exception.detail if isinstance(exception.detail, dict) else {"error": str(exception.detail)}
    )


@service.exception_handler(Exception)
async def handle_unexpected_errors(request: Request, exception: Exception):
    """
    Catches all unhandled exceptions and returns a generic error response
    """
    log_handler.error(f"Unhandled exception occurred: {str(exception)}")
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred"}
    )


if __name__ == "__main__":
    import uvicorn
    
    server_port = int(os.environ.get("PORT", 8000))
    
    uvicorn.run(
        "app:service",
        host="0.0.0.0",
        port=server_port,
        reload=False,
        log_level="info"
    )
