"""FastAPI service for ML model predictions."""

import logging
import os
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="ML Prediction Service",
    description="A minimal FastAPI service for ML model predictions",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    """Request schema for predictions."""

    features: List[float] = Field(
        ...,
        description="List of feature values for prediction",
        min_length=1,
        examples=[[1.0, 2.0, 3.0]],
    )


class PredictionResponse(BaseModel):
    """Response schema for predictions."""

    prediction: float = Field(..., description="Model prediction value")
    confidence: float = Field(
        ..., description="Confidence score (0-1)", ge=0.0, le=1.0
    )


class HealthResponse(BaseModel):
    """Response schema for health check."""

    status: str = Field(..., description="Service health status")
    model_loaded: bool = Field(..., description="Whether model is loaded")


# Simulated model state (replace with actual model loading)
MODEL_LOADED = True


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Check service health and model status."""
    return HealthResponse(status="healthy", model_loaded=MODEL_LOADED)


@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
async def predict(request: PredictionRequest):
    """
    Generate a prediction from input features.

    Replace the mock prediction logic with your actual model inference.
    """
    if not MODEL_LOADED:
        logger.error("Model not loaded")
        raise HTTPException(status_code=503, detail="Model not available")

    logger.info(f"Received prediction request with {len(request.features)} features")

    # Mock prediction logic - replace with actual model inference
    # Example: prediction = model.predict([request.features])[0]
    prediction = sum(request.features) / len(request.features)
    confidence = 0.85

    logger.info(f"Generated prediction: {prediction} (confidence: {confidence})")

    return PredictionResponse(prediction=prediction, confidence=confidence)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "service": "ML Prediction Service",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
