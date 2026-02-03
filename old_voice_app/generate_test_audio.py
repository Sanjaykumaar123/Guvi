"""
Generate a base64 encoded audio sample for testing the API
This creates a simple audio file and outputs the base64 string
"""

import base64
import wave
import struct
import math

def generate_base64_audio():
    """Generate a simple audio file and return its base64 encoding"""
    
    print("=" * 60)
    print("Generating Test Audio for API Testing")
    print("=" * 60)
    
    # Generate 1 second of 440Hz tone (A note)
    sample_rate = 44100
    duration = 1
    frequency = 440
    
    print("\n1. Generating audio samples...")
    samples = []
    for i in range(sample_rate * duration):
        value = int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate))
        samples.append(value)
    print(f"   ✅ Generated {len(samples)} samples")
    
    # Write to WAV file
    filename = "test_audio.wav"
    print(f"\n2. Writing to {filename}...")
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for sample in samples:
            wav_file.writeframes(struct.pack('h', sample))
    print(f"   ✅ Audio file created")
    
    # Read and encode to base64
    print(f"\n3. Encoding to base64...")
    with open(filename, "rb") as f:
        audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    
    print(f"   ✅ Encoded {len(audio_bytes)} bytes to base64")
    print(f"   ✅ Base64 length: {len(audio_base64)} characters")
    
    # Save to file for easy copying
    with open("audio_base64.txt", "w") as f:
        f.write(audio_base64)
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS!")
    print("=" * 60)
    print("\nBase64 audio has been saved to: audio_base64.txt")
    print("\nYou can also copy it from below:")
    print("-" * 60)
    print(audio_base64[:100] + "...")
    print("-" * 60)
    print(f"\nFull base64 string length: {len(audio_base64)} characters")
    print("\nTo use in GUVI tester:")
    print("1. Open audio_base64.txt")
    print("2. Copy the entire content")
    print("3. Paste into 'Audio Base64 Format' field")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    generate_base64_audio()
