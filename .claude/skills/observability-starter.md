# Skill: Observability Starter

## Trigger

Use this skill when setting up monitoring, logging, and observability for a service.

## Prerequisites

- Service running and accessible
- Basic understanding of logs, metrics, traces
- Access to monitoring tools (or willingness to set up)

**Level**: Intermediate+ (Tier 2)

## The Three Pillars

| Pillar | What | Why |
|--------|------|-----|
| **Logs** | Event records | Debug issues, audit trail |
| **Metrics** | Numeric measurements | Detect anomalies, track trends |
| **Traces** | Request flow | Understand latency, dependencies |

## Steps

### 1. Structured Logging (30 min)

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_record)

# Setup
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info("Processing request", extra={"request_id": "abc-123"})
```

**Log Levels**:
- `DEBUG`: Detailed debugging info
- `INFO`: Normal operations
- `WARNING`: Something unexpected
- `ERROR`: Something failed
- `CRITICAL`: System is down

### 2. Request ID Tracking (20 min)

```python
from fastapi import FastAPI, Request
from uuid import uuid4
import contextvars

# Context variable for request ID
request_id_var = contextvars.ContextVar('request_id', default=None)

app = FastAPI()

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid4()))
    request_id_var.set(request_id)

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

# In your logger
class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get()
        return True

logger.addFilter(RequestIDFilter())
```

### 3. Health Endpoints (15 min)

```python
from fastapi import FastAPI, HTTPException
from enum import Enum

class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

@app.get("/health")
async def health():
    """Liveness probe - is the process running?"""
    return {"status": HealthStatus.HEALTHY}

@app.get("/ready")
async def ready():
    """Readiness probe - can the service handle requests?"""
    checks = {
        "database": await check_database(),
        "cache": await check_cache(),
        "external_api": await check_external_api()
    }

    all_healthy = all(v == "ok" for v in checks.values())
    status = HealthStatus.HEALTHY if all_healthy else HealthStatus.DEGRADED

    return {"status": status, "checks": checks}

async def check_database() -> str:
    try:
        await db.execute("SELECT 1")
        return "ok"
    except Exception:
        return "error"
```

### 4. Basic Metrics (30 min)

```python
from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Response
import time

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time
    endpoint = request.url.path

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=endpoint
    ).observe(duration)

    return response

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

### 5. Error Tracking (20 min)

```python
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log the full error
    logger.error(
        f"Unhandled exception: {exc}",
        extra={
            "request_id": request_id_var.get(),
            "path": request.url.path,
            "method": request.method,
            "traceback": traceback.format_exc()
        }
    )

    # Return safe error to client
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "request_id": request_id_var.get()}
    )

# For production, consider Sentry
# import sentry_sdk
# sentry_sdk.init(dsn=settings.sentry_dsn)
```

### 6. Key Metrics to Track

| Metric | Type | Description |
|--------|------|-------------|
| `http_requests_total` | Counter | Total requests by endpoint/status |
| `http_request_duration_seconds` | Histogram | Request latency |
| `http_requests_in_flight` | Gauge | Current active requests |
| `db_query_duration_seconds` | Histogram | Database query time |
| `external_api_duration_seconds` | Histogram | External API latency |
| `cache_hits_total` | Counter | Cache hit/miss counts |
| `error_total` | Counter | Errors by type |

### 7. Dashboard Setup (Optional)

If using Grafana + Prometheus:

```yaml
# docker-compose.yml
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'myapp'
    static_configs:
      - targets: ['app:8000']
```

### 8. Alerting Rules (Optional)

```yaml
# alerts.yml
groups:
  - name: myapp
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "P95 latency above 2 seconds"
```

## Artifacts Produced

- Structured logging configuration
- Health check endpoints
- Metrics endpoint (`/metrics`)
- Error tracking setup
- (Optional) Dashboard configuration

## Quality Bar

- [ ] Logs are structured JSON
- [ ] Request IDs are tracked
- [ ] `/health` and `/ready` endpoints exist
- [ ] Basic metrics exposed
- [ ] Errors are logged with context

## Common Pitfalls

1. **Logging PII** - Be careful what you log
2. **High cardinality metrics** - Don't use user IDs as labels
3. **Missing request IDs** - Critical for debugging
4. **No health checks** - Orchestrators need these
5. **Silent failures** - Log all errors
