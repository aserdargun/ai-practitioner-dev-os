# FastAPI Service Template

A production-ready FastAPI template for deploying ML models as REST APIs.

## Features

- Health check endpoint
- Structured logging
- Docker support
- Type hints throughout
- Pytest integration
- Ruff linting

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run locally
uvicorn app.main:app --reload

# Run tests
pytest

# Build Docker image
docker build -t fastapi-service .

# Run container
docker run -p 8000:8000 fastapi-service
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/predict` | POST | Model prediction |
| `/docs` | GET | Swagger UI |

## Project Structure

```
template-fastapi-service/
├── app/
│   └── main.py        # FastAPI application
├── tests/
│   └── test_health.py # Test suite
├── Dockerfile         # Container definition
├── pyproject.toml     # Dependencies and config
└── README.md
```

## Configuration

Environment variables:
- `LOG_LEVEL`: Logging level (default: INFO)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)

## Customization

1. Add your model loading in `app/main.py`
2. Implement the `/predict` endpoint with your inference logic
3. Add input validation with Pydantic models
4. Write tests for your endpoints

## Usage in Curriculum

This template is used in:
- Month 04: API Development
- Month 07: Deployment with Docker
- Month 09: Cloud Deployment
