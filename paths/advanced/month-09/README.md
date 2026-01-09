# Month 09: Kubernetes & Container Orchestration

## Why It Matters

Kubernetes is the industry standard for container orchestration. This month teaches you to deploy, scale, and manage ML workloads on Kubernetes—essential for large-scale ML systems.

**Job Relevance**: K8s skills are required for senior ML/Platform Engineer roles. Companies running ML at scale use Kubernetes.

---

## Prerequisites

- Month 01-08 completed
- Docker mastery
- Cloud fundamentals
- Networking basics

---

## Learning Goals

### Tier 2 Focus (Consolidation)
- Docker Compose for local dev
- Container best practices

### Tier 3 Focus
- Kubernetes architecture
- Pods, Deployments, Services
- ConfigMaps and Secrets
- Horizontal Pod Autoscaling
- AKS/EKS/GKE managed Kubernetes
- Kubeflow for ML workloads

---

## Main Project: ML Platform on Kubernetes

Build an ML platform on Kubernetes that:
1. Deploys model serving pods
2. Auto-scales based on traffic
3. Handles rolling updates
4. Uses ConfigMaps for configuration
5. Implements health checks
6. Runs on managed Kubernetes

### Deliverables

1. **`k8s/`** - Kubernetes manifests
2. **`helm/`** - Helm charts (optional)
3. **`serving/`** - Model serving code
4. **`scripts/`** - Deployment scripts
5. **`monitoring/`** - K8s monitoring setup
6. **`docs/`** - Runbooks and architecture

### Definition of Done

- [ ] Model serving deployment works
- [ ] Service exposes predictions
- [ ] HPA configured and tested
- [ ] Rolling updates work
- [ ] Health checks passing
- [ ] Runbook documented
- [ ] Deployed on managed K8s (AKS/EKS/GKE)

---

## Week-by-Week Plan

### Week 1: Kubernetes Fundamentals

**Focus**: Understand K8s concepts.

- Kubernetes architecture
- kubectl basics
- Pods and containers
- ReplicaSets and Deployments
- Services and networking
- Local Kubernetes (minikube/kind)

**Milestone**: Application running on local Kubernetes.

### Week 2: Configuration & Secrets

**Focus**: Manage application config.

- ConfigMaps
- Secrets management
- Environment variables
- Volume mounts
- Namespaces

**Milestone**: Configurable deployment with secrets.

### Week 3: Scaling & Production

**Focus**: Production patterns.

- Horizontal Pod Autoscaler
- Resource requests and limits
- Health probes (liveness, readiness)
- Rolling updates
- Ingress controllers

**Milestone**: Auto-scaling deployment with health checks.

### Week 4: Managed Kubernetes & ML

**Focus**: Cloud Kubernetes and ML workloads.

- AKS/EKS/GKE setup
- Kubeflow introduction
- GPU workloads
- Cost optimization
- Monitoring on K8s

**Milestone**: ML workload on managed Kubernetes.

---

## Stretch Goals

- Implement Kubeflow pipeline
- Add service mesh (Istio)
- Set up GitOps (ArgoCD)
- Build custom K8s operator
- Implement blue-green deployments

---

## Claude Prompts

### Planning
```
/plan-week
```

### K8s Deployment
```
Use the K8s Deploy Checklist skill for my model serving deployment.
```

### Architecture Help
```
As the Researcher, explain Kubernetes networking for ML services.
```

### Troubleshooting
```
/debug-learning

My pods keep crashing. Here's the error log...
```

### Review
```
/harden

Review my Kubernetes manifests for best practices.
```

---

## How to Publish

### Demo Script
```bash
# Deploy to Kubernetes
kubectl apply -f k8s/

# Watch pods come up
kubectl get pods -w

# Test the service
kubectl port-forward svc/model-serving 8000:80
curl http://localhost:8000/predict

# Scale up
kubectl scale deployment model-serving --replicas=5

# Watch HPA
kubectl get hpa -w
```

### Write-Up Topics
- Kubernetes for ML workloads
- Scaling ML services automatically
- Configuration management in K8s
- From Docker to Kubernetes journey

---

## Resources

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubeflow](https://www.kubeflow.org/)
- [AKS Docs](https://docs.microsoft.com/azure/aks/)
- [EKS Docs](https://docs.aws.amazon.com/eks/)
- Skill: `.claude/skills/k8s-deploy-checklist.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 9
```
