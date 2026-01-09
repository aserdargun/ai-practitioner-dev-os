# Skill: API Shipping Checklist

Deploy a production-ready REST API.

## Trigger

Use this skill when:
- Building a web API (REST/GraphQL)
- Deploying an ML model as a service
- Creating microservices
- Preparing for production deployment

## Prerequisites

- Working application code
- Clear API contract (endpoints, inputs, outputs)
- Deployment target identified (cloud, container, serverless)
- Basic understanding of HTTP and REST

## Steps

### 1. Define API Contract (15 min)

```yaml
# openapi.yaml (or document in markdown)
openapi: 3.0.0
info:
  title: Prediction API
  version: 1.0.0

paths:
  /health:
    get:
      summary: Health check
      responses:
        '200':
          description: Service is healthy

  /predict:
    post:
      summary: Get prediction
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                features:
                  type: array
                  items:
                    type: number
      responses:
        '200':
          description: Prediction result
          content:
            application/json:
              schema:
                type: object
                properties:
                  prediction:
                    type: number
                  confidence:
                    type: number
```

### 2. Implement Endpoints (30 min)

```python
# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI(title="Prediction API")

# Load model at startup
model = joblib.load("model.pkl")

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        prediction = model.predict([request.features])[0]
        confidence = model.predict_proba([request.features]).max()
        return PredictionResponse(
            prediction=prediction,
            confidence=confidence
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 3. Add Input Validation (15 min)

```python
from pydantic import BaseModel, validator

class PredictionRequest(BaseModel):
    features: list[float]

    @validator('features')
    def validate_features(cls, v):
        if len(v) != 10:  # Expected feature count
            raise ValueError(f"Expected 10 features, got {len(v)}")
        if any(x < 0 for x in v):
            raise ValueError("Features must be non-negative")
        return v
```

### 4. Add Error Handling (15 min)

```python
from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if app.debug else "An error occurred"
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTP exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
```

### 5. Add Logging (10 min)

```python
import time
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time
    logger.info(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} duration={duration:.3f}s"
    )

    return response
```

### 6. Write Tests (20 min)

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_valid():
    response = client.post("/predict", json={
        "features": [1.0] * 10
    })
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "confidence" in response.json()

def test_predict_invalid_features():
    response = client.post("/predict", json={
        "features": [1.0, 2.0]  # Wrong count
    })
    assert response.status_code == 422  # Validation error

def test_predict_missing_body():
    response = client.post("/predict")
    assert response.status_code == 422
```

### 7. Create Dockerfile (10 min)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY model.pkl .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 8. Pre-Deploy Checklist (15 min)

```markdown
## Pre-Deploy Checklist

### Functionality
- [ ] All endpoints work as expected
- [ ] Input validation catches bad inputs
- [ ] Error responses are informative but safe
- [ ] Health check endpoint exists

### Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual smoke test completed
- [ ] Edge cases tested

### Security
- [ ] No hardcoded secrets
- [ ] Input validation prevents injection
- [ ] CORS configured appropriately
- [ ] Rate limiting considered

### Operations
- [ ] Logging captures important events
- [ ] Metrics endpoint or integration
- [ ] Health check for load balancer
- [ ] Graceful shutdown handling

### Documentation
- [ ] API docs accessible (FastAPI: /docs)
- [ ] README has setup instructions
- [ ] Environment variables documented

### Performance
- [ ] Response time acceptable (<200ms for simple calls)
- [ ] Memory usage reasonable
- [ ] Can handle expected load
```

### 9. Deploy (varies)

```bash
# Local Docker
docker build -t prediction-api .
docker run -p 8000:8000 prediction-api

# Cloud Run (example)
gcloud run deploy prediction-api \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# Verify
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1,2,3,4,5,6,7,8,9,10]}'
```

## Artifacts Produced

- [ ] API source code (`app/main.py`)
- [ ] Tests (`tests/test_api.py`)
- [ ] Dockerfile
- [ ] requirements.txt
- [ ] OpenAPI spec or API docs
- [ ] Deployment configuration

## Quality Bar

- [ ] Health check returns 200
- [ ] All tests pass
- [ ] Invalid inputs return 4xx, not 500
- [ ] Logs show request/response info
- [ ] Response time < 500ms for typical requests
- [ ] Container builds and runs locally

## Common Pitfalls

1. **No health check**
   - Load balancers need it; always include

2. **Returning 500 for user errors**
   - Validate input and return 400/422

3. **Logging secrets**
   - Never log passwords, tokens, or PII

4. **No timeout handling**
   - Add request timeouts for external calls

5. **Missing CORS**
   - Frontend can't call if CORS isn't set
