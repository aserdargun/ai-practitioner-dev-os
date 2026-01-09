# Tier 2: Intermediate Shipping

95 technologies for building and deploying production systems.

## Overview

Tier 2 expands on Tier 1 fundamentals with skills needed to ship real ML systems:
- Production-grade frameworks
- Cloud platforms
- CI/CD and DevOps
- Advanced databases
- Monitoring and observability

**Prerequisites**: Tier 1 complete
**Time to Complete**: 12 months at Intermediate pace (combined with T1)

---

## Skills (6)

| Skill | Description | Build On |
|-------|-------------|----------|
| MLOps (basics) | ML system operations | DevOps + ML |
| DevOps (basics) | Development operations | SDLC |
| CI/CD | Continuous integration/deployment | Git |
| NoSQL | Non-relational databases | SQL |
| Embedding Models | Vector representations | Word2Vec |
| RAG Systems | Retrieval-augmented generation | NLP |

---

## Algorithms (10)

Advanced ML algorithms.

| Algorithm | Type | When to Use |
|-----------|------|-------------|
| XGBoost | Gradient Boosting | Best accuracy for tabular |
| LightGBM | Gradient Boosting | Large datasets, fast |
| CatBoost | Gradient Boosting | Categorical features |
| CNN | Deep Learning | Images, spatial data |
| GAN | Generative | Image generation |
| GPT | Language Model | Text generation |
| BERT | Language Model | Text understanding |
| T5 | Language Model | Text-to-text tasks |
| PEFT | Fine-tuning | Efficient model tuning |
| LoRA/QLoRA | Fine-tuning | Low-rank adaptation |

---

## Automation (3)

Workflow automation tools.

| Tool | Platform | Best For |
|------|----------|----------|
| Power Automate | Microsoft | Office integrations |
| Power Apps | Microsoft | Low-code apps |
| n8n | Open Source | Workflow automation |

---

## Cloud (3)

Major cloud platforms.

| Platform | Strengths | When to Use |
|----------|-----------|-------------|
| AWS | Broadest services | Most jobs, flexibility |
| Azure | Microsoft integration | Enterprise, .NET shops |
| GCP | ML/AI services | ML-focused work |

### Learning Priority
Pick **one** to learn deeply first, understand the others conceptually.

---

## Databases (24)

Expanded database coverage.

### Relational
| Database | Best For |
|----------|----------|
| PostgreSQL | General purpose, advanced features |
| MySQL | Web applications |
| Azure SQL DB | Azure cloud |

### NoSQL Document
| Database | Best For |
|----------|----------|
| MongoDB | Flexible schemas |
| Cosmos DB | Azure multi-model |
| DynamoDB | AWS serverless |

### Key-Value / Cache
| Database | Best For |
|----------|----------|
| Redis | Caching, sessions |

### Search
| Database | Best For |
|----------|----------|
| Elasticsearch | Full-text search |
| OpenSearch | AWS search |

### Analytics
| Database | Best For |
|----------|----------|
| ClickHouse | Analytics, fast queries |
| Snowflake | Cloud data warehouse |
| Redshift | AWS data warehouse |
| BigQuery | GCP analytics |
| Synapse | Azure analytics |

### Data Lake
| Database | Best For |
|----------|----------|
| ADLS | Azure Data Lake |

### Graph
| Database | Best For |
|----------|----------|
| Neo4j | Graph relationships |
| TigerGraph | Large-scale graphs |
| JanusGraph | Distributed graphs |
| Neptune | AWS managed graphs |

### Vector
| Database | Best For |
|----------|----------|
| Pinecone | Managed vector search |
| Qdrant | Open source vectors |
| Weaviate | Vector + hybrid search |
| Milvus | Large-scale vectors |
| FAISS | Local vector search |

---

## Frameworks (4)

Production-grade frameworks.

| Framework | Best For |
|-----------|----------|
| FastAPI | Modern APIs (recommended) |
| React | Frontend UIs |
| Next.js | Full-stack React |
| Spring Boot | Java enterprise |

### Priority
- **FastAPI** — Primary API framework for ML
- Others as needed for full-stack work

---

## Libraries (15)

ML and data science libraries.

### Core ML
| Library | Purpose |
|---------|---------|
| scikit-learn | Classical ML |
| SciPy | Scientific computing |
| statsmodels | Statistical modeling |

### Deep Learning
| Library | Purpose |
|---------|---------|
| PyTorch | Primary DL framework |
| TensorFlow | Production DL |
| JAX | High-performance ML |

### Probabilistic
| Library | Purpose |
|---------|---------|
| PyMC | Bayesian modeling |
| NumPyro | Probabilistic programming |

### Vision & NLP
| Library | Purpose |
|---------|---------|
| OpenCV | Computer vision |
| Hugging Face | Transformers, models |

### LLM/Agent
| Library | Purpose |
|---------|---------|
| LangChain | LLM applications |
| LangGraph | Agent workflows |
| LlamaIndex | RAG systems |

### Data
| Library | Purpose |
|---------|---------|
| SQLAlchemy | Database ORM |
| GenSim | Topic modeling |

---

## Monitoring (4)

Observability tools.

| Tool | Purpose |
|------|---------|
| Prometheus | Metrics collection |
| Grafana | Dashboards |
| Datadog | Full observability |
| CloudWatch | AWS monitoring |

---

## Platforms (23)

Development and ML platforms.

### Containers & CI/CD
| Platform | Purpose |
|----------|---------|
| Docker | Containerization |
| GitHub Actions | CI/CD |
| Jenkins | CI/CD server |
| GitLab CI | GitLab CI/CD |
| CircleCI | Cloud CI/CD |
| Bitbucket | Git + CI/CD |
| Travis CI | Open source CI |

### Data Pipelines
| Platform | Purpose |
|----------|---------|
| Airflow | Workflow orchestration |
| Azure Data Factory | Azure ETL |
| dbt | Data transformation |

### ML Platforms
| Platform | Purpose |
|----------|---------|
| MLflow | ML lifecycle |
| Databricks | Unified analytics |
| Azure DevOps | Microsoft DevOps |
| SageMaker | AWS ML |
| Vertex AI | GCP ML |
| Bedrock | AWS LLM |
| Azure AI Foundry | Azure AI |
| Azure ML | Azure ML platform |
| Kubeflow (intro) | Kubernetes ML |

### Evaluation
| Platform | Purpose |
|----------|---------|
| OpenAI Agent Evals | Agent evaluation |
| OpenAI Trace Grading | Response grading |
| OpenAI Tools | File/web search |

---

## Services (8)

Cloud services.

### AWS
| Service | Purpose |
|---------|---------|
| S3 | Object storage |
| Athena | SQL on S3 |
| EventBridge | Event routing |
| API Gateway | API management |
| Lambda | Serverless functions |

### Azure
| Service | Purpose |
|---------|---------|
| Azure Functions | Serverless |
| Azure Stream Analytics | Stream processing |
| Azure Container Apps | Container hosting |

---

## Month-by-Month Focus (Intermediate)

| Month | Primary Focus | Key Technologies |
|-------|---------------|------------------|
| 1-2 | T1 Review + Setup | Review fundamentals, Docker |
| 3 | Cloud Basics | AWS/Azure/GCP intro |
| 4 | Advanced Databases | PostgreSQL, MongoDB |
| 5 | Advanced ML | XGBoost, scikit-learn deep dive |
| 6 | Deep Learning | PyTorch, CNNs |
| 7 | NLP/LLM | Hugging Face, BERT |
| 8 | RAG Systems | LangChain, vector DBs |
| 9 | APIs & Deployment | FastAPI, Docker |
| 10 | MLOps | MLflow, CI/CD |
| 11 | Monitoring | Prometheus, Grafana |
| 12 | Integration Project | Full ML system |

---

## Completion Criteria

You've completed Tier 2 when you can:
- [ ] Deploy ML models as APIs
- [ ] Work with cloud platforms (at least one)
- [ ] Build CI/CD pipelines
- [ ] Use Docker for containerization
- [ ] Implement RAG systems
- [ ] Monitor production systems
- [ ] Work with various database types
- [ ] Fine-tune language models
