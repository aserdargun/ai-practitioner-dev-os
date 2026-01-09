# RAG Service Template

A minimal Retrieval-Augmented Generation (RAG) service template with evaluation support.

## Features

- Document ingestion and chunking
- Vector-based retrieval
- Answer generation with citations
- Evaluation harness with golden set
- Modular, testable design

## Quick Start

```bash
# Install dependencies
pip install -e .

# Ingest documents
python rag/ingest.py --input docs/ --output index/

# Query the system
python rag/answer.py --query "What is RAG?"

# Run evaluations
python -m pytest tests/ -v
```

## Project Structure

```
template-rag-service/
├── rag/
│   ├── ingest.py        # Document ingestion
│   ├── retrieve.py      # Vector retrieval
│   └── answer.py        # Answer generation
├── eval/
│   └── golden_set.jsonl # Evaluation data
├── tests/
│   └── test_retrieve.py # Retrieval tests
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## Running Tests

```bash
pytest tests/ -v
```

## RAG Pipeline

### 1. Ingestion

```python
from rag.ingest import DocumentIngester

ingester = DocumentIngester(chunk_size=500, overlap=50)
chunks = ingester.ingest_file("document.txt")
```

### 2. Retrieval

```python
from rag.retrieve import Retriever

retriever = Retriever(index_path="index/")
results = retriever.search("What is RAG?", top_k=5)
```

### 3. Answer Generation

```python
from rag.answer import RAGAnswerer

answerer = RAGAnswerer(retriever)
response = answerer.answer("What is RAG?")
print(response.answer)
print(response.sources)
```

## Evaluation

The `eval/golden_set.jsonl` contains test cases:

```json
{"query": "What is RAG?", "expected_answer": "...", "expected_sources": [...]}
```

Run evaluation:

```bash
python rag/answer.py --eval eval/golden_set.jsonl
```

## Customization

1. **Embeddings**: Replace mock embeddings in `retrieve.py` with real embeddings (OpenAI, sentence-transformers)
2. **LLM**: Replace mock generation in `answer.py` with actual LLM calls
3. **Vector Store**: Swap mock store with ChromaDB, Pinecone, etc.
4. **Chunking**: Adjust chunk size and overlap in `ingest.py`

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `CHUNK_SIZE` | Characters per chunk | `500` |
| `CHUNK_OVERLAP` | Overlap between chunks | `50` |
| `TOP_K` | Retrieved documents | `5` |
| `MODEL_NAME` | LLM model name | `gpt-3.5-turbo` |
