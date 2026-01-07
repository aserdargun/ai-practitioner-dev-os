# Skill: Shipping APIs

Build and deploy FastAPI services quickly and reliably.

---

## When to Use

- Building a REST API for ML models
- Creating microservices
- Exposing data pipelines as services
- Building demo backends

---

## Prerequisites

```bash
pip install fastapi uvicorn pydantic python-multipart
```

---

## The API Playbook

### Phase 1: Project Structure (5 minutes)

```
my-api/
├── src/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── models.py        # Pydantic models
│   ├── routes/          # Route handlers
│   │   ├── __init__.py
│   │   └── health.py
│   └── services/        # Business logic
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml
├── Dockerfile
└── README.md
```

### Phase 2: Core App Setup (10 minutes)

**src/main.py**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import health

app = FastAPI(
    title="My API",
    description="API description here",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["Health"])


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
```

**src/routes/health.py**
```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.get("/ready")
async def readiness_check():
    # Add dependency checks here
    return {"status": "ready"}
```

### Phase 3: Define Models (10 minutes)

**src/models.py**
```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=1)


class PredictionResponse(BaseModel):
    prediction: float
    confidence: float
    model_version: str
```

### Phase 4: Add Routes (15 minutes)

**src/routes/items.py**
```python
from fastapi import APIRouter, HTTPException, status
from typing import List

from src.models import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

# In-memory storage (replace with database)
items_db: dict[int, dict] = {}
next_id = 1


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    global next_id
    from datetime import datetime

    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
        "created_at": datetime.utcnow(),
    }
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@router.get("/", response_model=List[ItemResponse])
async def list_items():
    return list(items_db.values())


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found"
        )
    return items_db[item_id]


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found"
        )
    del items_db[item_id]
```

### Phase 5: Add Tests (15 minutes)

**tests/test_main.py**
```python
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "A test"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data


def test_get_item_not_found():
    response = client.get("/items/99999")
    assert response.status_code == 404
```

### Phase 6: Docker Setup (10 minutes)

**Dockerfile**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy source
COPY src/ src/

# Run
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml**
```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - LOG_LEVEL=info
    volumes:
      - ./src:/app/src:ro  # For development
```

### Phase 7: Run and Test (5 minutes)

```bash
# Development
uvicorn src.main:app --reload

# Production
uvicorn src.main:app --host 0.0.0.0 --port 8000

# Docker
docker-compose up --build

# Run tests
pytest tests/ -v
```

Visit `http://localhost:8000/docs` for interactive API docs.

---

## Checklist

- [ ] Project structure created
- [ ] FastAPI app initialized
- [ ] Health endpoints added
- [ ] Pydantic models defined
- [ ] Routes implemented
- [ ] Error handling added
- [ ] Tests written and passing
- [ ] Dockerfile created
- [ ] README documented
- [ ] API docs accessible

---

## Common Patterns

### Dependency Injection
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items/")
async def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

### Background Tasks
```python
from fastapi import BackgroundTasks

@router.post("/notify/")
async def send_notification(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, "user@example.com")
    return {"message": "Notification queued"}
```

### File Upload
```python
from fastapi import UploadFile, File

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
```
