FROM python:3.10-slim

WORKDIR /app

# Install system deps (needed for librosa)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache optimization)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose port
EXPOSE 7860

# Start server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
