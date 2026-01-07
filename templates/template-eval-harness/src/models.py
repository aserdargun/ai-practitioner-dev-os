"""Pydantic models for evaluation harness."""

from typing import Any

from pydantic import BaseModel, Field


class MetricResult(BaseModel):
    """Result of a single metric evaluation."""

    name: str = Field(..., description="Metric name")
    value: float = Field(..., description="Metric value")
    passed: bool = Field(default=True, description="Whether metric passed threshold")
    threshold: float | None = Field(default=None, description="Threshold used")
    details: dict[str, Any] = Field(default_factory=dict, description="Additional details")


class EvaluationConfig(BaseModel):
    """Configuration for evaluation run."""

    metrics: list[str] = Field(default_factory=list, description="Metrics to compute")
    thresholds: dict[str, float] = Field(default_factory=dict, description="Metric thresholds")
    output_format: str = Field(default="json", description="Output format")
    fail_on_threshold: bool = Field(default=True, description="Fail if below threshold")


class EvaluationResult(BaseModel):
    """Result of evaluation run."""

    success: bool = Field(..., description="Whether evaluation completed")
    metrics: list[MetricResult] = Field(default_factory=list, description="Metric results")
    overall_passed: bool = Field(default=True, description="Whether all thresholds passed")
    samples_evaluated: int = Field(default=0, description="Number of samples")
    errors: list[str] = Field(default_factory=list, description="Errors encountered")

    def summary(self) -> str:
        """Generate summary string."""
        lines = [
            "Evaluation Results",
            "=" * 40,
            f"Samples: {self.samples_evaluated}",
            f"Status: {'PASSED' if self.overall_passed else 'FAILED'}",
            "",
            "Metrics:",
        ]
        for metric in self.metrics:
            status = "✓" if metric.passed else "✗"
            lines.append(f"  {status} {metric.name}: {metric.value:.4f}")

        return "\n".join(lines)


class EvaluationData(BaseModel):
    """Container for evaluation data."""

    predictions: list[Any] = Field(..., description="Model predictions")
    ground_truth: list[Any] = Field(..., description="Ground truth labels")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
