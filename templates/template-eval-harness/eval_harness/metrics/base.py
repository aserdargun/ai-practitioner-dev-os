"""Base metric class."""

from abc import ABC, abstractmethod
from typing import Any

import numpy as np


class BaseMetric(ABC):
    """Base class for evaluation metrics."""

    name: str = "base_metric"
    requires_proba: bool = False

    @abstractmethod
    def compute(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None,
    ) -> dict[str, Any]:
        """Compute the metric.

        Args:
            y_true: Ground truth labels.
            y_pred: Predicted labels.
            y_proba: Prediction probabilities (optional).

        Returns:
            Dictionary with metric name(s) and value(s).
        """
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"
