"""Classification metrics."""

from typing import Any

import numpy as np
from sklearn import metrics as sklearn_metrics

from eval_harness.metrics.base import BaseMetric


class Accuracy(BaseMetric):
    """Accuracy score."""

    name = "accuracy"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        return {"accuracy": float(sklearn_metrics.accuracy_score(y_true, y_pred))}


class Precision(BaseMetric):
    """Precision score."""

    name = "precision"

    def __init__(self, average: str = "weighted"):
        self.average = average

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        score = sklearn_metrics.precision_score(
            y_true, y_pred, average=self.average, zero_division=0
        )
        return {f"precision_{self.average}": float(score)}


class Recall(BaseMetric):
    """Recall score."""

    name = "recall"

    def __init__(self, average: str = "weighted"):
        self.average = average

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        score = sklearn_metrics.recall_score(
            y_true, y_pred, average=self.average, zero_division=0
        )
        return {f"recall_{self.average}": float(score)}


class F1Score(BaseMetric):
    """F1 score."""

    name = "f1_score"

    def __init__(self, average: str = "weighted"):
        self.average = average

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        score = sklearn_metrics.f1_score(
            y_true, y_pred, average=self.average, zero_division=0
        )
        return {f"f1_{self.average}": float(score)}


class ConfusionMatrix(BaseMetric):
    """Confusion matrix."""

    name = "confusion_matrix"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        cm = sklearn_metrics.confusion_matrix(y_true, y_pred)
        return {"confusion_matrix": cm.tolist()}


class RocAuc(BaseMetric):
    """ROC AUC score."""

    name = "roc_auc"
    requires_proba = True

    def __init__(self, multi_class: str = "ovr"):
        self.multi_class = multi_class

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        if y_proba is None:
            return {"roc_auc": None, "error": "Requires probability predictions"}

        try:
            # Binary classification
            if y_proba.ndim == 1 or y_proba.shape[1] == 2:
                if y_proba.ndim == 2:
                    y_proba = y_proba[:, 1]
                score = sklearn_metrics.roc_auc_score(y_true, y_proba)
            else:
                # Multi-class
                score = sklearn_metrics.roc_auc_score(
                    y_true, y_proba, multi_class=self.multi_class
                )
            return {"roc_auc": float(score)}
        except ValueError as e:
            return {"roc_auc": None, "error": str(e)}


class ClassificationReport(BaseMetric):
    """Full classification report."""

    name = "classification_report"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        report = sklearn_metrics.classification_report(
            y_true, y_pred, output_dict=True, zero_division=0
        )
        return {"classification_report": report}
