# Skill: Kubernetes Deploy Checklist

## Trigger

Use this skill when deploying a service to Kubernetes.

## Prerequisites

- Docker image built and pushed to registry
- kubectl configured for your cluster
- Basic understanding of K8s concepts

**Level**: ⚠️ **Advanced only** (Tier 3)

This skill requires:
- Understanding of containers and Docker
- Basic networking concepts
- Familiarity with YAML configuration

## Pre-Deployment Checklist

### 1. Container Ready ✅

- [ ] Dockerfile uses multi-stage builds (smaller images)
- [ ] Non-root user in container
- [ ] Health check configured in Dockerfile
- [ ] Image tagged with version (not just `latest`)
- [ ] Image pushed to registry

```dockerfile
# Example: Production Dockerfile
FROM python:3.11-slim as builder
WORKDIR /app
COPY pyproject.toml .
RUN pip wheel --no-deps --wheel-dir /wheels .

FROM python:3.11-slim
RUN useradd --create-home appuser
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*.whl
COPY app/ app/
USER appuser
EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. Kubernetes Manifests ✅

#### Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry/myapp:v1.0.0
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "256Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: myapp-secrets
              key: database-url
```

#### Service

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8000
  type: ClusterIP
```

#### ConfigMap & Secret

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
data:
  LOG_LEVEL: "INFO"
  FEATURE_FLAG: "true"

---
# secret.yaml (apply separately, don't commit!)
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secrets
type: Opaque
stringData:
  database-url: "postgresql://user:pass@host:5432/db"
```

### 3. Resource Configuration ✅

| Resource | Request | Limit | Notes |
|----------|---------|-------|-------|
| Memory | 256Mi | 512Mi | Set based on profiling |
| CPU | 100m | 500m | 100m = 0.1 core |

**Guidelines**:
- Requests = guaranteed resources
- Limits = maximum allowed
- Start conservative, adjust based on metrics

### 4. Health Probes ✅

| Probe | Purpose | Path | Timing |
|-------|---------|------|--------|
| Liveness | Is container alive? | `/health` | initialDelay: 10s, period: 10s |
| Readiness | Can handle traffic? | `/ready` | initialDelay: 5s, period: 5s |
| Startup | Still starting up? | `/health` | failureThreshold: 30 |

### 5. Scaling Configuration ✅

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### 6. Ingress (if needed) ✅

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - api.example.com
    secretName: myapp-tls
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp
            port:
              number: 80
```

## Deployment Steps

### 1. Pre-flight Checks

```bash
# Verify cluster access
kubectl cluster-info

# Check current state
kubectl get pods -n myapp-ns

# Validate manifests
kubectl apply --dry-run=client -f deployment.yaml
```

### 2. Deploy

```bash
# Create namespace (if new)
kubectl create namespace myapp-ns

# Apply secrets first
kubectl apply -f secret.yaml -n myapp-ns

# Apply configs
kubectl apply -f configmap.yaml -n myapp-ns

# Deploy application
kubectl apply -f deployment.yaml -n myapp-ns
kubectl apply -f service.yaml -n myapp-ns

# Wait for rollout
kubectl rollout status deployment/myapp -n myapp-ns
```

### 3. Verify

```bash
# Check pods
kubectl get pods -n myapp-ns

# Check logs
kubectl logs -f deployment/myapp -n myapp-ns

# Check events
kubectl get events -n myapp-ns --sort-by='.lastTimestamp'

# Test service
kubectl port-forward svc/myapp 8080:80 -n myapp-ns
curl http://localhost:8080/health
```

### 4. Rollback (if needed)

```bash
# Check rollout history
kubectl rollout history deployment/myapp -n myapp-ns

# Rollback to previous
kubectl rollout undo deployment/myapp -n myapp-ns

# Rollback to specific revision
kubectl rollout undo deployment/myapp --to-revision=2 -n myapp-ns
```

## Post-Deployment ✅

- [ ] All pods running
- [ ] Health checks passing
- [ ] Logs look normal
- [ ] Metrics flowing
- [ ] External access working (if applicable)
- [ ] Alerts configured

## Artifacts Produced

- `k8s/deployment.yaml`
- `k8s/service.yaml`
- `k8s/configmap.yaml`
- `k8s/hpa.yaml` (optional)
- `k8s/ingress.yaml` (optional)
- Deployment runbook

## Quality Bar

- [ ] Non-root container user
- [ ] Resource limits set
- [ ] Health probes configured
- [ ] Secrets not in manifests
- [ ] Rollback tested

## Common Pitfalls

1. **No resource limits** - Pods can starve others
2. **Missing probes** - K8s can't manage health
3. **Secrets in YAML** - Use sealed-secrets or external secret managers
4. **`latest` tag** - Use specific versions
5. **No rollback plan** - Always know how to undo
