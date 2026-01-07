"""Configuration for evaluation harness."""

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class DatasetConfig(BaseModel):
    """Configuration for a dataset."""

    name: str
    path: str
    target_column: str = "target"


class EvalConfig(BaseModel):
    """Main evaluation configuration."""

    name: str = Field(default="evaluation", description="Evaluation name")
    metrics: list[str] = Field(
        default_factory=lambda: ["accuracy", "f1_score"],
        description="Metrics to compute",
    )
    datasets: list[DatasetConfig] = Field(
        default_factory=list,
        description="Datasets to evaluate on",
    )
    output_format: str = Field(default="json", description="Output format")
    output_path: str = Field(default="./reports", description="Output directory")

    @classmethod
    def from_yaml(cls, path: Path) -> "EvalConfig":
        """Load configuration from YAML file.

        Args:
            path: Path to YAML file.

        Returns:
            EvalConfig instance.
        """
        with open(path) as f:
            data = yaml.safe_load(f)

        # Handle nested evaluation key
        if "evaluation" in data:
            eval_data = data.pop("evaluation")
            data.update(eval_data)

        # Handle output section
        if "output" in data:
            output_data = data.pop("output")
            data["output_format"] = output_data.get("format", "json")
            data["output_path"] = output_data.get("path", "./reports")

        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return self.model_dump()
