# FastAPI Service Template

A minimal, production-ready FastAPI service template for serving ML models.

## What This Template Provides

- FastAPI application structure
- Health check endpoint
- Prediction endpoint pattern
- Docker configuration
- Test setup with pytest
- Code quality with ruff

## Quick Start

### 1. Install Dependencies

```bash
cd template-fastapi-service
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
pytest
```

### 3. Start the Server

```bash
uvicorn app.main:app --reload
```

### 4. Test the Endpoints

```bash
# Health check
curl http://localhost:8000/health

# API docs
open http://localhost:8000/docs
```

## Project Structure

```
template-fastapi-service/
├── app/
│   └── main.py           # FastAPI application
├── tests/
│   └── test_health.py    # Test suite
├── Dockerfile            # Container configuration
├── pyproject.toml        # Dependencies and tooling
└── README.md
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/` | Root endpoint |
| POST | `/predict` | Make a prediction |
| GET | `/docs` | OpenAPI documentation |

## Customization

### Adding Your Model

1. Load your model in `app/main.py`
2. Update the `/predict` endpoint input/output schemas
3. Add model-specific tests

### Example Prediction Endpoint

```python
from pydantic import BaseModel

class PredictionInput(BaseModel):
    features: list[float]

class PredictionOutput(BaseModel):
    prediction: float
    confidence: float

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    # Your model inference here
    result = model.predict([input_data.features])
    return PredictionOutput(
        prediction=result[0],
        confidence=0.95
    )
```

## Docker

### Build

```bash
docker build -t fastapi-service .
```

### Run

```bash
docker run -p 8000:8000 fastapi-service
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_health.py -v
```

## Code Quality

```bash
# Check code style
ruff check .

# Format code
ruff format .
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host |
| `PORT` | `8000` | Server port |
| `LOG_LEVEL` | `info` | Logging level |

## Deployment Checklist

- [ ] Update model loading code
- [ ] Configure environment variables
- [ ] Set up health monitoring
- [ ] Configure logging
- [ ] Run security scan
- [ ] Load test endpoints
- [ ] Deploy to staging first

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [uvicorn Documentation](https://www.uvicorn.org/)
