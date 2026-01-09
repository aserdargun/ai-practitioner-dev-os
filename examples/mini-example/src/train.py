"""
Model Training Module

Functions for training, evaluating, and saving models.
"""

import pickle
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from src.data import load_iris_data, split_data

# Default model parameters
DEFAULT_N_ESTIMATORS = 100
DEFAULT_RANDOM_STATE = 42
DEFAULT_MODEL_PATH = Path("models/iris_model.pkl")


def train_model(
    X: np.ndarray,
    y: np.ndarray,
    n_estimators: int = DEFAULT_N_ESTIMATORS,
    random_state: int = DEFAULT_RANDOM_STATE,
) -> RandomForestClassifier:
    """
    Train a Random Forest classifier.

    Args:
        X: Feature matrix
        y: Target vector
        n_estimators: Number of trees in the forest
        random_state: Random seed for reproducibility

    Returns:
        Trained RandomForestClassifier
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=-1,
    )

    model.fit(X, y)

    return model


def evaluate_model(
    model: RandomForestClassifier,
    X: np.ndarray,
    y: np.ndarray,
    target_names: list[str] = None,
) -> dict:
    """
    Evaluate model performance.

    Args:
        model: Trained model
        X: Feature matrix
        y: True labels
        target_names: Names of target classes

    Returns:
        Dict with evaluation metrics
    """
    y_pred = model.predict(X)

    metrics = {
        "accuracy": accuracy_score(y, y_pred),
        "confusion_matrix": confusion_matrix(y, y_pred).tolist(),
        "predictions": y_pred.tolist(),
    }

    if target_names:
        report = classification_report(y, y_pred, target_names=target_names, output_dict=True)
        metrics["classification_report"] = report

    return metrics


def save_model(model: RandomForestClassifier, path: str = None) -> Path:
    """
    Save trained model to disk.

    Args:
        model: Trained model
        path: Path to save model (default: models/iris_model.pkl)

    Returns:
        Path where model was saved
    """
    if path is None:
        path = DEFAULT_MODEL_PATH

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump(model, f)

    return path


def get_feature_importance(
    model: RandomForestClassifier,
    feature_names: list[str],
) -> dict[str, float]:
    """
    Get feature importance from trained model.

    Args:
        model: Trained Random Forest model
        feature_names: Names of features

    Returns:
        Dict mapping feature names to importance scores
    """
    importances = model.feature_importances_

    return {
        name: float(importance)
        for name, importance in zip(feature_names, importances)
    }


def main():
    """Train and save the model."""
    print("Loading data...")
    X, y, feature_names, target_names = load_iris_data()

    print("Splitting data...")
    X_train, X_test, y_train, y_test = split_data(X, y)

    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")

    print("\nTraining model...")
    model = train_model(X_train, y_train)

    print("\nEvaluating on training set...")
    train_metrics = evaluate_model(model, X_train, y_train, target_names)
    print(f"Training Accuracy: {train_metrics['accuracy']:.2%}")

    print("\nEvaluating on test set...")
    test_metrics = evaluate_model(model, X_test, y_test, target_names)
    print(f"Test Accuracy: {test_metrics['accuracy']:.2%}")

    print("\nConfusion Matrix:")
    for row in test_metrics["confusion_matrix"]:
        print(f"  {row}")

    print("\nFeature Importance:")
    importance = get_feature_importance(model, feature_names)
    for name, imp in sorted(importance.items(), key=lambda x: -x[1]):
        print(f"  {name}: {imp:.3f}")

    print("\nSaving model...")
    path = save_model(model)
    print(f"Model saved to: {path}")

    print("\nDone!")


if __name__ == "__main__":
    main()
