# FastAPI Service Template

A production-ready FastAPI service template for ML model serving.

## Features

- FastAPI with async support
- Pydantic models for validation
- Health and readiness endpoints
- Docker support
- pytest test suite
- ruff linting

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -e ".[dev]"

# Run the service
uvicorn src.main:app --reload

# Run tests
pytest

# Run linting
ruff check src/ tests/
```

## Project Structure

```
template-fastapi-service/
├── src/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── models.py         # Pydantic models
│   └── routes/
│       ├── __init__.py
│       └── health.py     # Health endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py      # API tests
├── Dockerfile
├── pyproject.toml
└── README.md
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check |
| `/ready` | GET | Readiness check |
| `/predict` | POST | Model prediction |

## Configuration

Environment variables:
- `LOG_LEVEL`: Logging level (default: INFO)
- `MODEL_PATH`: Path to model file (optional)

## Docker

```bash
# Build
docker build -t fastapi-service .

# Run
docker run -p 8000:8000 fastapi-service
```

## Development

1. Create feature branch
2. Make changes
3. Run tests: `pytest`
4. Run linting: `ruff check .`
5. Commit and push

## License

MIT
