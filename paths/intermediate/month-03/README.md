# Month 03: Production APIs

**Focus**: Deploy ML models as production-ready APIs with FastAPI.

---

## Why It Matters

A model that isn't deployed has no impact. Learning to package and serve models via APIs is essential for ML engineers. This month bridges the gap between notebooks and production systems.

**Job Relevance**: Critical for ML engineering roles; differentiates from pure data science.

---

## Prerequisites

- Month 01-02 complete
- Basic understanding of HTTP/REST
- Docker basics (will learn more this month)

---

## Learning Goals

**Tier 1 Technologies**:
- RESTful APIs
- Flask/Django basics

**Tier 2 Technologies**:
- FastAPI (primary focus)
- Docker (containerization)
- GitHub Actions (CI/CD)
- PostgreSQL (database basics)

**Skills**:
- API design and implementation
- Request/response modeling
- Containerization
- Basic CI/CD

---

## Main Project: ML Model API Service

Deploy a trained model as a production-ready API service.

### Deliverables

1. **FastAPI Service** serving model predictions
2. **Docker Container** with the service
3. **Test Suite** for API endpoints
4. **CI Pipeline** running tests on push
5. **GitHub Repository** with documentation

### Definition of Done

- [ ] FastAPI service with /predict endpoint
- [ ] Pydantic models for request/response
- [ ] Health check endpoint
- [ ] Input validation implemented
- [ ] Error handling in place
- [ ] Tests for all endpoints
- [ ] Dockerfile created
- [ ] Container builds and runs
- [ ] GitHub Actions workflow passing
- [ ] README with setup instructions

---

## Stretch Goals

- [ ] Add authentication
- [ ] Implement rate limiting
- [ ] Add batch prediction endpoint
- [ ] Deploy to cloud (Render, Railway, etc.)

---

## Weekly Cadence

### Week 1: FastAPI Basics
- Set up FastAPI project
- Create basic endpoints
- Add Pydantic models
- Load model for predictions

### Week 2: Build Full API
- Implement /predict endpoint
- Add error handling
- Write tests
- Add health check

### Week 3: Containerize & CI
- Create Dockerfile
- Set up GitHub Actions
- Configure test pipeline
- Debug and fix issues

### Week 4: Ship & Document
- Finalize documentation
- Create API examples
- Demo preparation
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 3 on production APIs. I have my model from Month 2.
Help me plan the FastAPI service implementation.
```

### Building
```
/ship-mvp

My FastAPI service has:
- /health endpoint
- /predict endpoint
- Pydantic models
What's missing for MVP?
```

### Review
```
/harden

Review my API implementation for:
- Security (input validation)
- Error handling
- Test coverage
- Documentation
```

### Skill Application
```
Apply the API Shipping Checklist skill to my project.
I want to make sure I haven't missed anything.
```

---

## How to Publish

### Demo
- Show API in action (curl/Postman)
- Demonstrate Docker build and run
- Show GitHub Actions passing

### Write-up
- "From Notebook to API: Deploying My First ML Model"
- Include architecture diagram
- Share code snippets for key patterns

---

## Resources

### Templates
- [FastAPI Template](../../../templates/template-fastapi-service/)

### Skill Playbooks
- [API Shipping Checklist](../../../.claude/skills/api-shipping-checklist.md)

### Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## Next Month Preview

**Month 04**: Deep Learning — Build neural networks with PyTorch.
