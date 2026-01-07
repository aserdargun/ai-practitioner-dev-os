# Skill: Observability Starter

**Tier**: 2 (Intermediate)

Add logging, metrics, and tracing to your application for production visibility.

---

## Trigger

Use this skill when:
- Deploying to production
- Need to debug issues in running systems
- Want to understand system behavior

## Prerequisites

- [ ] Working application (API or service)
- [ ] Python environment
- [ ] Basic understanding of logging concepts

## Steps

### Step 1: Set Up Structured Logging (15 min)

```python
# app/logging_config.py
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Format logs as JSON for easy parsing."""

    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }

        # Add extra fields if present
        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id
        if hasattr(record, 'user_id'):
            log_record['user_id'] = record.user_id

        return json.dumps(log_record)

def setup_logging(level=logging.INFO):
    """Configure structured logging."""
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(handler)

    return root_logger

# Usage
logger = setup_logging()
logger.info("Application started", extra={"request_id": "abc123"})
```

**Checkpoint**: Structured JSON logs working.

### Step 2: Add Request Logging Middleware (15 min)

```python
# app/middleware.py
import time
import uuid
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log all requests with timing and metadata."""

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        start_time = time.time()

        # Add request_id to request state
        request.state.request_id = request_id

        # Log request
        logger.info(
            f"Request started: {request.method} {request.url.path}",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "client": request.client.host if request.client else None
            }
        )

        # Process request
        response = await call_next(request)

        # Log response
        duration_ms = (time.time() - start_time) * 1000
        logger.info(
            f"Request completed: {response.status_code} in {duration_ms:.2f}ms",
            extra={
                "request_id": request_id,
                "status_code": response.status_code,
                "duration_ms": duration_ms
            }
        )

        # Add request_id to response headers
        response.headers["X-Request-ID"] = request_id

        return response

# In main.py
# app.add_middleware(RequestLoggingMiddleware)
```

**Checkpoint**: All requests logged with timing.

### Step 3: Add Application Metrics (15 min)

```python
# app/metrics.py
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
)

PREDICTION_COUNT = Counter(
    'predictions_total',
    'Total predictions made',
    ['model_version']
)

# Metrics endpoint
def get_metrics():
    """Return Prometheus metrics."""
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

# Usage in endpoints
# REQUEST_COUNT.labels(method='POST', endpoint='/predict', status=200).inc()
# with REQUEST_LATENCY.labels(method='POST', endpoint='/predict').time():
#     # ... do prediction
```

```python
# In main.py
from app.metrics import get_metrics, REQUEST_COUNT, REQUEST_LATENCY

@app.get("/metrics")
def metrics():
    return get_metrics()
```

**Checkpoint**: Prometheus metrics exposed at /metrics.

### Step 4: Add Health Checks (10 min)

```python
# app/health.py
from typing import Dict
import time

class HealthChecker:
    """Check health of application dependencies."""

    def __init__(self):
        self.checks = {}

    def register(self, name: str, check_func):
        """Register a health check."""
        self.checks[name] = check_func

    def run_checks(self) -> Dict:
        """Run all health checks."""
        results = {"status": "healthy", "checks": {}}

        for name, check_func in self.checks.items():
            try:
                start = time.time()
                check_func()
                duration_ms = (time.time() - start) * 1000
                results["checks"][name] = {
                    "status": "healthy",
                    "duration_ms": duration_ms
                }
            except Exception as e:
                results["status"] = "unhealthy"
                results["checks"][name] = {
                    "status": "unhealthy",
                    "error": str(e)
                }

        return results

# Usage
health_checker = HealthChecker()

def check_model():
    if model is None:
        raise Exception("Model not loaded")

def check_database():
    # db.execute("SELECT 1")
    pass

health_checker.register("model", check_model)
health_checker.register("database", check_database)

@app.get("/health")
def health():
    return health_checker.run_checks()
```

**Checkpoint**: Comprehensive health checks.

### Step 5: Add Error Tracking (10 min)

```python
# app/error_tracking.py
import logging
import traceback
from typing import Optional

logger = logging.getLogger(__name__)

class ErrorTracker:
    """Track and log errors with context."""

    @staticmethod
    def capture_exception(
        exception: Exception,
        context: Optional[dict] = None,
        request_id: Optional[str] = None
    ):
        """Log an exception with context."""
        error_info = {
            "error_type": type(exception).__name__,
            "error_message": str(exception),
            "traceback": traceback.format_exc(),
            "request_id": request_id,
            "context": context or {}
        }

        logger.error(
            f"Exception occurred: {type(exception).__name__}: {exception}",
            extra=error_info
        )

        # In production, send to error tracking service
        # sentry_sdk.capture_exception(exception)

        return error_info

# Usage in exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    request_id = getattr(request.state, 'request_id', None)
    ErrorTracker.capture_exception(exc, request_id=request_id)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
```

**Checkpoint**: Errors tracked with full context.

### Step 6: Create Dashboard Config (10 min)

For Grafana dashboard, create `grafana/dashboard.json`:

```json
{
  "title": "API Dashboard",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(http_requests_total[5m])",
          "legendFormat": "{{method}} {{endpoint}}"
        }
      ]
    },
    {
      "title": "Latency (p95)",
      "type": "graph",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
          "legendFormat": "{{endpoint}}"
        }
      ]
    },
    {
      "title": "Error Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(http_requests_total{status=~\"5..\"}[5m])",
          "legendFormat": "{{endpoint}}"
        }
      ]
    }
  ]
}
```

**Checkpoint**: Dashboard configuration ready.

### Step 7: Document Observability (10 min)

```markdown
## Observability Guide

### Logging
- Logs are JSON-formatted for parsing
- Each request has a unique `request_id`
- Log levels: DEBUG, INFO, WARNING, ERROR

### Metrics (Prometheus)
Available at `/metrics`:
- `http_requests_total` - Request counter by method, endpoint, status
- `http_request_duration_seconds` - Request latency histogram
- `predictions_total` - Prediction counter by model version

### Health Checks
Available at `/health`:
- Returns status of all dependencies
- Returns "unhealthy" if any check fails

### Alerting Recommendations
- Alert if error rate > 1% for 5 minutes
- Alert if p95 latency > 1s for 5 minutes
- Alert if health check fails for 1 minute
```

**Checkpoint**: Observability documented.

## Artifacts Produced

- [ ] Structured logging configuration
- [ ] Request logging middleware
- [ ] Prometheus metrics
- [ ] Health check endpoints
- [ ] Error tracking
- [ ] Dashboard configuration
- [ ] Documentation

## Quality Bar

✅ **Done when**:
- All requests are logged
- Metrics exposed at /metrics
- Health check covers dependencies
- Errors logged with context
- Dashboard shows key metrics
- Runbook documented

## Example Prompt

```
I have a FastAPI prediction service. Help me add:

1. Structured JSON logging
2. Request timing metrics
3. Health checks for model and database
4. A Prometheus metrics endpoint

I want to deploy this with Grafana monitoring.
```

## Related Skills

- [API Shipping Checklist](api-shipping-checklist.md) - Build API first
- [K8s Deploy Checklist](k8s-deploy-checklist.md) - Deploy with observability
