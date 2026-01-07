"""Pydantic models for request/response validation."""

from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    """Single prediction input."""

    features: list[float] = Field(
        ...,
        description="Feature values for prediction",
        min_length=1,
    )


class PredictionOutput(BaseModel):
    """Single prediction output."""

    prediction: float
    confidence: float | None = None


class BatchPredictionInput(BaseModel):
    """Batch prediction input."""

    instances: list[PredictionInput] = Field(
        ...,
        description="List of prediction inputs",
        min_length=1,
    )


class BatchPredictionOutput(BaseModel):
    """Batch prediction output."""

    predictions: list[PredictionOutput]


class ModelInfo(BaseModel):
    """Model metadata."""

    name: str
    version: str
    description: str
    features_count: int
