# Source Code

This directory contains the main source code for the Iris classifier.

## Modules

### `data.py`

Data loading and preprocessing utilities.

```python
from src.data import load_iris_data

X, y, feature_names, target_names = load_iris_data()
```

### `train.py`

Model training and evaluation functions.

```python
from src.train import train_model, evaluate_model, save_model

model = train_model(X, y)
metrics = evaluate_model(model, X, y)
save_model(model, "models/iris_model.pkl")
```

### `predict.py`

Prediction utilities.

```python
from src.predict import load_model, predict, predict_proba

model = load_model("models/iris_model.pkl")
result = predict(model, [5.1, 3.5, 1.4, 0.2])
probas = predict_proba(model, [5.1, 3.5, 1.4, 0.2])
```

## Code Style

- All functions have docstrings
- Type hints are used throughout
- Maximum line length: 88 characters
- Formatted with ruff
