# Model Training Pipeline – VoxGuard AI

A Convolutional Neural Network (CNN) was used to classify Mel Spectrograms into Human or AI-generated speech.

## 1. Dataset Preparation

- Features saved as NumPy arrays
- Labels:
  - 0 → Human
  - 1 → AI-generated
- Dataset split:
  - Training: 80%
  - Validation: 20%

## 2. Model Architecture

The CNN architecture consists of:

- Conv2D (32 filters) + ReLU
- MaxPooling
- Conv2D (64 filters) + ReLU
- MaxPooling
- Conv2D (128 filters) + ReLU
- MaxPooling
- Flatten
- Dense (128 neurons)
- Dropout (0.3)
- Output Dense layer (Sigmoid)

This architecture captures both local and global frequency patterns.

## 3. Training Configuration

- Loss Function: Binary Crossentropy
- Optimizer: Adam
- Learning Rate: 0.0003
- Batch Size: 32
- Epochs: 15

## 4. Training Process

- Model trained on CPU
- Validation accuracy monitored every epoch
- Overfitting controlled using Dropout

## 5. Model Export

After training, the model was saved in Keras format:

