# Month 07: RAG Systems

**Focus**: Build a Retrieval-Augmented Generation system with proper evaluation.

---

## Why It Matters

RAG is the dominant pattern for building knowledge-grounded LLM applications. Understanding retrieval, embedding, and evaluation is essential for building systems that provide accurate, sourced answers rather than hallucinations.

**Job Relevance**: Critical skill for AI engineers; high-value project type for portfolios.

---

## Prerequisites

- Month 01-06 complete
- LangChain basics
- Understanding of embeddings

---

## Learning Goals

**Tier 2 Technologies**:
- RAG Systems (primary focus)
- Vector databases (Pinecone, Qdrant, Chroma)
- LlamaIndex
- Embedding models
- Evaluation frameworks

**Skills**:
- Document chunking
- Vector search
- Retrieval evaluation
- RAG evaluation

---

## Main Project: Document Q&A System

Build a Q&A system over a document corpus with retrieval and generation evaluation.

### Deliverables

1. **Document Ingestion Pipeline** with chunking
2. **Vector Store** with indexed documents
3. **RAG Chain** for question answering
4. **Evaluation Suite** with golden set
5. **GitHub Repository** with full documentation

### Definition of Done

- [ ] Documents chunked appropriately
- [ ] Embeddings generated and stored
- [ ] Vector search working
- [ ] RAG chain generates answers
- [ ] Source citations included
- [ ] Golden set of 20+ Q&A pairs
- [ ] Retrieval metrics computed (precision, recall)
- [ ] Generation quality evaluated
- [ ] "I don't know" handling tested
- [ ] Documentation complete

---

## Stretch Goals

- [ ] Hybrid search (semantic + keyword)
- [ ] Re-ranking implementation
- [ ] Multiple embedding models compared
- [ ] Deployed as API

---

## Weekly Cadence

### Week 1: Document Processing
- Document loading
- Chunking strategies
- Embedding generation
- Vector store setup

### Week 2: RAG Implementation
- Build retrieval chain
- Add generation
- Source citation
- Basic testing

### Week 3: Evaluation
- Create golden set
- Evaluate retrieval
- Evaluate generation
- Iterate on issues

### Week 4: Polish & Ship
- Handle edge cases
- Final evaluation
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 7 on RAG systems. I have a corpus of technical documentation.
Help me plan the ingestion and evaluation strategy.
```

### Skill Application
```
Apply the RAG with Evals skill to my project.
I want to make sure I'm building this correctly.
```

### Building
```
/ship-mvp

My RAG system has:
- 500 documents ingested
- Chroma vector store
- Basic retrieval and generation
Retrieval precision is 65%. How can I improve?
```

### Debugging
```
/debug-learning

My RAG is returning wrong answers even when the correct
information is in the corpus. I think it's a retrieval issue.
How do I debug this?
```

---

## How to Publish

### Demo
- Show Q&A in action
- Demonstrate source citations
- Show evaluation metrics

### Write-up
- "Building RAG That Actually Works"
- Focus on evaluation approach
- Share retrieval optimization insights

---

## Resources

### Templates
- [RAG Template](../../../templates/template-rag-service/)

### Skill Playbooks
- [RAG with Evals](../../../.claude/skills/rag-with-evals.md)

### Documentation
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Chroma Documentation](https://docs.trychroma.com/)
- [Pinecone Documentation](https://docs.pinecone.io/)

---

## Next Month Preview

**Month 08**: MLOps Foundations — Build end-to-end ML pipelines with Airflow and MLflow.
