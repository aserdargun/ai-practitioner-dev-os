# Source Code

This directory contains the main source code for the sentiment classifier.

## Files

| File | Purpose |
|------|---------|
| `model.py` | Model training and evaluation |
| `predict.py` | Prediction interface |

## model.py

Handles:
- Data loading from JSON
- TF-IDF vectorization
- Logistic Regression training
- Model evaluation
- Model persistence

Key functions:
- `load_data()`: Load training data
- `train_model()`: Train the classifier
- `evaluate_model()`: Compute metrics
- `save_model()`: Save to pickle

## predict.py

Provides:
- Model loading
- Single text prediction
- Confidence scores
- CLI interface

Usage:
```bash
python predict.py "Your text here"
```

## Code Style

- Type hints on all functions
- Docstrings with examples
- Logging for debugging
- Error handling for edge cases
