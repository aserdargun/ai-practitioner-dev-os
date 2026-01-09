# Mini Example: Sentiment Analysis Service

This is a complete, minimal example of an ML service. It demonstrates what a "done" project looks like for Month 03-04 level work.

## What This Demonstrates

- End-to-end ML workflow
- Model training and evaluation
- API serving with FastAPI
- Proper testing structure
- Clean project organization

## Quick Start

```bash
# Install dependencies
pip install -e .

# Train the model (uses sample data)
python src/train.py

# Run the service
python src/serve.py

# Test the API
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This product is amazing!"}'

# Run tests
pytest tests/ -v
```

## Project Structure

```
mini-example/
├── src/
│   ├── README.md        # Source code overview
│   ├── model.py         # Model definition
│   ├── train.py         # Training script
│   └── serve.py         # FastAPI service
├── tests/
│   ├── README.md        # Testing overview
│   ├── test_model.py    # Model unit tests
│   └── test_api.py      # API integration tests
├── data/                # Sample data (created by train.py)
├── models/              # Trained models (created by train.py)
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## The ML Task

**Sentiment Analysis**: Classify text as positive or negative sentiment.

This example uses a simple rule-based classifier for demonstration. In a real project, you would use:
- scikit-learn classifiers (LogisticRegression, SVM)
- Transformers (BERT, DistilBERT)
- Or cloud APIs (OpenAI, Anthropic)

## Demo Guide

### 1. Train the Model

```bash
python src/train.py
```

Output:
```
Loading sample data...
Training model...
Accuracy: 0.85
Model saved to models/sentiment_model.json
```

### 2. Start the Service

```bash
python src/serve.py
```

Output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 3. Make Predictions

```bash
# Positive example
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'

# Response: {"sentiment": "positive", "confidence": 0.9}

# Negative example
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is terrible"}'

# Response: {"sentiment": "negative", "confidence": 0.85}
```

### 4. Run Tests

```bash
pytest tests/ -v
```

## What Makes This "Done"

1. **Working Code**: All scripts run without errors
2. **Tests Pass**: Unit and integration tests
3. **Documentation**: Clear README with usage instructions
4. **Clean Structure**: Organized, maintainable code
5. **Demo Ready**: Easy to show to others

## Extending This Example

To turn this into a real project:

1. **Better Model**: Replace rule-based with ML model
   ```python
   from sklearn.linear_model import LogisticRegression
   from sklearn.feature_extraction.text import TfidfVectorizer
   ```

2. **Real Data**: Use a sentiment dataset
   ```python
   from datasets import load_dataset
   dataset = load_dataset("imdb")
   ```

3. **Model Registry**: Track with MLflow
   ```python
   import mlflow
   mlflow.log_model(model, "sentiment_model")
   ```

4. **Containerize**: Add Docker support
   ```dockerfile
   FROM python:3.11-slim
   COPY . /app
   CMD ["python", "src/serve.py"]
   ```

## Learning Checklist

After completing this example, you should understand:

- [ ] How to structure an ML project
- [ ] Basic model training workflow
- [ ] Serving models via REST API
- [ ] Writing tests for ML code
- [ ] Documentation best practices
