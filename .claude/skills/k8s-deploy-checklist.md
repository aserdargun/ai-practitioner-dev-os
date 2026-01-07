# Skill: Kubernetes Deploy Checklist

**Tier**: 3 (Advanced)

> ⚠️ **Note**: This skill is for Advanced learners only. Beginners and Intermediates should focus on simpler deployment methods (Docker, cloud-managed services) first.

Deploy your application to Kubernetes with production-ready configurations.

---

## Trigger

Use this skill when:
- Need container orchestration
- Deploying to production at scale
- Require auto-scaling and self-healing

## Prerequisites

- [ ] Application containerized (Docker)
- [ ] Kubernetes cluster available (local or cloud)
- [ ] kubectl configured
- [ ] Basic K8s concepts understood

## Steps

### Step 1: Create Deployment Manifest (15 min)

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-api
  labels:
    app: my-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-api
  template:
    metadata:
      labels:
        app: my-api
    spec:
      containers:
      - name: my-api
        image: my-registry/my-api:v1.0.0
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "256Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        env:
        - name: LOG_LEVEL
          value: "INFO"
        - name: MODEL_PATH
          value: "/models/model.joblib"
        volumeMounts:
        - name: model-storage
          mountPath: /models
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-pvc
```

**Checkpoint**: Deployment manifest created.

### Step 2: Add Health Probes (10 min)

```yaml
# Add to container spec in deployment.yaml
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 10
          failureThreshold: 3

        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
          failureThreshold: 3

        startupProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
          failureThreshold: 30
```

**Checkpoint**: Health probes configured.

### Step 3: Create Service (5 min)

```yaml
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-api-service
spec:
  selector:
    app: my-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: ClusterIP
```

**Checkpoint**: Service created.

### Step 4: Configure Ingress (10 min)

```yaml
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-api-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-api-service
            port:
              number: 80
```

**Checkpoint**: Ingress configured.

### Step 5: Add ConfigMap and Secrets (10 min)

```yaml
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-api-config
data:
  LOG_LEVEL: "INFO"
  MODEL_VERSION: "v1.0.0"
```

```yaml
# k8s/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-api-secrets
type: Opaque
stringData:
  API_KEY: "your-secret-key"  # Use kubectl create secret in production
```

```yaml
# Update deployment to use ConfigMap and Secret
        envFrom:
        - configMapRef:
            name: my-api-config
        - secretRef:
            name: my-api-secrets
```

**Checkpoint**: Configuration externalized.

### Step 6: Set Up Horizontal Pod Autoscaler (10 min)

```yaml
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

**Checkpoint**: Auto-scaling configured.

### Step 7: Deploy and Verify (15 min)

```bash
# Apply all manifests
kubectl apply -f k8s/

# Check deployment status
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress

# Check pod logs
kubectl logs -l app=my-api --tail=100

# Check pod health
kubectl describe pod <pod-name>

# Test the service
kubectl port-forward service/my-api-service 8080:80
curl http://localhost:8080/health
```

**Checkpoint**: Application deployed and healthy.

### Step 8: Document Deployment (10 min)

```markdown
## Kubernetes Deployment: my-api

### Architecture
- Deployment: 2-10 replicas (auto-scaled)
- Service: ClusterIP on port 80
- Ingress: api.example.com

### Manifests
- `k8s/deployment.yaml` - Main deployment
- `k8s/service.yaml` - Service definition
- `k8s/ingress.yaml` - Ingress rules
- `k8s/configmap.yaml` - Configuration
- `k8s/secret.yaml` - Secrets (template)
- `k8s/hpa.yaml` - Auto-scaling

### Deployment Commands
```bash
# Deploy
kubectl apply -f k8s/

# Check status
kubectl get all -l app=my-api

# View logs
kubectl logs -l app=my-api -f

# Rollback
kubectl rollout undo deployment/my-api
```

### Monitoring
- Health: /health endpoint
- Metrics: /metrics endpoint (Prometheus)
- Logs: kubectl logs or centralized logging

### Troubleshooting
1. Pods not starting: Check `kubectl describe pod`
2. Health check failing: Check application logs
3. High latency: Check resource limits and HPA
```

**Checkpoint**: Deployment documented.

## Artifacts Produced

- [ ] Deployment manifest
- [ ] Service manifest
- [ ] Ingress manifest
- [ ] ConfigMap and Secrets
- [ ] HPA configuration
- [ ] Deployment documentation

## Quality Bar

✅ **Done when**:
- Pods running and healthy
- Service accessible
- Auto-scaling working
- Secrets not in code
- Rollback tested
- Documentation complete

## Pre-Deploy Checklist

- [ ] Image tagged with version (not :latest)
- [ ] Resource limits set
- [ ] Health probes configured
- [ ] Secrets in Secret objects
- [ ] HPA configured
- [ ] Ingress TLS configured (production)
- [ ] Pod disruption budget set (production)

## Example Prompt

```
I have a FastAPI prediction service in a Docker container.
Help me deploy it to Kubernetes with:

1. 2 replicas minimum
2. Auto-scaling based on CPU
3. Health checks
4. External access via ingress

The image is at my-registry/my-api:v1.0.0
```

## Related Skills

- [API Shipping Checklist](api-shipping-checklist.md) - Containerize first
- [Observability Starter](observability-starter.md) - Add monitoring
