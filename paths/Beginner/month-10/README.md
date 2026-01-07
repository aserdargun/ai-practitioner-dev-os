# Month 10: Web Development for ML

**Focus**: Build and deploy ML models as web services

---

## Why It Matters

Models only create value when deployed. This month you'll learn:
- Building REST APIs with Flask
- Exposing ML models as services
- Basic deployment practices
- Frontend basics for demos

Employers want practitioners who can ship, not just build notebooks.

---

## Prerequisites

- Months 1-9 completed
- At least one trained model
- Python proficiency

---

## Learning Goals

By the end of this month, you will:

1. **Flask Basics**
   - [ ] Routes and views
   - [ ] Request/response handling
   - [ ] Templates (Jinja2)
   - [ ] Static files

2. **REST APIs**
   - [ ] HTTP methods (GET, POST)
   - [ ] JSON request/response
   - [ ] Error handling
   - [ ] Input validation

3. **ML Deployment**
   - [ ] Loading trained models
   - [ ] Making predictions via API
   - [ ] Batch vs real-time inference
   - [ ] Model versioning basics

4. **Deployment**
   - [ ] Docker basics
   - [ ] Environment variables
   - [ ] Health checks
   - [ ] Logging

---

## Main Project: ML Model API

Deploy one of your trained models as a production-ready API.

### Deliverables

1. **Flask Application** (`app/`)
   - `main.py` - Application entry
   - `routes.py` - API endpoints
   - `model.py` - Model loading and inference
   - `templates/` - Demo UI (optional)

2. **Docker Setup**
   - `Dockerfile`
   - `docker-compose.yml` (optional)
   - `requirements.txt`

3. **Documentation**
   - API documentation
   - Setup instructions
   - Example requests

4. **Tests**
   - Endpoint tests
   - Model inference tests

### Definition of Done

- [ ] Health endpoint returns 200
- [ ] Prediction endpoint works correctly
- [ ] Input validation in place
- [ ] Errors handled gracefully
- [ ] Docker builds and runs
- [ ] Documentation complete
- [ ] Tests pass

### API Endpoints

```
GET  /health          - Health check
GET  /model/info      - Model metadata
POST /predict         - Make prediction
POST /predict/batch   - Batch predictions (stretch)
```

---

## Stretch Goals

- [ ] Add authentication
- [ ] Implement rate limiting
- [ ] Create Swagger documentation
- [ ] Deploy to cloud (Heroku/Railway)

---

## Weekly Breakdown

### Week 1: Flask Fundamentals
- Flask setup and routing
- Request handling
- JSON responses
- Error handling

### Week 2: API Development
- REST API design
- Input validation
- Loading ML models
- Prediction endpoints

### Week 3: Docker & Deployment
- Docker basics
- Building images
- Environment configuration
- Health checks

### Week 4: Polish & Document
- Testing
- Documentation
- Demo UI
- Final deployment

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 10: Web Development.
I want to deploy my [model type] model as an API.
Help me plan the project.
```

### Skill Application
```
I want to apply the API Shipping skill.
Walk me through .claude/skills/api-shipping-checklist.md
for my trained model.
```

### Flask Help
```
I'm building a Flask endpoint that [description].
Show me:
- The route decorator
- Request handling
- Response format
- Error handling
```

### Model Integration
```
My model expects:
- Input: [describe input format]
- Output: [describe output]

How do I:
1. Accept this via POST request
2. Preprocess the input
3. Run inference
4. Return the result as JSON
```

### Docker Setup
```
I have a Flask app with:
- main.py as entry point
- requirements.txt for dependencies
- models/ directory with model files

Create a Dockerfile and explain each line.
```

### Testing APIs
```
Show me how to test my Flask API:
- Using pytest
- Testing the health endpoint
- Testing predictions
- Testing error cases
```

---

## How to Publish

### Demo

Show your deployed API:
1. API documentation
2. Making requests (curl or UI)
3. Response handling
4. Error cases

### Write-up

Cover:
- Why deployment matters
- API design decisions
- Docker experience
- Lessons learned

### Portfolio

- Live API endpoint (if deployed)
- GitHub repo with docs
- Demo video/screenshots

---

## Resources

### Flask
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Docker
- [Docker Getting Started](https://docs.docker.com/get-started/)
- [Docker for ML](https://docs.docker.com/language/python/)

### APIs
- [REST API Design Guide](https://restfulapi.net/)
- [FastAPI](https://fastapi.tiangolo.com/) (alternative to Flask)

---

## Next Month

[Month 11: Integration Projects](../month-11/README.md) - End-to-end ML systems
