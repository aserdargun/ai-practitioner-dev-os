"""Regression metrics."""

from typing import Any

import numpy as np
from sklearn import metrics as sklearn_metrics

from eval_harness.metrics.base import BaseMetric


class MSE(BaseMetric):
    """Mean Squared Error."""

    name = "mse"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        return {"mse": float(sklearn_metrics.mean_squared_error(y_true, y_pred))}


class RMSE(BaseMetric):
    """Root Mean Squared Error."""

    name = "rmse"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        mse = sklearn_metrics.mean_squared_error(y_true, y_pred)
        return {"rmse": float(np.sqrt(mse))}


class MAE(BaseMetric):
    """Mean Absolute Error."""

    name = "mae"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        return {"mae": float(sklearn_metrics.mean_absolute_error(y_true, y_pred))}


class R2Score(BaseMetric):
    """R-squared (coefficient of determination)."""

    name = "r2"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        return {"r2": float(sklearn_metrics.r2_score(y_true, y_pred))}


class MAPE(BaseMetric):
    """Mean Absolute Percentage Error."""

    name = "mape"

    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        # Avoid division by zero
        mask = y_true != 0
        if not mask.any():
            return {"mape": None, "error": "All true values are zero"}

        mape = np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100
        return {"mape": float(mape)}
