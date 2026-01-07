# RAG Service Template

A template for building Retrieval-Augmented Generation systems with evaluation.

## Features

- Document loading and chunking
- Vector store with Chroma
- RAG chain implementation
- RAGAS evaluation
- FastAPI serving

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Index documents
python -m src.index --docs-dir data/docs

# Run the service
uvicorn src.api:app --reload

# Run tests
pytest
```

## Project Structure

```
template-rag-service/
├── src/
│   ├── __init__.py
│   ├── api.py            # FastAPI endpoints
│   ├── rag.py            # RAG chain logic
│   ├── index.py          # Document indexing
│   ├── models.py         # Pydantic models
│   └── evaluation.py     # RAGAS evaluation
├── tests/
│   ├── __init__.py
│   └── test_rag.py
├── data/
│   ├── docs/             # Documents to index
│   └── chroma_db/        # Vector store
├── pyproject.toml
└── README.md
```

## Usage

### Index Documents

```bash
python -m src.index --docs-dir data/docs --persist-dir data/chroma_db
```

### Query via API

```bash
curl -X POST http://localhost:8000/query \
    -H "Content-Type: application/json" \
    -d '{"question": "What is the main topic?"}'
```

### Evaluate

```bash
python -m src.evaluation --eval-file data/eval_questions.json
```

## Configuration

Environment variables:
- `OPENAI_API_KEY`: OpenAI API key
- `CHROMA_PERSIST_DIR`: Path to Chroma database
- `CHUNK_SIZE`: Document chunk size (default: 1000)
- `CHUNK_OVERLAP`: Chunk overlap (default: 200)

## License

MIT
