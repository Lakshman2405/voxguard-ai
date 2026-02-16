# Audio Preprocessing Pipeline – VoxGuard AI

To make audio suitable for deep learning, raw audio signals were converted into time–frequency representations.

## 1. Audio Standardization

Each audio file was processed as follows:
- Converted to mono channel
- Resampled to 22,050 Hz
- Trimmed or padded to a fixed duration (3 seconds)

## 2. Feature Extraction

Mel Spectrograms were chosen as input features because they capture perceptually meaningful frequency information.

Steps:
1. Load audio using Librosa
2. Compute Mel Spectrogram
3. Convert power spectrogram to decibel (dB) scale
4. Normalize values

Parameters:
- Sample Rate: 22,050 Hz
- Number of Mel bands: 128
- Time frames: 300

## 3. Padding and Shape Normalization

- If spectrogram width < 300 → zero-padded
- If spectrogram width > 300 → truncated

Final input shape to the model:
(128, 300, 1)



## 4. Why Mel Spectrograms?

Mel Spectrograms help distinguish:
- Natural harmonic variations in human speech
- Repetitive and unnatural frequency patterns in AI-generated voices

This representation significantly improves classification performance.

















'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
