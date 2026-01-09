"""
Data Loading Module

Utilities for loading and preparing the Iris dataset.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_iris_data() -> tuple[np.ndarray, np.ndarray, list[str], list[str]]:
    """
    Load the Iris dataset.

    Returns:
        Tuple of (X, y, feature_names, target_names)
        - X: Feature matrix (150, 4)
        - y: Target vector (150,)
        - feature_names: List of feature names
        - target_names: List of class names
    """
    iris = load_iris()

    return (
        iris.data,
        iris.target,
        list(iris.feature_names),
        list(iris.target_names),
    )


def split_data(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split data into training and test sets.

    Args:
        X: Feature matrix
        y: Target vector
        test_size: Proportion of data for testing (0-1)
        random_state: Random seed for reproducibility

    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )


def get_feature_stats(X: np.ndarray, feature_names: list[str]) -> dict:
    """
    Calculate basic statistics for features.

    Args:
        X: Feature matrix
        feature_names: Names of features

    Returns:
        Dict with statistics per feature
    """
    stats = {}

    for i, name in enumerate(feature_names):
        stats[name] = {
            "min": float(X[:, i].min()),
            "max": float(X[:, i].max()),
            "mean": float(X[:, i].mean()),
            "std": float(X[:, i].std()),
        }

    return stats


if __name__ == "__main__":
    # Quick demo
    X, y, features, targets = load_iris_data()

    print("Iris Dataset Summary")
    print("=" * 40)
    print(f"Samples: {len(X)}")
    print(f"Features: {len(features)}")
    print(f"Classes: {len(targets)}")
    print()
    print("Features:", features)
    print("Classes:", targets)
    print()
    print("Feature Statistics:")
    stats = get_feature_stats(X, features)
    for name, s in stats.items():
        print(f"  {name}: min={s['min']:.2f}, max={s['max']:.2f}, mean={s['mean']:.2f}")
