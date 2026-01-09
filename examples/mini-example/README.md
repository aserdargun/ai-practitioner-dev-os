# Mini Example: Sentiment Classifier

A complete example showing what "done" looks like for a mini ML project.

This example demonstrates:
- Data loading and preprocessing
- Model training with scikit-learn
- Evaluation with metrics
- Simple prediction API
- Tests that pass

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Run the model
python src/model.py

# Run predictions
python src/predict.py "This product is amazing!"

# Run tests
pytest

# Run all quality checks
ruff check src/ tests/
pytest --cov=src
```

## Project Structure

```
mini-example/
├── data/
│   └── sample_reviews.json   # Sample dataset
├── src/
│   ├── README.md             # Source code docs
│   ├── model.py              # Model training
│   └── predict.py            # Prediction script
├── tests/
│   ├── README.md             # Test docs
│   └── test_model.py         # Model tests
├── pyproject.toml            # Dependencies
└── README.md                 # This file
```

## What This Example Teaches

### Month 2-3 Skills
- Loading and exploring data
- Basic text preprocessing
- Training a classifier
- Evaluating with metrics

### Month 4-5 Skills
- Structuring ML code
- Writing tests for ML
- Creating a prediction interface

## The Dataset

Sample sentiment data with positive/negative reviews:

```json
[
  {"text": "Great product, highly recommend!", "label": "positive"},
  {"text": "Terrible experience, avoid.", "label": "negative"}
]
```

## Model Details

- **Algorithm**: Logistic Regression with TF-IDF features
- **Features**: TF-IDF vectorization (max 1000 features)
- **Metrics**: Accuracy, Precision, Recall, F1

## Demo Guide

### Training
```bash
$ python src/model.py
Loading data...
Training model...
Evaluation Results:
  Accuracy:  0.85
  Precision: 0.84
  Recall:    0.86
  F1 Score:  0.85
Model saved to: model.pkl
```

### Prediction
```bash
$ python src/predict.py "This is wonderful!"
Prediction: positive (confidence: 0.92)

$ python src/predict.py "Worst purchase ever."
Prediction: negative (confidence: 0.89)
```

## Definition of Done

This example meets the "done" criteria:

- [x] Data is loaded and preprocessed
- [x] Model trains successfully
- [x] Evaluation metrics are computed
- [x] Predictions work correctly
- [x] Tests pass
- [x] Code is linted
- [x] README explains usage

## Extending This Example

Ideas for practice:
1. Add more training data
2. Try different models (SVM, Random Forest)
3. Add cross-validation
4. Create a FastAPI endpoint
5. Add model versioning
