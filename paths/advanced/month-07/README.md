# Month 07: RAG Systems

## Why It Matters

Retrieval-Augmented Generation (RAG) is how companies deploy LLMs on their own data. This month teaches you to build production-quality RAG systems with proper evaluation.

**Job Relevance**: RAG is the most in-demand LLM application pattern. Every company building with LLMs needs this skill.

---

## Prerequisites

- Month 01-06 completed
- NLP and embeddings understanding
- API development skills

---

## Learning Goals

### Tier 1 Focus
- Document preprocessing
- Chunking strategies
- Retrieval fundamentals

### Tier 2 Focus
- Vector databases (Qdrant, Pinecone, FAISS)
- Embedding models (OpenAI, Hugging Face)
- LangChain for RAG
- LlamaIndex basics
- RAG evaluation metrics

### Tier 3 Focus
- MCP (Model Context Protocol)
- Advanced retrieval (hybrid, reranking)
- Production RAG patterns
- Scaling considerations

---

## Main Project: Production RAG System

Build a RAG system that:
1. Ingests documents (PDF, MD, HTML)
2. Chunks intelligently
3. Creates and stores embeddings
4. Retrieves relevant context
5. Generates grounded answers
6. Evaluates with golden sets

### Deliverables

1. **`rag/ingest.py`** - Document ingestion
2. **`rag/retrieve.py`** - Retrieval pipeline
3. **`rag/answer.py`** - Answer generation
4. **`eval/`** - Evaluation harness
5. **`api/`** - RAG API service
6. **`docs/`** - Architecture documentation

### Definition of Done

- [ ] Ingestion handles PDF, MD, HTML
- [ ] Configurable chunking strategy
- [ ] Vector store integration working
- [ ] Retrieval achieves Hits@5 >70%
- [ ] Answer accuracy >60% on golden set
- [ ] API endpoint for queries
- [ ] Evaluation metrics documented

---

## Week-by-Week Plan

### Week 1: Document Processing & Chunking

**Focus**: Prepare documents for retrieval.

- Document parsing (PDF, MD, HTML)
- Chunking strategies (fixed, semantic, recursive)
- Metadata extraction
- Chunking experiments

**Milestone**: Documents chunked with metadata preserved.

### Week 2: Embeddings & Vector Stores

**Focus**: Build the retrieval layer.

- Embedding model selection
- Vector database setup (Qdrant)
- Indexing pipeline
- Similarity search

**Milestone**: Documents indexed, basic retrieval working.

### Week 3: Retrieval & Generation

**Focus**: Complete the RAG pipeline.

- Retrieval optimization
- Prompt engineering for generation
- Context formatting
- LangChain/LlamaIndex integration

**Milestone**: End-to-end RAG pipeline working.

### Week 4: Evaluation & Production

**Focus**: Make it production-ready.

- Golden set creation
- Evaluation metrics (retrieval + answer)
- API development
- Error handling
- Documentation

**Milestone**: Production RAG with evaluation harness.

---

## Stretch Goals

- Add hybrid search (vector + keyword)
- Implement reranking
- Add citation tracking
- Build streaming responses
- Implement query expansion

---

## Claude Prompts

### Planning
```
/plan-week
```

### RAG Best Practices
```
Use the RAG with Evals skill for building my retrieval system.
```

### Chunking Help
```
/debug-learning

I'm confused about chunking strategies. My retrieval quality is poor.
```

### Evaluation Design
```
As the Evaluator, help me create a golden set for RAG evaluation.
```

### Production Review
```
/harden

Review my RAG system for production readiness.
```

---

## How to Publish

### Demo Script
```python
# demo.py
from rag import RAGSystem

rag = RAGSystem.load("config.yaml")
answer = rag.query("How do I configure the system?")
print(f"Answer: {answer.text}")
print(f"Sources: {[s.title for s in answer.sources]}")
```

### Write-Up Topics
- Building RAG from scratch
- Chunking strategy comparison
- Vector database selection
- RAG evaluation methodology

---

## Resources

- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [RAG Best Practices (Anthropic)](https://docs.anthropic.com/claude/docs/retrieval-augmented-generation)
- Template: `templates/template-rag-service/`
- Skill: `.claude/skills/rag-with-evals.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 7
```
