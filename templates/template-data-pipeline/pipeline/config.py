"""Configuration handling for the pipeline."""

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class ExtractConfig(BaseModel):
    """Configuration for data extraction."""

    source: str = Field(..., description="Path to source data")
    format: str = Field(default="csv", description="Data format (csv, json)")


class TransformStep(BaseModel):
    """Configuration for a transform step."""

    name: str = Field(..., description="Transform name")
    enabled: bool = Field(default=True, description="Whether step is enabled")
    columns: list[str] = Field(default_factory=list, description="Columns to process")


class TransformConfig(BaseModel):
    """Configuration for data transformation."""

    steps: list[TransformStep] = Field(
        default_factory=list, description="Transform steps"
    )


class LoadConfig(BaseModel):
    """Configuration for data loading."""

    destination: str = Field(..., description="Path to output")
    format: str = Field(default="csv", description="Output format (csv, json)")


class PipelineConfig(BaseModel):
    """Main pipeline configuration."""

    name: str = Field(default="pipeline", description="Pipeline name")
    description: str = Field(default="", description="Pipeline description")
    extract: ExtractConfig
    transform: TransformConfig = Field(default_factory=TransformConfig)
    load: LoadConfig

    @classmethod
    def from_yaml(cls, path: Path) -> "PipelineConfig":
        """Load configuration from YAML file.

        Args:
            path: Path to YAML configuration file.

        Returns:
            PipelineConfig instance.
        """
        with open(path) as f:
            data = yaml.safe_load(f)

        # Flatten pipeline section if present
        if "pipeline" in data:
            pipeline_data = data.pop("pipeline")
            data.update(pipeline_data)

        return cls(**data)
