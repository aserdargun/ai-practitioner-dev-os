# Skill: Observability Starter

Add logging, metrics, and tracing to your application.

## Trigger

Use this skill when:
- Deploying to production
- Debugging issues in deployed code
- Need visibility into application behavior
- Building dashboards for monitoring

## Prerequisites

- Deployed or deployable application
- Basic understanding of logs/metrics/traces
- Monitoring platform access (optional for local dev)

## Steps

### 1. Structured Logging (20 min)

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        # Add exception info if present
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        # Add extra fields
        if hasattr(record, 'extra'):
            log_entry.update(record.extra)

        return json.dumps(log_entry)

def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger

logger = setup_logging()

# Usage
logger.info("Processing request", extra={"request_id": "abc123", "user_id": 42})
```

### 2. Request Logging Middleware (15 min)

```python
import time
import uuid
from fastapi import Request

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())[:8]
    start_time = time.time()

    # Log request
    logger.info("Request started", extra={
        "request_id": request_id,
        "method": request.method,
        "path": request.url.path,
        "client_ip": request.client.host,
    })

    # Process request
    response = await call_next(request)

    # Log response
    duration_ms = (time.time() - start_time) * 1000
    logger.info("Request completed", extra={
        "request_id": request_id,
        "status_code": response.status_code,
        "duration_ms": round(duration_ms, 2),
    })

    # Add request ID to response headers
    response.headers["X-Request-ID"] = request_id

    return response
```

### 3. Application Metrics (20 min)

```python
from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Response

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'path', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'path']
)

PREDICTION_COUNT = Counter(
    'predictions_total',
    'Total predictions made',
    ['model_version', 'result']
)

# Middleware to collect metrics
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        path=request.url.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        path=request.url.path
    ).observe(duration)

    return response

# Metrics endpoint
@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )
```

### 4. Health Check with Details (10 min)

```python
@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/health/ready")
def readiness():
    """Check if dependencies are ready."""
    checks = {
        "model_loaded": model is not None,
        "database": check_database_connection(),
    }

    all_ready = all(checks.values())

    return {
        "status": "ready" if all_ready else "not_ready",
        "checks": checks
    }

@app.get("/health/live")
def liveness():
    """Check if application is alive."""
    return {"status": "alive"}
```

### 5. Error Tracking (15 min)

```python
import traceback

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    # Log full error
    logger.error("Unhandled exception", extra={
        "request_id": getattr(request.state, 'request_id', 'unknown'),
        "path": request.url.path,
        "method": request.method,
        "error_type": type(exc).__name__,
        "error_message": str(exc),
        "traceback": traceback.format_exc(),
    })

    # Increment error counter
    ERROR_COUNT.labels(error_type=type(exc).__name__).inc()

    # Return safe error response
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
```

### 6. Distributed Tracing (Optional, 20 min)

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Setup tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Add exporter (e.g., to Jaeger)
otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317")
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# Usage in code
@app.post("/predict")
async def predict(request: PredictionRequest):
    with tracer.start_as_current_span("predict") as span:
        span.set_attribute("features_count", len(request.features))

        with tracer.start_as_current_span("model_inference"):
            prediction = model.predict([request.features])[0]

        span.set_attribute("prediction", prediction)

        return {"prediction": prediction}
```

### 7. Dashboard Setup (varies)

For local development, use Prometheus + Grafana:

```yaml
# docker-compose.yml
version: '3'
services:
  app:
    build: .
    ports:
      - "8000:8000"

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

## Artifacts Produced

- [ ] Structured logging setup
- [ ] Request/response logging middleware
- [ ] Metrics endpoint (`/metrics`)
- [ ] Health check endpoints
- [ ] Error tracking integration
- [ ] Dashboard configuration (optional)

## Quality Bar

- [ ] All requests logged with request ID
- [ ] Errors logged with full context
- [ ] Key metrics exposed (latency, errors, throughput)
- [ ] Health checks accurate
- [ ] No sensitive data in logs
- [ ] Logs are JSON formatted

## Common Pitfalls

1. **Logging too much**
   - Log at INFO level for normal ops, DEBUG for details

2. **Missing correlation IDs**
   - Request ID ties logs together

3. **Metrics cardinality explosion**
   - Don't use unbounded labels (like user ID)

4. **Logging sensitive data**
   - Never log passwords, tokens, or PII

5. **No alerting**
   - Metrics without alerts are just data
