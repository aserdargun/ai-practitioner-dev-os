# Skill: Observability Starter

Set up basic monitoring, logging, and alerting for your services.

## Trigger

Use this skill when:
- Deploying services to production
- Debugging production issues
- Need visibility into system behavior
- Setting up proactive alerting

## Prerequisites

- [ ] Service deployed and accessible
- [ ] Access to monitoring platform (or local setup)
- [ ] Understanding of key metrics for your service
- [ ] Alerting channel configured (email, Slack, etc.)

## Steps

### 1. Define Key Metrics (20 min)

**The Four Golden Signals**:

| Signal | What to Measure | Example Metric |
|--------|-----------------|----------------|
| Latency | Time to handle requests | `request_duration_seconds` |
| Traffic | Demand on system | `requests_total` |
| Errors | Rate of failures | `errors_total` |
| Saturation | Resource utilization | `cpu_usage_percent` |

**Service-Specific Metrics**:
```python
# For ML services
model_prediction_latency
model_prediction_count
model_error_rate
input_token_count
output_token_count

# For data pipelines
records_processed
processing_time
queue_depth
failed_records
```

### 2. Add Structured Logging (20 min)

```python
# app/logging_config.py
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        if hasattr(record, 'request_id'):
            log_obj["request_id"] = record.request_id
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_obj)

# Configure logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info("Processing request", extra={"request_id": "abc-123"})
```

### 3. Instrument with Metrics (30 min)

```python
# Using prometheus_client
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Define metrics
REQUEST_COUNT = Counter(
    'requests_total',
    'Total request count',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'request_duration_seconds',
    'Request latency',
    ['method', 'endpoint'],
    buckets=[.01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10]
)

MODEL_PREDICTIONS = Counter(
    'model_predictions_total',
    'Total predictions made',
    ['model_version']
)

# Middleware example (FastAPI)
from fastapi import Request
import time

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(duration)

    return response

# Metrics endpoint
@app.get("/metrics")
async def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
```

### 4. Set Up Tracing (Optional, 30 min)

```python
# Using OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Configure
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

# Usage
with tracer.start_as_current_span("process_request") as span:
    span.set_attribute("user_id", user_id)
    result = process(data)
    span.set_attribute("result_size", len(result))
```

### 5. Create Dashboard (30 min)

**Grafana Dashboard Panels** (example):

```json
{
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {"expr": "rate(requests_total[5m])"}
      ]
    },
    {
      "title": "Latency (p95)",
      "type": "graph",
      "targets": [
        {"expr": "histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))"}
      ]
    },
    {
      "title": "Error Rate",
      "type": "graph",
      "targets": [
        {"expr": "rate(requests_total{status=~'5..'}[5m]) / rate(requests_total[5m])"}
      ]
    },
    {
      "title": "CPU Usage",
      "type": "gauge",
      "targets": [
        {"expr": "process_cpu_seconds_total"}
      ]
    }
  ]
}
```

### 6. Configure Alerts (20 min)

```yaml
# alerting_rules.yml (Prometheus format)
groups:
  - name: service_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(requests_total{status=~"5.."}[5m]) / rate(requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }}"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency detected"
          description: "95th percentile latency is {{ $value }}s"

      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service is down"
```

### 7. Document Runbook (20 min)

```markdown
# Service Runbook

## Alert: HighErrorRate

### Symptoms
- Error rate > 5% for 5+ minutes
- User-facing errors reported

### Investigation Steps
1. Check logs: `kubectl logs -l app=my-service --since=10m | grep ERROR`
2. Check downstream dependencies
3. Review recent deployments

### Resolution
- If dependency issue: Check dependency status, consider circuit breaker
- If code issue: Rollback latest deployment
- If data issue: Review recent input patterns

### Escalation
- Page on-call if not resolved in 15 minutes
```

## Artifacts

| Artifact | Description |
|----------|-------------|
| `logging_config.py` | Structured logging setup |
| `metrics.py` | Prometheus metrics |
| `dashboard.json` | Grafana dashboard |
| `alerting_rules.yml` | Alert definitions |
| `runbook.md` | Incident response guide |

## Quality Bar

- [ ] Four golden signals instrumented
- [ ] Structured logging with request IDs
- [ ] Dashboard showing key metrics
- [ ] At least 3 alerts configured
- [ ] Runbook for each alert
- [ ] Tested alerting actually fires

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 4-6 hours |
| Practiced | 2-3 hours |
| Expert | 1-2 hours |

## Common Pitfalls

- Too many metrics (start with golden signals)
- Alert fatigue (too many alerts)
- Missing request correlation
- No runbooks for alerts
- Not testing alerting
