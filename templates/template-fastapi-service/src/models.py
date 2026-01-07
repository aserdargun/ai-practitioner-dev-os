"""Pydantic models for request/response validation."""

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """Request model for predictions."""

    features: list[float] = Field(
        ...,
        min_length=1,
        description="List of feature values for prediction",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"features": [1.0, 2.0, 3.0, 4.0]},
            ]
        }
    }


class PredictionResponse(BaseModel):
    """Response model for predictions."""

    prediction: float = Field(..., description="Model prediction value")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Prediction confidence")
    model_version: str = Field(..., description="Version of the model used")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prediction": 2.5,
                    "confidence": 0.95,
                    "model_version": "0.1.0",
                }
            ]
        }
    }


class HealthResponse(BaseModel):
    """Response model for health checks."""

    status: str = Field(..., description="Health status")


class ReadinessResponse(BaseModel):
    """Response model for readiness checks."""

    status: str = Field(..., description="Readiness status")
    checks: dict[str, bool] = Field(default_factory=dict, description="Individual check results")
