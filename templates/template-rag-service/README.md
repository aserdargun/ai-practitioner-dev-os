# RAG Service Template

A Retrieval-Augmented Generation (RAG) service template with evaluation support.

## Features

- Document ingestion and chunking
- Vector-based retrieval
- LLM-powered answer generation
- Golden set evaluation
- Modular architecture

## Quick Start

```bash
# Install dependencies
pip install -e ".[all]"

# Ingest documents
python rag/ingest.py --input docs/ --output vectorstore/

# Run retrieval test
python rag/retrieve.py --query "What is RAG?"

# Generate answer
python rag/answer.py --query "Explain RAG in simple terms"

# Run evaluations
pytest tests/

# Run golden set evaluation
python eval/run_eval.py
```

## Project Structure

```
template-rag-service/
├── rag/
│   ├── ingest.py      # Document ingestion
│   ├── retrieve.py    # Vector retrieval
│   └── answer.py      # Answer generation
├── eval/
│   └── golden_set.jsonl
├── tests/
│   └── test_retrieve.py
├── pyproject.toml
└── README.md
```

## Architecture

```
Documents → Chunking → Embedding → Vector Store
                                       ↓
Query → Embedding → Similarity Search → Context
                                           ↓
                              LLM → Generated Answer
```

## Configuration

Environment variables:
- `OPENAI_API_KEY`: OpenAI API key (for embeddings/completion)
- `EMBEDDING_MODEL`: Embedding model name
- `COMPLETION_MODEL`: Completion model name
- `CHUNK_SIZE`: Document chunk size (default: 500)
- `CHUNK_OVERLAP`: Chunk overlap (default: 50)

## Evaluation

The template includes a golden set evaluation framework:

```jsonl
{"query": "What is RAG?", "expected_context": ["retrieval", "augmented"], "expected_answer_contains": ["retrieval"]}
```

Run evaluations:
```bash
python eval/run_eval.py --golden-set eval/golden_set.jsonl
```

## Customization

1. **Ingestion**: Modify `ingest.py` for your document formats
2. **Retrieval**: Adjust `retrieve.py` for your vector store
3. **Answer Generation**: Customize `answer.py` for your LLM
4. **Evaluation**: Add test cases to `eval/golden_set.jsonl`

## Usage in Curriculum

This template is used in:
- Month 06: RAG fundamentals
- Month 07: RAG with evaluations
- Month 11: Advanced LLM applications
