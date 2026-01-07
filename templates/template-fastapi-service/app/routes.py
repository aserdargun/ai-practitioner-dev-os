"""API route definitions."""

from fastapi import APIRouter, HTTPException

from app.models import (
    BatchPredictionInput,
    BatchPredictionOutput,
    ModelInfo,
    PredictionInput,
    PredictionOutput,
)
from app.predictor import predictor

router = APIRouter()


@router.get("/model/info", response_model=ModelInfo)
async def get_model_info():
    """Get model metadata."""
    return predictor.get_info()


@router.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    """Make a single prediction."""
    try:
        prediction, confidence = predictor.predict(input_data.features)
        return PredictionOutput(prediction=prediction, confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/predict/batch", response_model=BatchPredictionOutput)
async def predict_batch(input_data: BatchPredictionInput):
    """Make batch predictions."""
    try:
        instances = [item.features for item in input_data.instances]
        results = predictor.predict_batch(instances)
        predictions = [
            PredictionOutput(prediction=pred, confidence=conf)
            for pred, conf in results
        ]
        return BatchPredictionOutput(predictions=predictions)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
