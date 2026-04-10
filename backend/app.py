import base64
import io
import os
import tempfile
import numpy as np
import librosa
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware


# CONFIG

API_KEY = os.getenv("API_KEY")   # change later if needed

if not API_KEY:
    raise Exception("API_KEY not found")

MODEL_PATH = "voice_detector_model.keras"

SAMPLE_RATE = 22050
N_MELS = 128
MAX_LEN = 300


# LOAD MODEL

model = load_model(MODEL_PATH)

app = FastAPI(title="AI Voice Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend to access API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# REQUEST SCHEMA

class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str


# AUDIO PREPROCESSING

def audio_to_mel_from_bytes(audio_bytes, file_ext):
    # Save temp file with correct extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        # Load audio (librosa + ffmpeg handles multiple formats)
        y, sr = librosa.load(tmp_path, sr=SAMPLE_RATE, duration=3.0)
    except Exception as e:
        os.remove(tmp_path)
        raise HTTPException(status_code=400, detail=f"Unsupported or corrupted audio format: {file_ext}")

    os.remove(tmp_path)

    # Generate Mel Spectrogram
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=N_MELS)
    mel_db = librosa.power_to_db(mel, ref=np.max)

    # Pad / truncate
    if mel_db.shape[1] < MAX_LEN:
        pad_width = MAX_LEN - mel_db.shape[1]
        mel_db = np.pad(mel_db, ((0, 0), (0, pad_width)), mode='constant')
    else:
        mel_db = mel_db[:, :MAX_LEN]

    mel_db = mel_db[np.newaxis, ..., np.newaxis]
    return mel_db

# API ENDPOINT

from fastapi.responses import FileResponse

@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

@app.post("/api/voice-detection")
def detect_voice(
    request: VoiceRequest,
    x_api_key: str = Header(...)
):
    # API key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    SUPPORTED_FORMATS = ["mp3", "wav", "m4a", "ogg", "flac"]
    
    if request.audioFormat.lower() not in SUPPORTED_FORMATS:
        raise HTTPException(status_code=400, detail="Unsupported audio format")

    try:
        audio_bytes = base64.b64decode(request.audioBase64)
    except:
        raise HTTPException(status_code=400, detail="Invalid Base64 audio")

    # Preprocess
    file_ext = request.audioFormat.lower()
    mel_input = audio_to_mel_from_bytes(audio_bytes, file_ext)

    # Predict
    prediction = model.predict(mel_input)[0][0]

    confidence = float(abs(prediction - 0.5) * 2)

    if confidence >= 0.5:
        classification = "AI_GENERATED"
        explanation = "Unnatural spectral patterns detected"
    else:
        classification = "HUMAN"
        confidence = 1 - confidence
        explanation = "Natural voice frequency variations detected"

    # Response
    return {
        "status": "success",
        "language": request.language,
        "classification": classification,
        "confidenceScore": round(confidence, 3),
        "explanation": explanation
    }
