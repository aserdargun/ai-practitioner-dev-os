# Month 01: Foundation & Environment Setup

## Why It Matters

A solid foundation accelerates everything that follows. This month establishes your development environment, core Python skills, and data manipulation fundamentals—skills you'll use every day as an AI practitioner.

**Job Relevance**: Every AI/ML role requires proficiency in Python, pandas, and version control. These are table-stakes skills.

---

## Prerequisites

- Basic programming experience (any language)
- Computer with Python 3.11+ installed
- GitHub account
- VS Code installed

---

## Learning Goals

### Tier 1 Focus
- Python fundamentals and best practices
- Git/GitHub workflow
- Pandas for data manipulation
- NumPy for numerical computing
- SQL basics
- VS Code and Jupyter setup
- Linux command line fundamentals

### Tier 2 Introduction
- Docker basics (containerization concepts)
- GitHub Actions (CI/CD introduction)

### Tier 3 Preview
- Understanding where these foundations lead

---

## Main Project: Data Processing Pipeline

Build a data processing pipeline that:
1. Reads data from multiple sources (CSV, JSON, SQL)
2. Cleans and transforms data with pandas
3. Performs basic analysis
4. Outputs processed data
5. Runs in a Docker container

### Deliverables

1. **`pipeline/`** - Python package with data processing code
2. **`tests/`** - Unit tests for pipeline functions
3. **`data/`** - Sample input data
4. **`output/`** - Processed results
5. **`Dockerfile`** - Container definition
6. **`README.md`** - Setup and usage instructions

### Definition of Done

- [ ] Pipeline reads from CSV, JSON, and SQLite
- [ ] At least 5 data transformation functions
- [ ] At least 5 unit tests passing
- [ ] Dockerfile builds and runs successfully
- [ ] README with setup instructions

---

## Week-by-Week Plan

### Week 1: Environment & Python

**Focus**: Get your dev environment set up perfectly.

- Set up VS Code with Python extensions
- Configure Git and GitHub
- Review Python fundamentals (data structures, functions, classes)
- Set up virtual environments (venv or conda)
- Practice basic Linux commands

**Milestone**: Hello World pipeline that reads and writes a CSV.

### Week 2: Pandas & NumPy

**Focus**: Master data manipulation.

- Pandas DataFrames and Series
- Data cleaning techniques
- GroupBy and aggregations
- NumPy array operations
- Vectorized operations

**Milestone**: Pipeline can clean and transform messy data.

### Week 3: SQL & Data Sources

**Focus**: Work with structured data.

- SQL basics (SELECT, JOIN, WHERE)
- SQLite with Python
- Reading from multiple sources
- Data validation

**Milestone**: Pipeline reads from CSV, JSON, and SQLite.

### Week 4: Docker & Polish

**Focus**: Containerize and ship.

- Docker fundamentals
- Write Dockerfile
- GitHub Actions for CI
- Write tests
- Documentation

**Milestone**: Dockerized pipeline with tests and docs.

---

## Stretch Goals

- Add data validation with pydantic
- Implement basic caching
- Add logging throughout
- Create Makefile for common tasks
- Set up pre-commit hooks

---

## Claude Prompts

### Planning
```
/plan-week
```

### Getting Started
```
/start-week

As the Builder, scaffold a Python project with:
- src/pipeline/ package structure
- tests/ directory
- pyproject.toml with pytest and ruff
```

### Mid-Month Review
```
/status

How am I tracking against Month 01 goals?
```

### Code Review
```
/harden

Review my data processing pipeline for quality and security.
```

### Week-End Reflection
```
/retro

Run a Week [X] retrospective for Month 01.
```

---

## How to Publish

### Demo Script
```python
# demo.py
from pipeline import process

# Show the pipeline in action
input_data = load_sample_data()
result = process(input_data)
print(f"Processed {len(result)} records")
```

### Write-Up Topics
- Why data pipeline skills matter
- Challenges with messy data
- Docker for reproducibility
- Lessons learned

---

## Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Docker Getting Started](https://docs.docker.com/get-started/)
- Template: `templates/template-data-pipeline/`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 1
```

Check scores against the rubric in `docs/evaluation/rubric.md`.
