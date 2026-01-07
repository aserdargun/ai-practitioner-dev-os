"""Evaluation metrics implementation."""

from typing import Any, Callable

import numpy as np

# Registry for custom metrics
_METRICS_REGISTRY: dict[str, Callable] = {}


def register_metric(name: str):
    """Decorator to register a custom metric.

    Args:
        name: Name of the metric

    Returns:
        Decorator function
    """

    def decorator(func: Callable) -> Callable:
        _METRICS_REGISTRY[name] = func
        return func

    return decorator


def get_metric(name: str) -> Callable:
    """Get a metric function by name.

    Args:
        name: Name of the metric

    Returns:
        Metric function

    Raises:
        ValueError: If metric not found
    """
    if name not in _METRICS_REGISTRY:
        raise ValueError(f"Unknown metric: {name}. Available: {list(_METRICS_REGISTRY.keys())}")
    return _METRICS_REGISTRY[name]


def list_metrics() -> list[str]:
    """List all registered metrics."""
    return list(_METRICS_REGISTRY.keys())


# Built-in metrics


@register_metric("accuracy")
def accuracy(predictions: list[Any], ground_truth: list[Any]) -> float:
    """Calculate accuracy.

    Args:
        predictions: Predicted values
        ground_truth: True values

    Returns:
        Accuracy score
    """
    if len(predictions) != len(ground_truth):
        raise ValueError("Predictions and ground truth must have same length")
    if len(predictions) == 0:
        return 0.0

    correct = sum(p == g for p, g in zip(predictions, ground_truth))
    return correct / len(predictions)


@register_metric("precision")
def precision(predictions: list[Any], ground_truth: list[Any], positive_label: Any = 1) -> float:
    """Calculate precision for binary classification.

    Args:
        predictions: Predicted values
        ground_truth: True values
        positive_label: Label for positive class

    Returns:
        Precision score
    """
    true_positives = sum(
        p == positive_label and g == positive_label for p, g in zip(predictions, ground_truth)
    )
    predicted_positives = sum(p == positive_label for p in predictions)

    if predicted_positives == 0:
        return 0.0

    return true_positives / predicted_positives


@register_metric("recall")
def recall(predictions: list[Any], ground_truth: list[Any], positive_label: Any = 1) -> float:
    """Calculate recall for binary classification.

    Args:
        predictions: Predicted values
        ground_truth: True values
        positive_label: Label for positive class

    Returns:
        Recall score
    """
    true_positives = sum(
        p == positive_label and g == positive_label for p, g in zip(predictions, ground_truth)
    )
    actual_positives = sum(g == positive_label for g in ground_truth)

    if actual_positives == 0:
        return 0.0

    return true_positives / actual_positives


@register_metric("f1")
def f1_score(predictions: list[Any], ground_truth: list[Any], positive_label: Any = 1) -> float:
    """Calculate F1 score for binary classification.

    Args:
        predictions: Predicted values
        ground_truth: True values
        positive_label: Label for positive class

    Returns:
        F1 score
    """
    p = precision(predictions, ground_truth, positive_label)
    r = recall(predictions, ground_truth, positive_label)

    if p + r == 0:
        return 0.0

    return 2 * (p * r) / (p + r)


@register_metric("mse")
def mean_squared_error(predictions: list[float], ground_truth: list[float]) -> float:
    """Calculate mean squared error.

    Args:
        predictions: Predicted values
        ground_truth: True values

    Returns:
        MSE value
    """
    predictions = np.array(predictions)
    ground_truth = np.array(ground_truth)
    return float(np.mean((predictions - ground_truth) ** 2))


@register_metric("mae")
def mean_absolute_error(predictions: list[float], ground_truth: list[float]) -> float:
    """Calculate mean absolute error.

    Args:
        predictions: Predicted values
        ground_truth: True values

    Returns:
        MAE value
    """
    predictions = np.array(predictions)
    ground_truth = np.array(ground_truth)
    return float(np.mean(np.abs(predictions - ground_truth)))
