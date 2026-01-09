# Month 10: Building Web APIs

**Theme**: Learn to serve your ML models via web APIs.

## Why It Matters

A model in a notebook doesn't create value. APIs make models usable by applications, other services, and end-users. This is how ML goes from experiment to product.

## Prerequisites

- Month 5-6 completed (have models to serve)
- Python function writing
- Basic HTTP understanding

## Learning Goals

### API Fundamentals (Week 1)
- [ ] HTTP basics (methods, status codes)
- [ ] REST principles
- [ ] JSON data format
- [ ] API design basics
- [ ] Request/response lifecycle

### Flask & FastAPI (Week 2-3)
- [ ] Flask basics
- [ ] FastAPI introduction (recommended)
- [ ] Routing and endpoints
- [ ] Request validation
- [ ] Error handling
- [ ] Testing APIs

### Production Concerns (Week 4)
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Environment configuration
- [ ] Basic logging
- [ ] Health checks
- [ ] Deployment basics (Docker intro)

## Main Project: ML Model API

Deploy one of your ML models as a REST API.

### Choose a Model
Use your best model from previous months:
- House price predictor (Month 5)
- Churn classifier (Month 6)
- Sentiment analyzer (Month 8)

### Deliverables
1. REST API with endpoints:
   - `GET /health` — Health check
   - `POST /predict` — Make prediction
   - `GET /docs` — API documentation

2. Supporting files:
   - Dockerfile
   - Requirements file
   - README with usage

3. Test suite:
   - Unit tests for prediction
   - API integration tests

### Definition of Done
- [ ] API runs locally
- [ ] /predict returns valid predictions
- [ ] Input validation works
- [ ] Errors handled gracefully
- [ ] Tests pass
- [ ] Documentation accessible

## Stretch Goals

- [ ] Add batch prediction endpoint
- [ ] Implement rate limiting
- [ ] Add authentication
- [ ] Deploy to cloud (free tier)
- [ ] Add model versioning

## Weekly Breakdown

### Week 1: API Fundamentals
- HTTP and REST concepts
- JSON handling
- First Flask "Hello World"
- Simple endpoints

### Week 2: Building the API
- Load saved model
- Create prediction endpoint
- Input validation
- Error handling

### Week 3: Testing & Docs
- Write tests
- Add documentation
- Logging basics
- Docker introduction

### Week 4: Polish & Ship
- Dockerfile
- Final testing
- Documentation
- Demo prep

## Claude Prompts

### Planning
```
/plan-week
Month 10 Week 2 - Focus on building the prediction API
I'm using FastAPI with my churn model
```

### Skill Guidance
```
Guide me through the API Shipping Checklist skill
for my model deployment.
```

### Building
```
Ask the Builder to help me create a FastAPI
endpoint that accepts features as JSON and
returns predictions with confidence scores.
```

### Review
```
Ask the Reviewer to review my API code.
Check for security issues, error handling,
and best practices.
```

## How to Publish

### Demo
1. Show API running locally
2. Demonstrate /health endpoint
3. Make predictions via curl
4. Show error handling
5. Tour the documentation

### Write-up Topics
- Why APIs matter for ML
- FastAPI vs Flask decision
- Validation and error handling
- Docker basics learned

### Portfolio Entry
- GitHub with clean code
- README with curl examples
- Docker instructions

## Resources

### FastAPI
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

### Flask
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### APIs
- [REST API Tutorial](https://restfulapi.net/)
- [HTTP Status Codes](https://httpstatuses.com/)

### Docker
- [Docker Getting Started](https://docs.docker.com/get-started/)

## Tips

1. **Start with FastAPI** — Modern, fast, auto-docs
2. **Validate everything** — Never trust input
3. **Return useful errors** — Help API users debug
4. **Test with curl first** — Simple and reliable
5. **Document as you build** — FastAPI does this automatically
