# Skills Playbook

Reusable playbooks for common AI/ML engineering tasks.

---

## Overview

Skills are structured workflows for recurring tasks. Each skill provides:
- Step-by-step process
- Code templates
- Checklists
- Best practices

Skills are stored in `.claude/skills/` and can be referenced by any agent.

---

## Available Skills

| Skill | File | Use Case |
|-------|------|----------|
| EDA to Insight | `eda.md` | Exploratory data analysis |
| Shipping APIs | `shipping-api.md` | FastAPI service development |
| RAG + Evals | `rag-eval.md` | RAG systems with evaluation |

---

## Skill: EDA to Insight

**File**: `.claude/skills/eda.md`

**When to Use**:
- Starting a new data project
- Investigating data quality
- Preparing data for modeling

### Quick Start

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and inspect
df = pd.read_csv("data.csv")
print(f"Shape: {df.shape}")
df.info()
df.head()
```

### The Process

1. **First Look** (10 min)
   - Load data
   - Check shape, types, head

2. **Missing Data** (15 min)
   - Analyze patterns
   - Decide on strategy

3. **Univariate Analysis** (20 min)
   - Distribution of each variable
   - Identify outliers

4. **Bivariate Analysis** (20 min)
   - Correlations
   - Target relationships

5. **Document Findings** (15 min)
   - Write summary
   - List next steps

### Checklist

- [ ] Data loaded
- [ ] Types checked
- [ ] Missing values analyzed
- [ ] Distributions visualized
- [ ] Correlations explored
- [ ] Findings documented

---

## Skill: Shipping APIs

**File**: `.claude/skills/shipping-api.md`

**When to Use**:
- Building REST APIs
- ML model serving
- Creating microservices

### Quick Start

```bash
pip install fastapi uvicorn pydantic
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

### The Process

1. **Project Structure** (5 min)
   ```
   my-api/
   ├── src/
   │   ├── main.py
   │   ├── models.py
   │   └── routes/
   ├── tests/
   ├── Dockerfile
   └── pyproject.toml
   ```

2. **Core Setup** (10 min)
   - FastAPI app
   - Health endpoints
   - CORS middleware

3. **Define Models** (10 min)
   - Pydantic schemas
   - Request/response types

4. **Add Routes** (15 min)
   - CRUD operations
   - Error handling

5. **Add Tests** (15 min)
   - TestClient
   - Happy path + errors

6. **Docker** (10 min)
   - Dockerfile
   - docker-compose

### Checklist

- [ ] FastAPI app created
- [ ] Health endpoints added
- [ ] Pydantic models defined
- [ ] Routes implemented
- [ ] Tests written
- [ ] Dockerfile created

---

## Skill: RAG + Evals

**File**: `.claude/skills/rag-eval.md`

**When to Use**:
- Building Q&A systems
- Document search
- Knowledge bases

### Quick Start

```bash
pip install langchain chromadb sentence-transformers ragas
```

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
vectorstore = Chroma.from_documents(docs, embeddings)
```

### The Process

1. **Document Loading** (10 min)
   - Load PDFs/text
   - Split into chunks

2. **Embedding & Indexing** (15 min)
   - Generate embeddings
   - Create vector store

3. **Retrieval Setup** (10 min)
   - Configure retriever
   - Test queries

4. **RAG Chain** (15 min)
   - Create prompt template
   - Chain retriever + LLM

5. **Evaluation Dataset** (15 min)
   - Create test questions
   - Define ground truth

6. **RAGAS Evaluation** (20 min)
   - Run metrics
   - Analyze results

### Key Metrics

| Metric | Target | Meaning |
|--------|--------|---------|
| Faithfulness | > 80% | Answer grounded in context |
| Relevancy | > 80% | Answer addresses question |
| Context Precision | > 70% | Retrieved docs are relevant |
| Context Recall | > 70% | All needed docs retrieved |

### Checklist

- [ ] Documents loaded and chunked
- [ ] Vector store created
- [ ] Retriever working
- [ ] RAG chain built
- [ ] Eval dataset created
- [ ] Metrics computed

---

## Using Skills

### In Commands

Skills are automatically referenced when relevant:

```
/ship-mvp

Building FastAPI service...
Using skill: Shipping APIs

[Follows the shipping-api.md playbook]
```

### Directly

Ask Claude to use a skill:

```
"Use the EDA skill to analyze this dataset"
```

### Customizing

Edit skill files to add project-specific guidance:

```markdown
## Project-Specific Notes

For this project:
- Use SQLAlchemy for database
- Follow company API standards
- Include Prometheus metrics
```

---

## Creating New Skills

### Template

```markdown
# Skill: [Name]

[Brief description]

---

## When to Use

- [Situation 1]
- [Situation 2]

---

## Prerequisites

```bash
pip install [packages]
```

---

## The Process

### Phase 1: [Name] (X minutes)

[Description]

```python
[Code]
```

### Phase 2: [Name] (X minutes)

[Description]

---

## Checklist

- [ ] Step 1
- [ ] Step 2

---

## Common Pitfalls

1. [Pitfall 1]
2. [Pitfall 2]
```

### Adding to System

1. Create file in `.claude/skills/`
2. Update `.claude/README.md` skill list
3. Reference in agent files if relevant

---

## Best Practices

### For Using Skills

1. **Follow the order**: Steps are sequenced intentionally
2. **Use checklists**: Don't skip verification steps
3. **Adapt as needed**: Skills are guidelines, not rules

### For Creating Skills

1. **Time estimates**: Include realistic time per phase
2. **Code examples**: Working code, not pseudocode
3. **Checklists**: Make completion verifiable
4. **Common pitfalls**: Help avoid mistakes

---

## See Also

- [How to Use](how-to-use.md) — Overall workflow
- [Commands Guide](commands.md) — Available commands
- Skill files in `.claude/skills/`
