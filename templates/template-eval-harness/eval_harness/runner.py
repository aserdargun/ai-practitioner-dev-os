"""Evaluation runner."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

import numpy as np

from eval_harness.metrics.base import BaseMetric


@dataclass
class EvaluationResults:
    """Container for evaluation results."""

    model_name: str
    timestamp: str
    metrics: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert results to dictionary."""
        return {
            "model_name": self.model_name,
            "timestamp": self.timestamp,
            "metrics": self.metrics,
            "metadata": self.metadata,
        }

    def summary(self) -> str:
        """Generate summary string."""
        lines = [
            f"Model: {self.model_name}",
            f"Timestamp: {self.timestamp}",
            "",
            "Metrics:",
        ]
        for name, value in self.metrics.items():
            if isinstance(value, float):
                lines.append(f"  {name}: {value:.4f}")
            else:
                lines.append(f"  {name}: {value}")
        return "\n".join(lines)


class EvaluationRunner:
    """Runner for model evaluation."""

    def __init__(self):
        """Initialize the runner."""
        self.metrics: list[BaseMetric] = []

    def add_metric(self, metric: BaseMetric) -> None:
        """Add a metric to the evaluation.

        Args:
            metric: Metric instance to add.
        """
        self.metrics.append(metric)

    def evaluate(
        self,
        model: Any,
        X: np.ndarray,
        y: np.ndarray,
        model_name: str = "model",
    ) -> EvaluationResults:
        """Run evaluation on a model.

        Args:
            model: Model with predict method.
            X: Feature array.
            y: Target array.
            model_name: Name for identification.

        Returns:
            EvaluationResults with all computed metrics.
        """
        # Make predictions
        y_pred = model.predict(X)

        # Get probabilities if available and needed
        y_proba = None
        if any(m.requires_proba for m in self.metrics):
            if hasattr(model, "predict_proba"):
                y_proba = model.predict_proba(X)

        # Compute all metrics
        all_metrics = {}
        for metric in self.metrics:
            try:
                result = metric.compute(y_true=y, y_pred=y_pred, y_proba=y_proba)
                all_metrics.update(result)
            except Exception as e:
                all_metrics[metric.name] = {"error": str(e)}

        # Build results
        return EvaluationResults(
            model_name=model_name,
            timestamp=datetime.now().isoformat(),
            metrics=all_metrics,
            metadata={
                "n_samples": len(y),
                "n_features": X.shape[1] if X.ndim > 1 else 1,
                "metrics_computed": [m.name for m in self.metrics],
            },
        )

    def compare(
        self,
        models: dict[str, Any],
        X: np.ndarray,
        y: np.ndarray,
    ) -> dict[str, EvaluationResults]:
        """Compare multiple models.

        Args:
            models: Dictionary of model_name -> model.
            X: Feature array.
            y: Target array.

        Returns:
            Dictionary of model_name -> EvaluationResults.
        """
        results = {}
        for name, model in models.items():
            results[name] = self.evaluate(model, X, y, model_name=name)
        return results
