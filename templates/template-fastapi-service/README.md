# FastAPI Service Template

A minimal, production-ready FastAPI service template for ML model serving.

## Features

- Health check endpoint
- Prediction endpoint with request validation
- Structured logging
- Docker support
- Pytest configuration

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run the service
uvicorn app.main:app --reload

# Test health endpoint
curl http://localhost:8000/health

# Test prediction endpoint
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0]}'
```

## Project Structure

```
template-fastapi-service/
├── app/
│   └── main.py          # FastAPI application
├── tests/
│   └── test_health.py   # Health check tests
├── Dockerfile           # Container definition
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## Running Tests

```bash
pytest tests/ -v
```

## Docker

```bash
# Build image
docker build -t fastapi-service .

# Run container
docker run -p 8000:8000 fastapi-service
```

## Customization

1. Add your model loading logic in `app/main.py`
2. Update the `PredictionRequest` schema for your input format
3. Implement your prediction logic in the `/predict` endpoint
4. Add additional tests in `tests/`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MODEL_PATH` | Path to model file | `models/model.pkl` |
| `LOG_LEVEL` | Logging level | `INFO` |

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
