# Data Collection Strategy – VoxGuard AI

This project focuses on detecting whether a given voice sample is Human-generated or AI-generated.  
A diverse and balanced dataset was required to ensure robustness across languages, accents, and speaking styles.

## 1. Data Sources

The dataset was collected from multiple publicly available and open-source repositories:

### Human Voice Data
- Public speech datasets
- Audiobook voice samples
- Podcast and interview voice clips
- Multi-language voice corpora

Languages covered:
- English
- Hindi
- Tamil
- Telugu
- Malayalam

### AI-Generated Voice Data
- Synthetic speech generated using modern TTS models
- AI voice samples from open repositories
- Cloned voice samples generated using neural TTS systems

## 2. Dataset Composition

- Total samples: ~4,300 audio clips
- Human voice samples: ~50%
- AI-generated voice samples: ~50%
- Clip duration: 3 seconds each
- Audio formats: WAV, MP3

The dataset was balanced to prevent model bias toward either class.

## 3. Data Preparation

- Long audio files (5–10 minutes) were split into 3-second clips
- Silent and corrupted clips were removed
- All clips were normalized before preprocessing

## 4. Why Raw Data Is Not Included

Raw audio files are not included in the repository due to:
- Large dataset size
- Licensing constraints
- Privacy considerations

However, the entire data processing and training pipeline is fully documented.
