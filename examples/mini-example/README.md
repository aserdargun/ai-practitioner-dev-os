# Mini Example: Iris Classifier

A complete, working example showing what "done" looks like for a beginner ML project.

This example demonstrates a simple but production-quality machine learning project:
classifying Iris flowers using scikit-learn.

## What This Example Demonstrates

- Clean project structure
- Data loading and exploration
- Model training with evaluation
- Model persistence (save/load)
- Simple prediction API
- Comprehensive tests
- Documentation

## Quick Start

### 1. Install Dependencies

```bash
cd examples/mini-example
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
pytest
```

### 3. Train the Model

```bash
python -m src.train
```

### 4. Make Predictions

```python
from src.predict import load_model, predict

model = load_model()
prediction = predict(model, [5.1, 3.5, 1.4, 0.2])
print(prediction)  # "setosa"
```

## Project Structure

```
mini-example/
├── src/
│   ├── README.md        # Source code documentation
│   ├── train.py         # Model training script
│   ├── predict.py       # Prediction functions
│   └── data.py          # Data loading utilities
├── tests/
│   ├── README.md        # Test documentation
│   ├── test_train.py    # Training tests
│   └── test_predict.py  # Prediction tests
├── models/              # Saved models (gitignored)
├── pyproject.toml       # Dependencies
└── README.md            # This file
```

## The Dataset

We use the famous Iris dataset:
- **150 samples** of iris flowers
- **4 features**: sepal length, sepal width, petal length, petal width
- **3 classes**: setosa, versicolor, virginica

This is a classic dataset for learning ML classification.

## The Model

We use a **Random Forest Classifier**:
- Ensemble of decision trees
- Good default performance
- Handles non-linear relationships
- Easy to interpret

## Demo Walkthrough

### 1. Load and Explore Data

```python
from src.data import load_iris_data

X, y, feature_names, target_names = load_iris_data()

print(f"Features: {feature_names}")
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print(f"Classes: {target_names}")
# ['setosa', 'versicolor', 'virginica']

print(f"Samples: {len(X)}")
# 150
```

### 2. Train Model

```python
from src.train import train_model, evaluate_model

# Train
model = train_model(X, y)

# Evaluate
metrics = evaluate_model(model, X, y)
print(f"Accuracy: {metrics['accuracy']:.2%}")
# Accuracy: 97.33%
```

### 3. Save and Load Model

```python
from src.train import save_model
from src.predict import load_model

# Save
save_model(model, "models/iris_model.pkl")

# Load
loaded_model = load_model("models/iris_model.pkl")
```

### 4. Make Predictions

```python
from src.predict import predict, predict_proba

# Single prediction
sample = [5.1, 3.5, 1.4, 0.2]
result = predict(model, sample)
print(f"Prediction: {result}")  # "setosa"

# With probabilities
result = predict_proba(model, sample)
print(result)
# {"setosa": 0.95, "versicolor": 0.03, "virginica": 0.02}
```

## What Makes This "Done"

### Code Quality
- [x] Clean, readable code
- [x] Docstrings on all functions
- [x] Type hints
- [x] No code duplication

### Testing
- [x] Tests for all main functions
- [x] Tests pass consistently
- [x] Edge cases covered

### Documentation
- [x] README with quick start
- [x] Code comments where needed
- [x] Example usage

### Reproducibility
- [x] Fixed random seeds
- [x] Pinned dependencies
- [x] Model versioning

## Extending This Example

### Add Cross-Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(f"CV Accuracy: {scores.mean():.2%} (+/- {scores.std():.2%})")
```

### Try Different Models

```python
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

models = {
    "SVM": SVC(),
    "KNN": KNeighborsClassifier(),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name}: {score:.2%}")
```

### Add Feature Importance

```python
importance = model.feature_importances_
for name, imp in zip(feature_names, importance):
    print(f"{name}: {imp:.3f}")
```

## Common Questions

### Why Random Forest?

- Works well out of the box
- Doesn't require feature scaling
- Provides feature importance
- Handles overfitting naturally

### Why Not Deep Learning?

For small datasets like Iris (150 samples), traditional ML often works better.
Deep learning shines with large datasets and complex patterns.

### What's Next?

After mastering this example:
1. Try a larger dataset (e.g., from Kaggle)
2. Add more preprocessing steps
3. Experiment with hyperparameter tuning
4. Build a simple web interface

## Resources

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Iris Dataset Info](https://archive.ics.uci.edu/ml/datasets/iris)
- [Random Forest Guide](https://scikit-learn.org/stable/modules/ensemble.html#forest)
