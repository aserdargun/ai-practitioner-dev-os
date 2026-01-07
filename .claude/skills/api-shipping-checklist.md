# Skill: API Shipping Checklist

**Tier**: 1-2 (Beginner to Intermediate)

Deploy a production-ready API for your ML model or service.

---

## Trigger

Use this skill when:
- Model is ready to be served
- Need to expose functionality via HTTP
- Building a service for others to consume

## Prerequisites

- [ ] Working model or logic to expose
- [ ] Python environment with FastAPI
- [ ] Basic understanding of REST APIs

## Steps

### Step 1: Set Up FastAPI Project (10 min)

```bash
# Create project structure
mkdir my-api
cd my-api
mkdir app tests
touch app/__init__.py app/main.py
touch tests/__init__.py tests/test_health.py
```

```python
# app/main.py
from fastapi import FastAPI

app = FastAPI(
    title="My ML API",
    description="API for serving predictions",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
```

**Checkpoint**: Basic FastAPI app running.

### Step 2: Define Request/Response Models (10 min)

```python
# app/models.py
from pydantic import BaseModel, Field
from typing import List, Optional

class PredictionRequest(BaseModel):
    """Request schema for predictions."""
    features: List[float] = Field(..., description="Input features")

    class Config:
        json_schema_extra = {
            "example": {
                "features": [1.0, 2.0, 3.0, 4.0]
            }
        }

class PredictionResponse(BaseModel):
    """Response schema for predictions."""
    prediction: float
    confidence: Optional[float] = None
    model_version: str

class ErrorResponse(BaseModel):
    """Error response schema."""
    error: str
    detail: Optional[str] = None
```

**Checkpoint**: Pydantic models defined with examples.

### Step 3: Add Prediction Endpoint (15 min)

```python
# app/main.py (updated)
from fastapi import FastAPI, HTTPException
from app.models import PredictionRequest, PredictionResponse, ErrorResponse
import joblib

app = FastAPI(
    title="My ML API",
    description="API for serving predictions",
    version="1.0.0"
)

# Load model at startup
MODEL_PATH = "models/model.joblib"
MODEL_VERSION = "1.0.0"

@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"Warning: Could not load model: {e}")
        model = None

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """Make a prediction."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    try:
        prediction = model.predict([request.features])[0]
        return PredictionResponse(
            prediction=float(prediction),
            model_version=MODEL_VERSION
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

**Checkpoint**: Prediction endpoint working.

### Step 4: Add Input Validation (10 min)

```python
# app/models.py (updated with validation)
from pydantic import BaseModel, Field, validator
from typing import List

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=4, max_items=4)

    @validator('features')
    def validate_features(cls, v):
        for i, feat in enumerate(v):
            if feat < -1000 or feat > 1000:
                raise ValueError(f'Feature {i} out of valid range [-1000, 1000]')
        return v
```

**Checkpoint**: Input validation in place.

### Step 5: Add Error Handling (10 min)

```python
# app/main.py (add error handlers)
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
```

**Checkpoint**: Graceful error handling.

### Step 6: Write Tests (15 min)

```python
# tests/test_health.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_valid():
    response = client.post(
        "/predict",
        json={"features": [1.0, 2.0, 3.0, 4.0]}
    )
    # Will be 503 if model not loaded, which is expected in test
    assert response.status_code in [200, 503]

def test_predict_invalid_features():
    response = client.post(
        "/predict",
        json={"features": [1.0, 2.0]}  # Too few features
    )
    assert response.status_code == 422  # Validation error
```

```bash
# Run tests
pytest tests/ -v
```

**Checkpoint**: Tests passing.

### Step 7: Create Dockerfile (10 min)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/ ./app/
COPY models/ ./models/

# Expose port
EXPOSE 8000

# Run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```txt
# requirements.txt
fastapi>=0.100.0
uvicorn>=0.23.0
pydantic>=2.0.0
joblib>=1.3.0
scikit-learn>=1.3.0
```

```bash
# Build and run
docker build -t my-api .
docker run -p 8000:8000 my-api
```

**Checkpoint**: Docker image builds and runs.

### Step 8: Document API (10 min)

FastAPI auto-generates docs at `/docs` (Swagger) and `/redoc`.

Create README.md:

```markdown
# My ML API

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn app.main:app --reload

# Run with Docker
docker build -t my-api .
docker run -p 8000:8000 my-api
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
| POST | /predict | Make prediction |

## Example Request

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0, 4.0]}'
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
```

**Checkpoint**: Documentation complete.

## Artifacts Produced

- [ ] FastAPI application
- [ ] Pydantic request/response models
- [ ] Tests (passing)
- [ ] Dockerfile
- [ ] README with usage instructions

## Quality Bar

✅ **Done when**:
- Health check returns 200
- Prediction endpoint works
- Input validation catches bad requests
- Tests pass
- Docker builds successfully
- Docs accessible at /docs

## Pre-Ship Checklist

Before deploying:

- [ ] Health endpoint works
- [ ] All tests pass
- [ ] Input validation in place
- [ ] Error responses are clean (no stack traces)
- [ ] No hardcoded secrets
- [ ] Docker image builds
- [ ] README updated
- [ ] API docs reviewed

## Example Prompt

```
I have a trained scikit-learn model (model.joblib) that predicts house prices
from 4 features. Help me:

1. Create a FastAPI service to serve predictions
2. Add proper validation and error handling
3. Write tests
4. Create a Dockerfile

The API should be production-ready.
```

## Related Skills

- [Baseline Model and Card](baseline-model-and-card.md) - Create model first
- [Observability Starter](observability-starter.md) - Add monitoring
