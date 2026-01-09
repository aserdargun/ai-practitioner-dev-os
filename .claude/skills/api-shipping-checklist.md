# Skill: API Shipping Checklist

## Trigger

Use this skill when shipping a production-ready API service.

## Prerequisites

- API implementation complete (endpoints working)
- Test suite exists
- Deployment target identified

**Level**: Intermediate+ (Tier 2)

## Pre-Ship Checklist

### 1. Functionality ✅

- [ ] All endpoints working as documented
- [ ] Request validation implemented
- [ ] Error responses are consistent (JSON, status codes)
- [ ] Pagination for list endpoints
- [ ] CORS configured (if needed)

```python
# Example: Consistent error response
from fastapi import HTTPException
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str
    detail: str | None = None

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "detail": None}
    )
```

### 2. Security ✅

- [ ] No secrets in code (use environment variables)
- [ ] Input validation on all endpoints
- [ ] Rate limiting configured
- [ ] Authentication/Authorization (if needed)
- [ ] HTTPS only (production)
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (proper escaping)

```python
# Example: Environment-based config
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    database_url: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
```

### 3. Documentation ✅

- [ ] OpenAPI/Swagger docs generated
- [ ] All endpoints documented
- [ ] Request/response examples
- [ ] Error codes documented
- [ ] README with setup instructions

```python
# Example: FastAPI auto-docs
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="API for doing X",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

@app.get("/items/{item_id}", summary="Get an item", description="Retrieve item by ID")
async def get_item(item_id: int) -> Item:
    """Get a specific item by its ID."""
    ...
```

### 4. Testing ✅

- [ ] Unit tests for business logic
- [ ] Integration tests for endpoints
- [ ] Contract tests (if applicable)
- [ ] Load testing (basic)
- [ ] All tests passing in CI

```python
# Example: FastAPI test
from fastapi.testclient import TestClient

def test_health():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_item_not_found():
    client = TestClient(app)
    response = client.get("/items/999999")
    assert response.status_code == 404
```

### 5. Observability ✅

- [ ] Health check endpoint (`/health`)
- [ ] Readiness check endpoint (`/ready`)
- [ ] Structured logging (JSON)
- [ ] Request ID tracking
- [ ] Basic metrics (request count, latency)
- [ ] Error tracking configured

```python
# Example: Health endpoints
@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/ready")
async def ready():
    # Check dependencies
    try:
        await db.execute("SELECT 1")
        return {"status": "ready", "database": "connected"}
    except Exception as e:
        raise HTTPException(503, detail="Database not ready")
```

### 6. Performance ✅

- [ ] Response times acceptable (<500ms for most)
- [ ] Connection pooling for databases
- [ ] Caching where appropriate
- [ ] Async handlers for I/O-bound operations
- [ ] No N+1 queries

```python
# Example: Connection pooling
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(
    settings.database_url,
    pool_size=5,
    max_overflow=10
)
```

### 7. Deployment ✅

- [ ] Dockerfile working
- [ ] Docker image builds successfully
- [ ] Environment variables documented
- [ ] Graceful shutdown handling
- [ ] Container health check configured

```dockerfile
# Example: Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml .
RUN pip install .

COPY app/ app/

EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 8. Operations ✅

- [ ] Deployment runbook documented
- [ ] Rollback procedure defined
- [ ] Monitoring dashboards (if applicable)
- [ ] Alerting configured (if applicable)
- [ ] Secrets management (not in repo)

## Ship Day Checklist

```markdown
## Ship Day: [API Name]

### Pre-deployment
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Changelog updated
- [ ] Version bumped

### Deployment
- [ ] Deploy to staging
- [ ] Smoke test staging
- [ ] Deploy to production
- [ ] Smoke test production

### Post-deployment
- [ ] Monitor error rates
- [ ] Check response times
- [ ] Verify logs flowing
- [ ] Update documentation

### Rollback trigger
- Error rate > 5%
- P50 latency > 2x baseline
- Critical functionality broken
```

## Artifacts Produced

- Working API with all endpoints
- OpenAPI documentation
- Test suite (unit + integration)
- Dockerfile
- Deployment runbook
- CI/CD pipeline

## Quality Bar

- [ ] 0 critical security issues
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Health endpoints working
- [ ] Logs are structured
- [ ] Graceful error handling

## Common Pitfalls

1. **No health check** - Required for orchestrators
2. **Secrets in code** - Use environment variables
3. **Missing validation** - All input must be validated
4. **Poor error messages** - Be helpful but not leaky
5. **No rate limiting** - Protect against abuse
