# Model Evaluation – VoxGuard AI

The trained model was evaluated using unseen validation data.

## 1. Evaluation Metrics

Primary metrics used:
- Accuracy
- Validation Loss
- Confidence Score

Final Results:
- Training Accuracy: ~99%
- Validation Accuracy: ~98.5%

## 2. Confidence Score Calculation

Instead of returning raw probabilities, a confidence score was computed:

confidence = |prediction - 0.5| × 2

This ensures:
- Scores range between 0 and 1
- Higher confidence reflects stronger classification certainty

## 3. Observations

Human Voice:
- Natural frequency variations
- Irregular harmonic structures

AI Voice:
- Repetitive spectral patterns
- Over-smoothed frequency bands

## 4. Limitations

- Performance may degrade on extremely short or noisy audio
- Heavily compressed audio may affect prediction
- Real-time streaming is not yet supported

## 5. Deployment Validation

The deployed API was tested using:
- Swagger UI
- Docker container
- Cloud deployment (Hugging Face Docker Space)

All tests confirmed consistent inference behavior.

