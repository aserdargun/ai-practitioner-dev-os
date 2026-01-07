"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.models import PredictionRequest, PredictionResponse
from src.routes import health

app = FastAPI(
    title="FastAPI Service Template",
    description="A template for ML model serving with FastAPI",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["Health"])


@app.get("/")
async def root() -> dict:
    """Root endpoint with welcome message."""
    return {"message": "Welcome to FastAPI Service Template", "version": "0.1.0"}


@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest) -> PredictionResponse:
    """Make a prediction with the model.

    Args:
        request: Prediction request with features

    Returns:
        Prediction response with result
    """
    # TODO: Replace with actual model inference
    # This is a placeholder that returns a dummy prediction
    prediction = sum(request.features) / len(request.features)
    confidence = 0.95

    return PredictionResponse(
        prediction=prediction,
        confidence=confidence,
        model_version="0.1.0",
    )
