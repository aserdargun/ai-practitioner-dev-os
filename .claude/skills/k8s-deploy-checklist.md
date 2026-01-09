# Skill: K8s Deploy Checklist

Deploy application to Kubernetes (Advanced tier).

> **Note**: This skill is gated to **Advanced** learners. Beginners and Intermediates should use simpler deployment methods (Docker, Cloud Run, etc.) first.

## Trigger

Use this skill when:
- Deploying to Kubernetes cluster
- Need auto-scaling and high availability
- Running multiple services that need to communicate
- Production deployment requiring orchestration

## Prerequisites

- Working Docker container
- Kubernetes cluster access (local: minikube, kind; cloud: GKE, EKS, AKS)
- kubectl installed and configured
- Basic understanding of Kubernetes concepts

## Steps

### 1. Verify Container Works (10 min)

```bash
# Test locally first
docker build -t myapp:v1 .
docker run -p 8000:8000 myapp:v1

# Test endpoints
curl http://localhost:8000/health
```

### 2. Create Deployment Manifest (20 min)

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prediction-api
  labels:
    app: prediction-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: prediction-api
  template:
    metadata:
      labels:
        app: prediction-api
    spec:
      containers:
      - name: prediction-api
        image: myregistry/prediction-api:v1
        ports:
        - containerPort: 8000

        # Resource limits
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"

        # Health checks
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 10

        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5

        # Environment variables
        env:
        - name: LOG_LEVEL
          value: "INFO"
        - name: MODEL_PATH
          value: "/app/models/model.pkl"

        # Secrets from ConfigMap/Secret
        envFrom:
        - configMapRef:
            name: prediction-api-config
        - secretRef:
            name: prediction-api-secrets
```

### 3. Create Service (10 min)

```yaml
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: prediction-api
spec:
  selector:
    app: prediction-api
  ports:
  - port: 80
    targetPort: 8000
  type: ClusterIP
```

### 4. Create ConfigMap and Secrets (10 min)

```yaml
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prediction-api-config
data:
  LOG_LEVEL: "INFO"
  METRICS_ENABLED: "true"
```

```bash
# Create secret (don't commit to git!)
kubectl create secret generic prediction-api-secrets \
  --from-literal=API_KEY=your-secret-key
```

### 5. Create Ingress (Optional, 15 min)

```yaml
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: prediction-api
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: prediction-api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: prediction-api
            port:
              number: 80
```

### 6. Create HorizontalPodAutoscaler (10 min)

```yaml
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: prediction-api
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: prediction-api
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

### 7. Deploy (15 min)

```bash
# Apply manifests
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
# kubectl apply -f k8s/ingress.yaml  # if using ingress

# Watch deployment
kubectl rollout status deployment/prediction-api

# Check pods
kubectl get pods -l app=prediction-api

# Check service
kubectl get svc prediction-api
```

### 8. Verify Deployment (10 min)

```bash
# Port forward for local testing
kubectl port-forward svc/prediction-api 8000:80

# Test endpoints
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1,2,3,4,5,6,7,8,9,10]}'

# Check logs
kubectl logs -l app=prediction-api --tail=50

# Check resource usage
kubectl top pods -l app=prediction-api
```

### 9. Pre-Production Checklist

```markdown
## K8s Deploy Checklist

### Container
- [ ] Image pushed to registry
- [ ] Image tagged with version (not just :latest)
- [ ] Container runs locally
- [ ] Health endpoints work

### Deployment
- [ ] Resource requests and limits set
- [ ] Liveness probe configured
- [ ] Readiness probe configured
- [ ] Replicas >= 2 for availability
- [ ] Rolling update strategy (default)

### Service
- [ ] Service exposes correct port
- [ ] Service selector matches pod labels

### Configuration
- [ ] ConfigMap for non-sensitive config
- [ ] Secrets for sensitive data
- [ ] Secrets NOT in git

### Scaling
- [ ] HPA configured
- [ ] Min replicas >= 2
- [ ] Max replicas reasonable
- [ ] Metrics server running

### Networking
- [ ] Ingress configured (if external access needed)
- [ ] TLS configured (production)
- [ ] Network policies (if required)

### Observability
- [ ] Logs accessible via kubectl
- [ ] Metrics exposed
- [ ] Monitoring dashboards
```

## Artifacts Produced

- [ ] `k8s/deployment.yaml`
- [ ] `k8s/service.yaml`
- [ ] `k8s/configmap.yaml`
- [ ] `k8s/hpa.yaml`
- [ ] `k8s/ingress.yaml` (optional)
- [ ] Deployment verification commands

## Quality Bar

- [ ] Zero-downtime deployment works
- [ ] Pods restart on failure (liveness probe)
- [ ] Traffic only hits ready pods (readiness probe)
- [ ] Auto-scaling triggers under load
- [ ] Logs accessible
- [ ] Rollback tested

## Common Pitfalls

1. **No resource limits**
   - Pods can consume entire node

2. **Missing health probes**
   - Bad pods keep receiving traffic

3. **Secrets in ConfigMaps**
   - Use Secrets for sensitive data

4. **:latest tag**
   - Can't rollback; use version tags

5. **Single replica**
   - No availability during updates/failures

## Simpler Alternatives

If K8s feels complex, consider:
- **Docker Compose**: For local/small deployments
- **Cloud Run**: Serverless containers
- **AWS App Runner**: Managed container deployment
- **Heroku**: Platform-as-a-Service
