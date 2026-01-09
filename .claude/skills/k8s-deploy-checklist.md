# Skill: Kubernetes Deploy Checklist

Deploy services to Kubernetes with production-grade configuration.

> **Level**: Advanced only. Intermediate learners should use simpler deployment options (Docker Compose, Cloud Run, etc.) until comfortable with container orchestration concepts.

## Trigger

Use this skill when:
- Deploying to Kubernetes clusters
- Need auto-scaling and high availability
- Managing multiple microservices
- Production-grade container orchestration required

## Prerequisites

- [ ] Docker image built and pushed to registry
- [ ] `kubectl` configured with cluster access
- [ ] Namespace created for your service
- [ ] Container registry credentials configured
- [ ] Comfortable with Docker and basic K8s concepts

## Steps

### 1. Create Deployment (30 min)

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-service
  labels:
    app: my-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-service
  template:
    metadata:
      labels:
        app: my-service
    spec:
      containers:
        - name: my-service
          image: gcr.io/project/my-service:v1.0.0
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
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: my-service-secrets
                  key: api-key
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 5
```

### 2. Create Service (10 min)

```yaml
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-service
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: ClusterIP
```

### 3. Create ConfigMap (10 min)

```yaml
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-service-config
data:
  LOG_LEVEL: "INFO"
  MAX_CONNECTIONS: "100"
  TIMEOUT_SECONDS: "30"
```

### 4. Create Secrets (10 min)

```bash
# Create secret from literal
kubectl create secret generic my-service-secrets \
  --from-literal=api-key='your-secret-key' \
  --dry-run=client -o yaml > k8s/secret.yaml

# Or from file
kubectl create secret generic my-service-secrets \
  --from-file=credentials.json \
  --dry-run=client -o yaml > k8s/secret.yaml
```

> **Important**: Never commit actual secrets to git. Use sealed-secrets, external-secrets, or similar.

### 5. Configure Ingress (20 min)

```yaml
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-service-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
    - hosts:
        - api.example.com
      secretName: my-service-tls
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-service
                port:
                  number: 80
```

### 6. Set Up HPA (15 min)

```yaml
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-service-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-service
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

### 7. Deploy (15 min)

```bash
# Apply all configurations
kubectl apply -f k8s/

# Watch rollout
kubectl rollout status deployment/my-service

# Verify pods
kubectl get pods -l app=my-service

# Check logs
kubectl logs -l app=my-service --tail=100

# Test service
kubectl port-forward svc/my-service 8080:80
curl http://localhost:8080/health
```

### 8. Production Checklist

#### Security
- [ ] Pod security context configured
- [ ] Network policies defined
- [ ] Secrets not in git
- [ ] RBAC configured
- [ ] Image from trusted registry
- [ ] No privileged containers

#### Reliability
- [ ] Resource requests and limits set
- [ ] Liveness and readiness probes
- [ ] Multiple replicas
- [ ] Pod disruption budget
- [ ] Graceful shutdown handling

#### Observability
- [ ] Prometheus scrape annotations
- [ ] Structured logging
- [ ] Distributed tracing
- [ ] Log aggregation configured

#### Networking
- [ ] Service mesh (if applicable)
- [ ] TLS termination
- [ ] Rate limiting
- [ ] Circuit breakers

### 9. Useful Commands

```bash
# Debug pod issues
kubectl describe pod <pod-name>
kubectl logs <pod-name> --previous

# Scale manually
kubectl scale deployment my-service --replicas=3

# Rollback
kubectl rollout undo deployment/my-service

# Execute into pod
kubectl exec -it <pod-name> -- /bin/sh

# Check resource usage
kubectl top pods -l app=my-service
```

## Artifacts

| Artifact | Description |
|----------|-------------|
| `k8s/deployment.yaml` | Deployment configuration |
| `k8s/service.yaml` | Service configuration |
| `k8s/configmap.yaml` | Configuration data |
| `k8s/ingress.yaml` | Ingress rules |
| `k8s/hpa.yaml` | Auto-scaling rules |

## Quality Bar

- [ ] All pods healthy and ready
- [ ] Probes configured and working
- [ ] Resource limits appropriate
- [ ] HPA tested under load
- [ ] Rollback procedure verified
- [ ] Secrets managed securely

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 4-6 hours |
| Practiced | 2-3 hours |
| Expert | 1 hour |

## Common Pitfalls

- Resource limits too tight (OOMKilled)
- Missing readiness probes (premature traffic)
- Secrets in git
- No pod disruption budget
- Ignoring resource requests
- Not testing rollback
