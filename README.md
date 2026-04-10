---
title: Voxguard Ai
emoji: 👁
colorFrom: pink
colorTo: red
sdk: docker
pinned: false
license: mit
---
---

title: Voxguard Ai
emoji: 👁
colorFrom: pink
colorTo: red
sdk: docker
pinned: false
license: mit
------------

# VoxGuard AI 🎙️

AI vs Human Voice Detection API

VoxGuard AI is a deep learning powered REST API that classifies voice samples as either AI-generated or real human speech.
The system converts audio into Mel Spectrograms and uses a CNN model trained on synthetic and real voice datasets.

---

## ⚡ Quick Access

### 🌐 Live Demo (Hugging Face)

https://coderlakshman-voxguard-ai.hf.space

### 🐳 Run Locally with Docker (No setup required)

```bash
docker build -t voxguard-ai https://github.com/Lakshman2405/voxguard-ai.git#main:backend
docker run -p 7860:7860 -e API_KEY=demo123 voxguard-ai
```

---

## Features

* Detects AI-generated vs Human voice
* Accepts Base64 encoded audio files
* Supports MP3 audio input (optimized for short clips)
* Returns confidence score
* Multi-language friendly (English, Tamil, Hindi, Malayalam, Telugu)
* FastAPI backend
* Dockerized for easy deployment

---

## Web Interface

VoxGuard AI includes a simple frontend interface:

* Upload audio file
* Detect AI vs Human voice
* View confidence score

Access:

* Hugging Face → opens automatically
* Docker → http://localhost:7860/

---

## Tech Stack

* Python
* FastAPI
* TensorFlow / Keras
* Librosa
* Docker
* Hugging Face Spaces

---

## 📁 Project Structure

### 🔹 Hugging Face (Flat Structure)

Used for direct Docker deployment in Spaces:

```
voxguard-ai/
├── app.py
├── requirements.txt
├── Dockerfile
├── voice_detector_model.keras
├── index.html
└── README.md
```

---

### 🔹 GitHub Repository (Modular Structure)

Used for development and Docker build from subdirectory:

```
voxguard-ai/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── voice_detector_model.keras
│   └── index.html
├── frontend/ (optional future use)
└── README.md
```

---

### ⚠️ Important Note

* Hugging Face expects files at **root level**
* GitHub version keeps backend isolated inside `/backend`

👉 That’s why Docker build uses:

```bash
docker build -t voxguard-ai https://github.com/...#main:backend
```

---

## Model Details

* Input: 3-second audio clips
* Feature: Mel Spectrogram (128 x 300)
* Model: CNN-based classifier
* Output: Binary classification (AI vs Human) with confidence score

---

## Authentication

All API requests require an API key.

Pass it in headers:

```
x-api-key: YOUR_API_KEY
```

Example:

```
x-api-key: demo123
```

---

## API Usage

### Endpoint:

POST /api/voice-detection

### Request Body:

```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "BASE64_AUDIO_STRING"
}
```

### Response:

```json
{
  "status": "success",
  "language": "English",
  "classification": "HUMAN",
  "confidenceScore": 0.997,
  "explanation": "Natural spectral patterns detected"
}
```

(or)

```json
{
  "status": "success",
  "language": "English",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.997,
  "explanation": "Unnatural spectral patterns detected"
}
```

---

## Run Locally

### Install dependencies

```
pip install -r requirements.txt
```

### Set API key (Linux/Mac)

```
export API_KEY=your_api_key_here
```

### Set API Key (Windows PowerShell)

```
setx API_KEY "your_api_key_here"
```

### Start Server

```
uvicorn app:app --reload
```

### Open Swagger UI:

http://127.0.0.1:8000/docs

---

## Run with Docker

### Option 1: Build from GitHub (Recommended)

```
docker build -t voxguard-ai https://github.com/Lakshman2405/voxguard-ai.git#main:backend
docker run -p 7860:7860 -e API_KEY=your_api_key voxguard-ai
```

### Option 2: Build from local repo

```
docker build -t voxguard-ai .
docker run -p 7860:7860 -e API_KEY=your_api_key voxguard-ai
```

### Access

Frontend:
http://localhost:7860/

Swagger Docs:
http://localhost:7860/docs

---

## Deployment

VoxGuard AI is deployed using:

* Hugging Face Spaces (Docker SDK)

It can also be deployed on:

* Render
* Railway
* AWS
* GCP

---

## Use Case

This system helps in:

* Detecting deepfake voice content
* Enhancing user safety
* Fraud detection
* AI content verification

---

## Hackathon Validation (HCL)

The API endpoint successfully passes the India AI Impact Buildathon Endpoint Tester with real-time predictions.

---

## Author

Lakshman Guru Sai
India AI Impact Buildathon Participant

---

## References

* Mel Spectrogram Audio Processing
* CNN-based Audio Classification
* FastAPI REST Architecture

---

Check out the configuration reference at:
https://huggingface.co/docs/hub/spaces-config-reference
