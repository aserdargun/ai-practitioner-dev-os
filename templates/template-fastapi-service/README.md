# FastAPI ML Service Template

A minimal template for deploying ML models as REST APIs using FastAPI.

## Features

- Health check endpoint
- Model info endpoint
- Prediction endpoint (single and batch)
- Input validation with Pydantic
- Error handling
- Docker support
- Tests included

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -e ".[dev]"

# Run the server
uvicorn app.main:app --reload

# Run tests
pytest
```

### Docker

```bash
# Build
docker build -t ml-service .

# Run
docker run -p 8000:8000 ml-service
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/model/info` | GET | Model metadata |
| `/predict` | POST | Single prediction |
| `/predict/batch` | POST | Batch predictions |

## Project Structure

```
template-fastapi-service/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── models.py         # Pydantic models
│   ├── predictor.py      # ML model wrapper
│   └── routes.py         # API routes
├── tests/
│   ├── __init__.py
│   └── test_api.py       # API tests
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Usage

### Making Predictions

```python
import requests

# Single prediction
response = requests.post(
    "http://localhost:8000/predict",
    json={"features": [1.0, 2.0, 3.0, 4.0]}
)
print(response.json())

# Batch prediction
response = requests.post(
    "http://localhost:8000/predict/batch",
    json={"instances": [
        {"features": [1.0, 2.0, 3.0, 4.0]},
        {"features": [5.0, 6.0, 7.0, 8.0]}
    ]}
)
print(response.json())
```

### cURL Examples

```bash
# Health check
curl http://localhost:8000/health

# Model info
curl http://localhost:8000/model/info

# Single prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0, 4.0]}'

# Batch prediction
curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{"instances": [{"features": [1.0, 2.0, 3.0, 4.0]}]}'
```

## Customization

### Adding Your Model

1. Update `app/predictor.py` with your model loading and inference logic
2. Update `app/models.py` with your input/output schemas
3. Update tests in `tests/test_api.py`

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MODEL_PATH` | Path to model file | `model.pkl` |
| `LOG_LEVEL` | Logging level | `INFO` |

## License

MIT
