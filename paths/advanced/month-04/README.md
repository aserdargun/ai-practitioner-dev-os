# Month 04: APIs & Microservices

## Why It Matters

Models without APIs are just notebooks. This month teaches you to ship ML models as production-ready services that other systems can consume.

**Job Relevance**: ML Engineers must deploy models. Companies need practitioners who can build reliable, scalable APIs.

---

## Prerequisites

- Month 01-03 completed
- Python proficiency
- Docker basics from Month 01

---

## Learning Goals

### Tier 1 Focus
- RESTful API design principles
- Flask basics
- Django overview
- HTTP methods and status codes
- API documentation

### Tier 2 Focus
- FastAPI for modern async APIs
- Docker for containerization
- Request validation with Pydantic
- Authentication basics
- API testing strategies
- GitHub Actions CI/CD

### Tier 3 Preview
- Kubernetes introduction
- API Gateway patterns
- Service mesh concepts

---

## Main Project: ML Prediction API

Build a production-ready API that:
1. Serves ML model predictions
2. Validates inputs with Pydantic
3. Handles errors gracefully
4. Includes health checks
5. Has comprehensive tests
6. Runs in Docker
7. Deploys via CI/CD

### Deliverables

1. **`app/`** - FastAPI application
2. **`models/`** - Saved ML model
3. **`tests/`** - API tests
4. **`Dockerfile`** - Container definition
5. **`.github/workflows/`** - CI/CD pipeline
6. **`docs/`** - API documentation

### Definition of Done

- [ ] POST endpoint for predictions
- [ ] GET endpoint for health check
- [ ] Input validation with Pydantic
- [ ] Error handling with proper status codes
- [ ] At least 10 API tests
- [ ] Docker container works
- [ ] CI pipeline passes

---

## Week-by-Week Plan

### Week 1: FastAPI Fundamentals

**Focus**: Build your first API.

- FastAPI basics
- Path and query parameters
- Request body with Pydantic
- Response models
- OpenAPI documentation

**Milestone**: Basic CRUD API working.

### Week 2: ML Model Integration

**Focus**: Serve your model.

- Loading ML models
- Prediction endpoints
- Input preprocessing
- Output formatting
- Batch predictions

**Milestone**: Model serving with /predict endpoint.

### Week 3: Production Hardening

**Focus**: Make it production-ready.

- Error handling
- Logging and monitoring
- Health and readiness checks
- Authentication basics
- Rate limiting

**Milestone**: Production-grade API with observability.

### Week 4: Docker & CI/CD

**Focus**: Ship it.

- Dockerfile optimization
- Docker Compose for local dev
- GitHub Actions pipeline
- Testing in CI
- Documentation

**Milestone**: Containerized API with passing CI.

---

## Stretch Goals

- Add async database operations
- Implement API versioning
- Add request/response logging
- Build admin dashboard
- Add caching with Redis

---

## Claude Prompts

### Planning
```
/plan-week
```

### API Design
```
As the Researcher, what are FastAPI best practices for ML serving?
```

### Skill Application
```
Use the API Shipping Checklist skill for my prediction API.
```

### Security Review
```
/harden

Review my API for security issues and best practices.
```

### Pre-Deploy
```
/publish

Prepare my API for deployment.
```

---

## How to Publish

### Demo Script
```bash
# Start the API
uvicorn app.main:app --host 0.0.0.0 --port 8000

# In another terminal
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0]}'
```

### Write-Up Topics
- Building ML APIs with FastAPI
- Pydantic for data validation
- Docker best practices
- CI/CD for ML services

---

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- Template: `templates/template-fastapi-service/`
- Skill: `.claude/skills/api-shipping-checklist.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 4
```
