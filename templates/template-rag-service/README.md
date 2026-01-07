# RAG Service Template

A minimal template for building Retrieval-Augmented Generation (RAG) services.

## Features

- Document ingestion and chunking
- Vector store with FAISS
- Semantic search
- LLM integration ready
- FastAPI endpoints
- Tests included

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Ingest documents
python -m rag.ingest --docs-dir ./documents

# Run the server
uvicorn rag.api:app --reload

# Run tests
pytest
```

## Project Structure

```
template-rag-service/
├── rag/
│   ├── __init__.py
│   ├── api.py            # FastAPI endpoints
│   ├── ingest.py         # Document ingestion
│   ├── chunker.py        # Text chunking
│   ├── embedder.py       # Embedding generation
│   ├── retriever.py      # Vector search
│   └── generator.py      # LLM response generation
├── tests/
│   ├── __init__.py
│   └── test_rag.py       # RAG tests
├── documents/            # Sample documents
├── pyproject.toml
└── README.md
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/ingest` | POST | Ingest a document |
| `/search` | POST | Semantic search |
| `/query` | POST | RAG query (search + generate) |
| `/documents` | GET | List indexed documents |

## Usage

### Ingesting Documents

```bash
# From CLI
python -m rag.ingest --docs-dir ./documents

# Via API
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{"text": "Your document content here", "metadata": {"source": "manual"}}'
```

### Querying

```python
import requests

# Semantic search only
response = requests.post(
    "http://localhost:8000/search",
    json={"query": "What is machine learning?", "top_k": 5}
)
print(response.json()["results"])

# Full RAG query (requires LLM config)
response = requests.post(
    "http://localhost:8000/query",
    json={"question": "Explain machine learning"}
)
print(response.json()["answer"])
```

## Configuration

Environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `EMBEDDING_MODEL` | Sentence transformer model | `all-MiniLM-L6-v2` |
| `CHUNK_SIZE` | Characters per chunk | `500` |
| `CHUNK_OVERLAP` | Overlap between chunks | `50` |
| `TOP_K` | Default results to return | `5` |
| `VECTOR_STORE_PATH` | Path to vector store | `./vector_store` |

## Customization

### Using a Different Embedding Model

Update the `EMBEDDING_MODEL` environment variable or modify `rag/embedder.py`.

### Adding LLM Generation

The template includes a placeholder for LLM integration. Implement your preferred LLM in `rag/generator.py`:

```python
# Example with OpenAI (add openai to dependencies)
import openai

def generate_response(context: str, question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
```

## License

MIT
