"""Evaluation metrics."""

from eval_harness.metrics.base import BaseMetric
from eval_harness.metrics.classification import (
    Accuracy,
    ClassificationReport,
    ConfusionMatrix,
    F1Score,
    Precision,
    Recall,
    RocAuc,
)
from eval_harness.metrics.regression import MAE, MAPE, MSE, RMSE, R2Score

# Registry of all available metrics
METRIC_REGISTRY = {
    # Classification
    "accuracy": Accuracy,
    "precision": Precision,
    "recall": Recall,
    "f1_score": F1Score,
    "confusion_matrix": ConfusionMatrix,
    "roc_auc": RocAuc,
    "classification_report": ClassificationReport,
    # Regression
    "mse": MSE,
    "rmse": RMSE,
    "mae": MAE,
    "r2": R2Score,
    "mape": MAPE,
}

__all__ = [
    "BaseMetric",
    "METRIC_REGISTRY",
    # Classification
    "Accuracy",
    "Precision",
    "Recall",
    "F1Score",
    "ConfusionMatrix",
    "RocAuc",
    "ClassificationReport",
    # Regression
    "MSE",
    "RMSE",
    "MAE",
    "R2Score",
    "MAPE",
]
