# SETUP.md — Repository Generator Prompt (Claude Code)

## How to use this prompt
1) Open this file in GitHub (or locally), copy **everything** below.
2) Paste it into **Claude Code** (with repo integration enabled) while connected to your fork of this repository.
3) Run it. Claude will ask you **one** question for `{{LEARNER_LEVEL}}`, then generate the entire repository structure, docs, templates, CI, and scripts.

> Important: This prompt is meant to be executed by Claude Code. It is not a human checklist.

### Generator Prompt (copy everything from here to the end)

---

You are Claude Code acting as:
1) a senior AI engineer + OSS maintainer,
2) a learning scientist,
3) a project manager,
4) an evaluator/coach.

Build a public, forkable GitHub repository.

Repo name (use as title in README): "ai-practitioner-dev-os"
Theme: “AI Practitioner Booster 2026 — AI-driven, project-based learning system”.

IMPORTANT: Before you generate anything, ask me ONE question:
- “What is the learner level? (Beginner / Intermediate / Advanced)”
Use the answer to set {{LEARNER_LEVEL}} everywhere.

Hard requirements
- Markdown-first documentation.
- The repo must be immediately usable by a learner (no placeholders except {{LEARNER_LEVEL}}).
- The system must be AI-driven and continuously evolving based on learner successes/failures.
- Claude capabilities must live under a `.claude/` folder (agents, commands, skills, hooks, memory, MCP).
- Do not break links from docs/ to tooling; keep docs pointing to `.claude/` where appropriate.
- Provide a “special path README” per learner level that becomes their main dashboard.

Core concept
- Levels are pace-based and cumulative:
  - Beginner completes Tier 1 only in 2026.
  - Intermediate completes Tier 1 + Tier 2 in 2026.
  - Advanced completes Tier 1 + Tier 2 + Tier 3 in 2026 (hands-on across all items).

Allowed adaptations (must be enforced by docs + code)
- Level changes: upgrade/downgrade learner level (Beginner ↔ Intermediate ↔ Advanced), only at month boundaries unless explicitly overridden by rubric rules.
- Month reordering: swap upcoming month modules while preserving tier scope.
- Remediation weeks: insert 1-week remediation blocks inside a month without changing tier scope.
- Project swap: replace a month’s main project with an alternative of equivalent scope/skills (same tier scope), keeping deliverables and DoD comparable.

## Required repository tree (generate exactly this structure)

/ 
  README.md
  CLAUDE.md
  LICENSE
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  SECURITY.md

  .claude/
    README.md
    agents/
      README.md
      planner.md
      builder.md
      reviewer.md
      evaluator.md
      coach.md
      researcher.md
    commands/
      README.md
      catalog.md
    skills/
      README.md
      eda-to-insight.md
      baseline-model-and-card.md
      experiment-plan.md
      forecasting-checklist.md
      rag-with-evals.md
      api-shipping-checklist.md
      observability-starter.md
      k8s-deploy-checklist.md   # include but gate it to Advanced in docs
    hooks/
      README.md
      pre_week_start.sh
      post_week_review.sh
      pre_publish_check.sh
    memory/
      README.md
      learner_profile.json
      progress_log.jsonl
      decisions.jsonl
      best_practices.md
    mcp/
      README.md
      tool-contracts.md
      examples.md
      safety.md
      server_stub/
        README.md
        server.py
      client_examples/
        README.md
        python_client.py
    path-engine/
      README.md
      evaluate.py
      adapt.py
      report.py

  docs/
    how-to-use.md
    system-overview.md
    commands.md
    agents.md
    skills-playbook.md
    hooks.md
    memory-system.md
    evaluation/
      rubric.md
      signals.md
      scoring.md
      adaptation-rules.md
    publishing/
      how-to-demo.md
      how-to-write-medium-post.md
      portfolio-checklist.md

  stacks/
    tiers.md
    tier-1-beginner.md
    tier-2-intermediate.md
    tier-3-advanced.md

  paths/
    {{LEARNER_LEVEL}}/
      README.md
      tracker.md
      journal/
        README.md
        weekly-template.md
        monthly-template.md
      month-01/
        README.md
      month-02/
        README.md
      month-03/
        README.md
      month-04/
        README.md
      month-05/
        README.md
      month-06/
        README.md
      month-07/
        README.md
      month-08/
        README.md
      month-09/
        README.md
      month-10/
        README.md
      month-11/
        README.md
      month-12/
        README.md

  templates/
    template-fastapi-service/
      README.md
      app/
        main.py
      tests/
        test_health.py
      Dockerfile
      pyproject.toml
    template-data-pipeline/
      README.md
      pipeline/
        run.py
        validate.py
      tests/
        test_validate.py
      pyproject.toml
    template-rag-service/
      README.md
      rag/
        ingest.py
        retrieve.py
        answer.py
      eval/
        golden_set.jsonl
      tests/
        test_retrieve.py
      pyproject.toml
    template-eval-harness/
      README.md
      evals/
        run_evals.py
        graders.py
      datasets/
        sample_golden.jsonl
      pyproject.toml

  examples/
    mini-example/
      README.md
      src/
        README.md
      tests/
        README.md

  .github/
    ISSUE_TEMPLATE/
      bug_report.md
      feature_request.md
      monthly_journal.md
    PULL_REQUEST_TEMPLATE.md
    workflows/
      ci.yml

## Linking rules (do NOT break these)
- docs/commands.md must reference `.claude/commands/catalog.md`
- docs/agents.md must reference `.claude/agents/*.md`
- docs/skills-playbook.md must reference `.claude/skills/*.md`
- docs/hooks.md must reference `.claude/hooks/*.sh`
- docs/memory-system.md must reference `.claude/memory/*`
- docs/evaluation/* must reference `.claude/path-engine/*`
- docs/system-overview.md must explain the end-to-end loop and point to `.claude/README.md`
- paths/{{LEARNER_LEVEL}}/README.md must link to:
  - docs/how-to-use.md
  - stacks/tiers.md
  - docs/commands.md
  - docs/evaluation/rubric.md
  - `.claude/path-engine/report.py` usage
  - `.claude/memory/best_practices.md`

## Content requirements (must be fully written, no empty files)

### 1) Root README.md
Must include:
- What this repo is
- “How to use (from zero)” section:
  1) Fork this repository to your GitHub account
  2) Connect Claude Code to your forked repository
  3) In the README, copy the “Repository Generator Prompt” block and paste it into Claude Code
  4) Claude Code generates the full repo structure and commits it to your fork
  5) Clone your generated repository to your local dev environment
  6) Recommended IDE: VS Code
- Quickstart (5 minutes) to run a first /status + /plan-week + /evaluate + /report cycle
- How the AI-driven loop works (Evaluate → Adapt → Execute)
- Link to learner dashboard: paths/{{LEARNER_LEVEL}}/README.md
- Daily workflow + Weekly workflow
- How to ask Claude for help using /commands
- Where Claude capabilities live: `.claude/`
- Link to `SETUP.md` as the canonical generator prompt (do not duplicate the generator prompt in README to avoid drift)

### 2) paths/{{LEARNER_LEVEL}}/README.md (SPECIAL DASHBOARD)
Must include:
- Learner level shown clearly: {{LEARNER_LEVEL}}
- Current month pointer + checklists
- “This week plan” template
- Commands cheat-sheet (links to docs/commands.md)
- Evaluation snapshot (what to run, how to interpret)
- “If you are stuck” playbook
- “Upgrade/Downgrade rules” and what triggers a path change

### 3) docs/how-to-use.md
Must be ready-to-use, include:
- How to run the system loop locally (scripts + how to invoke via Claude)
- Weekly cadence (Week1/2/3/4)
- How to log progress & reflections
- How to request path changes
- How to capture best practices into `.claude/memory/best_practices.md`

### 4) Commands
- `.claude/commands/catalog.md` is the source of truth.
- docs/commands.md should be a friendly guide and link to the catalog.
Provide a command catalog like:
- /status
- /plan-week
- /start-week
- /ship-mvp
- /harden
- /publish
- /retro
- /evaluate
- /adapt-path
- /add-best-practice
- /debug-learning
Each command must include:
- purpose, inputs, outputs, when to use, example prompt.
Also include a “command routing” note: which agent handles which command.

### 5) Agents
- `.claude/agents/*.md` define role responsibilities + constraints + handoffs:
  - Planner Agent
  - Builder Agent
  - Reviewer Agent
  - Evaluator Agent
  - Coach Agent
  - Researcher Agent
docs/agents.md should explain how to invoke them and point to those files.

### 6) Skills
- `.claude/skills/*.md` are the canonical playbooks.
docs/skills-playbook.md summarizes and links.
Each skill must include:
- trigger, steps, artifacts produced, quality bar.

### 7) Hooks
- `.claude/hooks/*.sh` contain runnable (simple) scripts.
docs/hooks.md explains when/why to use them and how.
Hooks required:
- pre_week_start.sh (creates week plan stub, updates tracker)
- post_week_review.sh (prompts retrospective, updates progress log)
- pre_publish_check.sh (runs tests, lints, checks docs links)

Cross-platform note (must appear in docs/hooks.md):
- These hooks are shell scripts intended for Linux/macOS and Windows via WSL or Git Bash.
- Provide a “Manual fallback” subsection showing the equivalent commands a learner can run step-by-step if they cannot run .sh scripts.

### 8) Local “Memory System”
- `.claude/memory/*` is the only “memory store”.
Implement:
- learner_profile.json (goals, constraints, schedule)
- progress_log.jsonl (timestamped events)
- decisions.jsonl (important decisions)
- best_practices.md (living doc; appended frequently)

docs/memory-system.md must explain:
- how Claude updates memory (append-only discipline + PR-friendly edits)
- how learner reviews/edits memory
- how memory affects adaptation
- IMPORTANT: Memory files are append-only sources of truth; `paths/{{LEARNER_LEVEL}}/tracker.md` is a derived artifact that `report.py` may overwrite/regenerate at any time.

### 9) Evaluation & Adaptation
- `.claude/path-engine/*` implements the loop with Python stdlib only.
Implement:
- evaluate.py reads `.claude/memory/*` + basic repo signals and outputs scores
- adapt.py proposes modifications (repeat month, remediate, accelerate, swap project, reorder upcoming months, change learner level)
- report.py writes/updates `paths/{{LEARNER_LEVEL}}/tracker.md` with a clean report

Hard rules:
- docs/evaluation/adaptation-rules.md must define the allowed mutations (the “Allowed adaptations” list above) and provide a clear schema.
- adapt.py MUST ONLY output those allowed mutations, in that schema, so changes are deterministic and reviewable.
- docs/evaluation/scoring.md must also include:
  - IMPORTANT: Memory files are append-only sources of truth; `paths/{{LEARNER_LEVEL}}/tracker.md` is a derived artifact that `report.py` may overwrite/regenerate at any time.

docs/evaluation/* explain rubric/signals/scoring/adaptation rules and link to scripts.

### 10) MCP
- `.claude/mcp/*` contains tool contracts + safety + examples + stubs.
Provide:
- tool-contracts.md (schemas + constraints)
- examples.md (how agents use tools)
- safety.md (secrets, privacy, eval integrity)
Include server stub:
- `.claude/mcp/server_stub/server.py` exposes:
  - hello tool
  - read_repo_file tool (safe subset)
  - write_memory_entry tool (append-only into `.claude/memory/`)
Include a client example:
- `.claude/mcp/client_examples/python_client.py`

### 11) 12-month curriculum
Generate `paths/{{LEARNER_LEVEL}}/month-01..month-12/README.md`.
Each month README MUST include:
- Why it matters (job relevance)
- Prerequisites
- Learning goals
- Main project (deliverables + Definition of Done checklist)
- Stretch goals
- “Claude prompts” section (copy/paste prompts that call agents + commands)
- How to publish (demo + write-up)
Apply pace rules:
- Beginner: Tier 1 only
- Intermediate: Tier 1 + Tier 2
- Advanced: Tier 1 + Tier 2 + Tier 3
Keep month numbering consistent; Advanced integrates harder infra/ops earlier.

### 12) Stacks
Write:
- stacks/tiers.md (tier definitions + pace)
- stacks/tier-1-beginner.md, tier-2-intermediate.md, tier-3-advanced.md
Use this refactored tier model (copy verbatim into files and present cleanly):

Tier 1 (Beginner Foundation)
- Mindset: Agile
- Skills: Data Science, Probability, Statistics, ETL, Predictive Analytics, Optimization, Experimental Design, A/B Testing, Time Series Analysis, Text Mining, Computer Vision, Deep Learning (intro), SDLC, Digital Signal Processing, Fast Fourier Analysis
- Algorithms: ARIMA, KNN, Naive Bayes, SVM, Decision Forests, Boosting, Clustering, LDA, RNN, LSTM, Word2Vec, GloVe, FastText, YOLO
- Languages: Python (assumed), SQL, R, Bash, Shell Scripting, VBA, GraphQL
- DB: MS SQL
- Frameworks: Flask, Django
- Libraries: Pandas, NumPy, Matplotlib, seaborn, Plotly, NLTK, Dash
- Tools/Platforms: VS Code, Jupyter, Git/GitHub, Linux fundamentals, Streamlit, Power BI, Metabase (optional), PyCharm (optional)
- Protocol: RESTful APIs

Tier 2 (Intermediate Shipping)
- Skills: MLOps (basics), DevOps (basics), CI/CD, NoSQL, Embedding Models, RAG Systems
- Algorithms: XGBoost, LightGBM, CatBoost, CNN, GAN, GPT, BERT, T5, PEFT, LoRA/QLoRA
- Automation: Power Automate, Power Apps, n8n
- Cloud: AWS, Azure, GCP
- Databases: PostgreSQL, MySQL, MongoDB, Redis, DynamoDB, Elasticsearch, OpenSearch, ClickHouse, Snowflake, Redshift, BigQuery, Synapse, Azure SQL DB, Cosmos DB, ADLS, Neo4j, TigerGraph, JanusGraph, Neptune, Pinecone, Qdrant, Weaviate, Milvus, FAISS
- Frameworks: FastAPI, React, Next.js, Spring Boot
- Libraries: scikit-learn, SciPy, statsmodels, PyTorch, TensorFlow, JAX, PyMC, NumPyro, OpenCV, Hugging Face, LangChain, LangGraph, LlamaIndex, SQLAlchemy, GenSim
- Monitoring: Prometheus, Grafana, Datadog, CloudWatch
- Platforms: Docker, GitHub Actions, Jenkins, GitLab CI, CircleCI, Bitbucket, Travis CI, Airflow, Azure Data Factory, dbt, MLflow, Databricks/Azure Databricks, Azure DevOps, SageMaker, Vertex AI, Bedrock, Azure AI Foundry, Azure ML, Kubeflow (intro), OpenAI Agent Evals, OpenAI Trace Grading, OpenAI Tools File Search/Web Search
- Services: S3, Athena, EventBridge, API Gateway, Lambda, Azure Functions, Azure Stream Analytics, Azure Container Apps

Tier 3 (Advanced Scale/Interop/Perf)
- APIs/Protocols: OpenAI Responses API, OpenAI Realtime API, MCP, A2A
- Systems: Kafka, RabbitMQ, Kinesis, Spark, Hadoop, Hive, Pig
- Platform: Kubernetes, AKS, ECS, Kubeflow (platform-grade)
- Performance: ONNX, TensorRT, CUDA, TFLite
- Advanced ML: Federated Learning, NVIDIA FLARE, Reinforcement Learning, Graph Neural Networks, Network Analysis
- Languages: Scala, C, C++, Java-for-big-data
- Domain: ArcGIS (optional), OpenEmbedded, YOCTO (optional)

### 13) OSS hygiene + CI
Include:
- MIT license
- Contributor Covenant code of conduct
- Contributing guide
- Security policy
- GitHub issue templates + PR template
- GitHub Actions workflow (ruff + pytest) on PR and main

### 14) Templates must be real (STRICT)
Each template must have:
- a README explaining usage
- minimal runnable code
- tests that pass
- pyproject.toml with:
  - pinned minimal dependencies (use conservative version ranges)
  - a [tool.ruff] section (or equivalent) with sensible defaults
  - pytest configuration (e.g., [tool.pytest.ini_options]) so tests run consistently
Keep them consistent and lightweight across templates.

### 15) Examples
examples/mini-example must show “done looks like this” with:
- small dataset or stub
- one model or one RAG mini flow
- tests
- demo guide

## Generation rules
- Print the final repo tree first.
- Ensure all relative links work.
- Ensure no file is empty or placeholder (except {{LEARNER_LEVEL}}).
- Prefer simple, standard tooling.
- Add copy/paste “Claude prompts” in each month README that invoke:
  - /commands
  - specific agents
  - memory updates
  - evaluation + adaptation loop
- Make the system feel like a “learning OS” that guides, evaluates, and adapts.
- If any instruction conflicts, resolve by priority: Hard requirements → Linking rules → Required tree → Content requirements → Everything else.

Now proceed to generate the entire repository.
