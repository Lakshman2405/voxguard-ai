---
title: Voxguard Ai
emoji: 👁
colorFrom: pink
colorTo: red
sdk: docker
pinned: false
license: mit
---
# VoxGuard AI 🎙️

AI vs Human Voice Detection API

VoxGuard AI is a deep learning powered REST API that classifies voice samples as either AI-generated or real human speech.
The system converts audio into Mel Spectrograms and uses a CNN model trained on synthetic and real voice datasets.


🚀 Live Demo: https://coderlakshman-voxguard-ai.hf.space

## Features

- Detects AI-generated vs Human voice
- Accepts Base64 encoded audio files
- Supports MP3, WAV and common formats
- Detects AI Generated vs Human Voice
- Returns confidence score
- Multi-language friendly (English, Tamil, Hindi, Malayalam, Telugu)
- FastAPI backend
- Dockerized for easy deployment
  

## Tech Stack

- Python
- FastAPI
- TensorFlow / Keras
- Librosa
- Docker
- Hugging Face Spaces

## Project Structure

voxguard-ai/

- app.py
- requirements.txt
- Dockerfile
- voice_detector_model.keras
- README.md

## API Usage

### Endpoint:

POST /api/voice-detection

### Request Body:

{
"language": "English",
"audioFormat": "mp3",
"audioBase64": "BASE64_AUDIO_STRING"
}

### Response:

{
"status": "success",
"language": "English",
"classification": "HUMAN",
"confidenceScore": 0.997,
"explanation": "Natural spectral patterns detected"
}

(or)

{
"status": "success",
"language": "English",
"classification": "AI_GENERATED",
"confidenceScore": 0.997,
"explanation": "Unnatural spectral patterns detected"
}

## Run Locally

### Install dependencies

pip install -r requirements.txt

### Set API key(Linux/Mac)

export API_KEY=your_api_key_here

### Set API Key(Windows PowerShell)

setx API_KEY "your_api_key_here"

### Start Server

uvicorn app:app --reload

### Open Swagger UI:

http://127.0.0.1:8000/docs


## Run with Docker

docker build -t voxguard-ai .

docker run -p 7860:7860 voxguard-ai


## Deployment

VoxGuard AI is deployed using:
- Hugging Face Spaces (Docker SDK)

It can also be deployed on:
- Render
- Railway
- AWS
- GCP

## Use Case:

This system helps in:
- Detecting deepfake voice content
- Enhancing user safety
- Fraud detection
- AI content verification

## Hackathon Validation(HCL 

The API endpoint successfully passes the India AI Impact Buildathon Endpoint Tester with real-time predictions.

## Author

Lakshman Guru Sai
India AI Impact Buildathon Participant

## References

- Mel Spectrogram Audio Processing
- CNN-based Audio Classification
- FastAPI REST Architecture


Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
