"""
Prediction Module

Functions for loading models and making predictions.
"""

import pickle
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Target class names
TARGET_NAMES = ["setosa", "versicolor", "virginica"]

# Default model path
DEFAULT_MODEL_PATH = Path("models/iris_model.pkl")


def load_model(path: str = None) -> RandomForestClassifier:
    """
    Load a trained model from disk.

    Args:
        path: Path to model file (default: models/iris_model.pkl)

    Returns:
        Loaded RandomForestClassifier

    Raises:
        FileNotFoundError: If model file doesn't exist
    """
    if path is None:
        path = DEFAULT_MODEL_PATH

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Model not found at {path}. Run train.py first.")

    with open(path, "rb") as f:
        model = pickle.load(f)

    return model


def predict(
    model: RandomForestClassifier,
    features: list[float],
) -> str:
    """
    Make a single prediction.

    Args:
        model: Trained model
        features: List of 4 feature values
                  [sepal_length, sepal_width, petal_length, petal_width]

    Returns:
        Predicted class name (e.g., "setosa")

    Raises:
        ValueError: If features is not length 4
    """
    if len(features) != 4:
        raise ValueError(f"Expected 4 features, got {len(features)}")

    X = np.array(features).reshape(1, -1)
    prediction = model.predict(X)[0]

    return TARGET_NAMES[prediction]


def predict_proba(
    model: RandomForestClassifier,
    features: list[float],
) -> dict[str, float]:
    """
    Make a prediction with probabilities.

    Args:
        model: Trained model
        features: List of 4 feature values

    Returns:
        Dict mapping class names to probabilities

    Raises:
        ValueError: If features is not length 4
    """
    if len(features) != 4:
        raise ValueError(f"Expected 4 features, got {len(features)}")

    X = np.array(features).reshape(1, -1)
    probabilities = model.predict_proba(X)[0]

    return {
        name: float(prob)
        for name, prob in zip(TARGET_NAMES, probabilities)
    }


def predict_batch(
    model: RandomForestClassifier,
    samples: list[list[float]],
) -> list[str]:
    """
    Make predictions for multiple samples.

    Args:
        model: Trained model
        samples: List of feature lists

    Returns:
        List of predicted class names
    """
    X = np.array(samples)
    predictions = model.predict(X)

    return [TARGET_NAMES[p] for p in predictions]


if __name__ == "__main__":
    # Demo predictions
    print("Loading model...")
    try:
        model = load_model()
    except FileNotFoundError:
        print("Model not found. Training first...")
        from src.train import main as train_main
        train_main()
        model = load_model()

    # Example predictions
    examples = [
        [5.1, 3.5, 1.4, 0.2],  # Typical setosa
        [6.0, 2.7, 5.1, 1.6],  # Typical versicolor
        [6.3, 3.3, 6.0, 2.5],  # Typical virginica
    ]

    print("\nExample Predictions:")
    print("-" * 60)

    for features in examples:
        prediction = predict(model, features)
        probas = predict_proba(model, features)

        print(f"Features: {features}")
        print(f"Prediction: {prediction}")
        print(f"Probabilities: ", end="")
        for name, prob in probas.items():
            print(f"{name}={prob:.2%} ", end="")
        print("\n")
