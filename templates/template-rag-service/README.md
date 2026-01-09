# RAG Service Template

A minimal Retrieval-Augmented Generation (RAG) service template with built-in evaluation.

## What This Template Provides

- Document ingestion pipeline
- Vector store retrieval
- Answer generation with context
- Evaluation framework with golden set
- Test setup with pytest

## Quick Start

### 1. Install Dependencies

```bash
cd template-rag-service
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
pytest
```

### 3. Ingest Documents

```bash
python -m rag.ingest --input docs/
```

### 4. Query the System

```python
from rag.retrieve import Retriever
from rag.answer import AnswerGenerator

retriever = Retriever()
generator = AnswerGenerator()

# Retrieve relevant documents
docs = retriever.search("What is machine learning?", top_k=3)

# Generate answer
answer = generator.generate(query="What is machine learning?", context=docs)
print(answer)
```

## Project Structure

```
template-rag-service/
├── rag/
│   ├── ingest.py         # Document ingestion
│   ├── retrieve.py       # Vector search
│   └── answer.py         # Answer generation
├── eval/
│   └── golden_set.jsonl  # Evaluation dataset
├── tests/
│   └── test_retrieve.py  # Test suite
├── pyproject.toml        # Dependencies and tooling
└── README.md
```

## RAG Pipeline

```
Documents → Chunk → Embed → Index → Query → Retrieve → Generate Answer
```

### 1. Ingest
- Load documents
- Split into chunks
- Generate embeddings
- Store in vector index

### 2. Retrieve
- Embed user query
- Search vector index
- Return top-k relevant chunks

### 3. Answer
- Combine query with retrieved context
- Generate answer using LLM
- Return with source citations

## Customization

### Document Chunking

Edit `rag/ingest.py`:

```python
def chunk_document(text: str, chunk_size: int = 500, overlap: int = 50):
    """Split document into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks
```

### Embedding Model

Edit `rag/retrieve.py`:

```python
# Option 1: Use sentence-transformers
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Option 2: Use OpenAI
import openai
def embed(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding
```

### Answer Generation

Edit `rag/answer.py`:

```python
# Using OpenAI
import openai

def generate_answer(query: str, context: list[str]) -> str:
    context_text = "\n\n".join(context)
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Answer based on the context provided."},
            {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
        ]
    )
    return response.choices[0].message.content
```

## Evaluation

### Golden Set Format

`eval/golden_set.jsonl`:
```json
{"query": "What is Python?", "expected_answer": "A programming language", "relevant_docs": ["doc1.txt"]}
{"query": "How to install pip?", "expected_answer": "Use get-pip.py or package manager", "relevant_docs": ["doc2.txt"]}
```

### Running Evaluation

```python
from rag.retrieve import Retriever
from rag.answer import AnswerGenerator
import json

retriever = Retriever()
generator = AnswerGenerator()

# Load golden set
with open("eval/golden_set.jsonl") as f:
    golden = [json.loads(line) for line in f]

# Evaluate
results = []
for item in golden:
    docs = retriever.search(item["query"])
    answer = generator.generate(item["query"], docs)
    results.append({
        "query": item["query"],
        "expected": item["expected_answer"],
        "actual": answer,
        "retrieved_docs": [d["source"] for d in docs]
    })
```

### Metrics

- **Retrieval Recall**: % of relevant docs retrieved
- **Answer Accuracy**: Semantic similarity to expected answer
- **Faithfulness**: Answer grounded in retrieved context

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Embedding model |
| `CHUNK_SIZE` | `500` | Document chunk size |
| `TOP_K` | `5` | Number of docs to retrieve |
| `LLM_MODEL` | `gpt-4` | LLM for answer generation |

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=rag

# Run specific test
pytest tests/test_retrieve.py -v
```

## Production Checklist

- [ ] Set up document ingestion pipeline
- [ ] Configure embedding model
- [ ] Test retrieval quality
- [ ] Set up answer generation
- [ ] Create golden evaluation set
- [ ] Run evaluation metrics
- [ ] Add logging and monitoring
- [ ] Deploy and test at scale

## Resources

- [LangChain RAG](https://python.langchain.com/docs/tutorials/rag/)
- [LlamaIndex](https://docs.llamaindex.ai/)
- [ChromaDB](https://docs.trychroma.com/)
- [RAGAS Evaluation](https://docs.ragas.io/)
