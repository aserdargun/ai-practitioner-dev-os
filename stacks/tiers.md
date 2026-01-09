# Tier System

How technologies are organized by complexity.

## Overview

The AI Practitioner Learning OS organizes 175 technologies into three tiers. Your learner level determines which tiers you work with.

## Tier Summary

| Tier | Focus | Items | Level |
|------|-------|-------|-------|
| Tier 1 | Foundation | 53 | Beginner+ |
| Tier 2 | Shipping | 95 | Intermediate+ |
| Tier 3 | Scale & Performance | 27 | Advanced |

## Learner Levels (Cumulative)

| Level | Tiers Included | Total Items |
|-------|----------------|-------------|
| **Beginner** | Tier 1 | 53 |
| **Intermediate** | Tier 1 + Tier 2 | 148 |
| **Advanced** | Tier 1 + Tier 2 + Tier 3 | 175 |

Levels are **cumulative** - each higher level includes all lower tiers.

## Tier Details

### Tier 1 — Beginner Foundation (53 items)

**Focus**: Core skills and tools every AI practitioner needs.

**Categories**:
- Mindset & Skills (16): Agile, Data Science, Probability, Statistics, etc.
- Algorithms (14): ARIMA, KNN, SVM, Decision Forests, RNN, LSTM, etc.
- Languages (7): Python, SQL, R, Bash, Shell Scripting, VBA, GraphQL
- Databases (1): MS SQL
- Frameworks (2): Flask, Django
- Libraries (7): Pandas, NumPy, Matplotlib, seaborn, Plotly, NLTK, Dash
- Tools & Platforms (8): VS Code, Jupyter, Git/GitHub, Linux, Streamlit, etc.
- Protocols (1): RESTful APIs

See [tier-1-beginner.md](tier-1-beginner.md) for full list.

### Tier 2 — Intermediate Shipping (95 items)

**Focus**: Skills for shipping production ML systems.

**Categories**:
- Skills (6): MLOps, DevOps, CI/CD, NoSQL, Embeddings, RAG
- Algorithms (10): XGBoost, LightGBM, CNN, GAN, GPT, BERT, LoRA, etc.
- Automation (3): Power Automate, Power Apps, n8n
- Cloud (3): AWS, Azure, GCP
- Databases (25): PostgreSQL, MongoDB, Redis, Pinecone, Qdrant, etc.
- Frameworks (4): FastAPI, React, Next.js, Spring Boot
- Libraries (15): scikit-learn, PyTorch, TensorFlow, LangChain, etc.
- Monitoring (4): Prometheus, Grafana, Datadog, CloudWatch
- Platforms (22): Docker, GitHub Actions, Airflow, MLflow, etc.
- Services (8): S3, Lambda, Azure Functions, etc.

See [tier-2-intermediate.md](tier-2-intermediate.md) for full list.

### Tier 3 — Advanced Scale/Interop/Perf (27 items)

**Focus**: Large-scale systems, performance optimization, advanced ML.

**Categories**:
- APIs & Protocols (4): OpenAI Responses/Realtime API, MCP, A2A
- Systems (7): Kafka, RabbitMQ, Kinesis, Spark, Hadoop, Hive, Pig
- Platforms (4): Kubernetes, AKS, ECS, Kubeflow (platform-grade)
- Performance (4): ONNX, TensorRT, CUDA, TFLite
- Advanced ML (5): Federated Learning, NVIDIA FLARE, RL, GNNs, etc.
- Languages (4): Scala, C, C++, Java-for-big-data
- Domain-Specific (3): ArcGIS, OpenEmbedded, YOCTO

See [tier-3-advanced.md](tier-3-advanced.md) for full list.

## 12-Month Curriculum Mapping

For **Advanced** level (all tiers):

| Months | Primary Focus | Tier Emphasis |
|--------|---------------|---------------|
| 1-3 | Foundation + EDA + ML Basics | Tier 1 |
| 4-6 | APIs + RAG + Cloud Deployment | Tier 1 + Tier 2 |
| 7-9 | MLOps + Monitoring + Scale | Tier 2 + Tier 3 |
| 10-12 | Advanced Systems + Performance | Tier 2 + Tier 3 |

Each month integrates technologies from relevant tiers based on project needs.

## Pace Rules

- **Beginner**: Covers all Tier 1 items in 12 months
- **Intermediate**: Covers Tier 1 + Tier 2 in 12 months
- **Advanced**: Covers all tiers in 12 months

The Advanced pace is intensive - expect to work with 15+ technologies per month.

## Level Changes

You can change levels at month boundaries:

**Upgrade** (e.g., Beginner → Intermediate):
- When consistently scoring >85%
- When ready for more challenge
- Adds new tier technologies

**Downgrade** (e.g., Advanced → Intermediate):
- When consistently scoring <55%
- When struggling with tier scope
- Removes Tier 3 from scope

See [docs/evaluation/adaptation-rules.md](../docs/evaluation/adaptation-rules.md) for details.

## Using STACK.md

The `STACK.md` file lists all 175 technologies. You can:

1. **Use all items** (default): Run generator without customization
2. **Customize**: Edit `MY_STACK.md`, check `[x]` only items you want

The generator respects your tier scope and selections.

## Related Files

- [tier-1-beginner.md](tier-1-beginner.md) - Full Tier 1 list
- [tier-2-intermediate.md](tier-2-intermediate.md) - Full Tier 2 list
- [tier-3-advanced.md](tier-3-advanced.md) - Full Tier 3 list
- [STACK.md](../STACK.md) - Master technology list
