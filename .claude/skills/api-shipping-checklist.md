# Skill: API Shipping Checklist

Deploy a production-ready API with proper testing, documentation, and monitoring.

## Trigger

Use this skill when:
- Deploying a model as an API
- Building backend services
- Creating microservices
- Shipping to production

## Prerequisites

- [ ] Core functionality implemented and tested locally
- [ ] API framework chosen (FastAPI recommended)
- [ ] Deployment target identified
- [ ] CI/CD pipeline available

## Steps

### 1. API Structure (30 min)

```
my-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── config.py        # Configuration
│   ├── models.py        # Pydantic models
│   ├── routers/
│   │   ├── __init__.py
│   │   └── predict.py   # Prediction endpoints
│   └── services/
│       ├── __init__.py
│       └── model.py     # ML model logic
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
├── Dockerfile
├── pyproject.toml
└── README.md
```

### 2. Define API Contract (20 min)

```python
# app/models.py
from pydantic import BaseModel, Field
from typing import Optional, List

class PredictionRequest(BaseModel):
    """Input for prediction endpoint."""
    text: str = Field(..., min_length=1, max_length=10000)
    options: Optional[dict] = None

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Sample input text",
                "options": {"temperature": 0.7}
            }
        }

class PredictionResponse(BaseModel):
    """Output from prediction endpoint."""
    prediction: str
    confidence: float = Field(..., ge=0, le=1)
    metadata: Optional[dict] = None
```

### 3. Implement Endpoints (30 min)

```python
# app/main.py
from fastapi import FastAPI, HTTPException
from app.models import PredictionRequest, PredictionResponse
from app.services.model import ModelService

app = FastAPI(
    title="ML API",
    description="Production ML service",
    version="1.0.0"
)

model_service = ModelService()

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Generate prediction."""
    try:
        result = model_service.predict(request.text, request.options)
        return PredictionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 4. Write Tests (30 min)

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_success():
    response = client.post(
        "/predict",
        json={"text": "test input"}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "confidence" in response.json()

def test_predict_invalid_input():
    response = client.post(
        "/predict",
        json={"text": ""}  # Empty string should fail
    )
    assert response.status_code == 422  # Validation error

def test_predict_missing_field():
    response = client.post(
        "/predict",
        json={}  # Missing required field
    )
    assert response.status_code == 422
```

### 5. Containerize (20 min)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy application
COPY app/ app/

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Run
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and test
docker build -t my-api:latest .
docker run -p 8000:8000 my-api:latest
```

### 6. Production Checklist

#### Security
- [ ] Input validation on all endpoints
- [ ] Rate limiting configured
- [ ] CORS settings appropriate
- [ ] No secrets in code/images
- [ ] Non-root container user

#### Reliability
- [ ] Health check endpoint
- [ ] Graceful shutdown handling
- [ ] Request timeouts set
- [ ] Error handling comprehensive
- [ ] Retry logic for dependencies

#### Observability
- [ ] Structured logging
- [ ] Request ID tracking
- [ ] Metrics endpoint
- [ ] Error alerting configured

#### Documentation
- [ ] OpenAPI spec complete
- [ ] README with setup instructions
- [ ] Example requests documented
- [ ] Error codes documented

### 7. Deploy (varies)

**Docker Compose** (development):
```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - LOG_LEVEL=INFO
```

**Cloud Run** (example):
```bash
gcloud run deploy my-api \
  --image gcr.io/project/my-api:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 8. Post-Deploy Verification

```bash
# Health check
curl https://my-api.run.app/health

# Test prediction
curl -X POST https://my-api.run.app/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "test input"}'

# Check OpenAPI docs
open https://my-api.run.app/docs
```

## Artifacts

| Artifact | Description |
|----------|-------------|
| `app/` | Application code |
| `tests/` | Test suite |
| `Dockerfile` | Container definition |
| `pyproject.toml` | Dependencies |
| `README.md` | Setup and usage docs |

## Quality Bar

- [ ] All tests passing
- [ ] Health endpoint working
- [ ] Input validation complete
- [ ] OpenAPI docs generated
- [ ] Container builds successfully
- [ ] Local testing works end-to-end

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 4-6 hours |
| Practiced | 2-3 hours |
| Expert | 1-2 hours |

## Common Pitfalls

- Skipping input validation
- Not handling errors gracefully
- Missing health checks
- Secrets in container images
- No request timeouts
- Insufficient logging
