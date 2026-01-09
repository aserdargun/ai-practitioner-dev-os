"""
FastAPI Service Template

A minimal FastAPI application for serving ML models.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="ML Service",
    description="A template for serving ML models via REST API",
    version="1.0.0",
)


# --- Models ---


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    version: str


class PredictionInput(BaseModel):
    """Input schema for predictions."""

    features: list[float]


class PredictionOutput(BaseModel):
    """Output schema for predictions."""

    prediction: float
    confidence: float


# --- Endpoints ---


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "ML Service is running", "docs": "/docs"}


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.

    Returns service status and version.
    """
    return HealthResponse(status="healthy", version="1.0.0")


@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    """
    Make a prediction.

    This is a template endpoint. Replace with your model inference logic.

    Args:
        input_data: Features for prediction

    Returns:
        Prediction result with confidence score
    """
    # Validate input
    if not input_data.features:
        raise HTTPException(status_code=400, detail="Features cannot be empty")

    # Template: Simple mean as "prediction"
    # Replace this with your actual model inference
    prediction = sum(input_data.features) / len(input_data.features)

    return PredictionOutput(
        prediction=round(prediction, 4),
        confidence=0.95,  # Replace with actual confidence
    )


# --- Startup/Shutdown ---


@app.on_event("startup")
async def startup_event():
    """
    Startup event handler.

    Load your model here:
    ```
    global model
    model = joblib.load("model.pkl")
    ```
    """
    print("Service starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler."""
    print("Service shutting down...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
