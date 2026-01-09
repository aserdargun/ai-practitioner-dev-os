"""FastAPI service for sentiment prediction."""

import logging
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from model import SentimentModel, load_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
MODEL_PATH = os.getenv("MODEL_PATH", "models/sentiment_model.json")

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple sentiment analysis service",
    version="1.0.0",
)

# Load model at startup
model: SentimentModel = None


@app.on_event("startup")
async def startup_event():
    """Load model on startup."""
    global model

    if Path(MODEL_PATH).exists():
        model = load_model(MODEL_PATH)
        logger.info(f"Loaded model from {MODEL_PATH}")
    else:
        # Create untrained model for demo
        model = SentimentModel()
        # Add some default words
        model.positive_words = [
            "good", "great", "love", "excellent", "amazing",
            "wonderful", "fantastic", "best", "happy", "perfect"
        ]
        model.negative_words = [
            "bad", "terrible", "hate", "awful", "worst",
            "horrible", "disappointing", "poor", "unhappy", "broken"
        ]
        model._trained = True
        logger.warning(f"Model not found at {MODEL_PATH}, using default")


class PredictRequest(BaseModel):
    """Request schema for prediction."""

    text: str = Field(
        ...,
        description="Text to analyze for sentiment",
        min_length=1,
        max_length=5000,
        examples=["I love this product!"],
    )


class PredictResponse(BaseModel):
    """Response schema for prediction."""

    sentiment: str = Field(..., description="Predicted sentiment")
    confidence: float = Field(..., description="Confidence score (0-1)")


class HealthResponse(BaseModel):
    """Response schema for health check."""

    status: str
    model_loaded: bool


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        model_loaded=model is not None and model.is_trained,
    )


@app.post("/predict", response_model=PredictResponse, tags=["Prediction"])
async def predict(request: PredictRequest):
    """Predict sentiment for input text."""
    if model is None or not model.is_trained:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Run train.py first.",
        )

    prediction = model.predict(request.text)

    logger.info(
        f"Predicted '{prediction.sentiment}' "
        f"(confidence: {prediction.confidence:.2f}) "
        f"for text: '{request.text[:50]}...'"
    )

    return PredictResponse(
        sentiment=prediction.sentiment,
        confidence=round(prediction.confidence, 2),
    )


@app.get("/", tags=["Info"])
async def root():
    """API information."""
    return {
        "name": "Sentiment Analysis API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "docs": "/docs",
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
