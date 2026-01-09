# Skill: RAG with Evals

## Trigger

Use this skill when building a Retrieval-Augmented Generation system with proper evaluation.

## Prerequisites

- Document corpus available
- OpenAI API key (or alternative embedding/LLM provider)
- Vector database selected (Qdrant, Pinecone, FAISS, etc.)
- Python environment ready

**Level**: Intermediate+ (Tier 2)

## Steps

### 1. Document Preparation (30 min)

```python
from pathlib import Path
import json

def load_documents(source_dir: str) -> list[dict]:
    """Load documents from a directory."""
    docs = []
    for path in Path(source_dir).glob("**/*.md"):  # or *.txt, *.pdf
        content = path.read_text()
        docs.append({
            "id": str(path),
            "content": content,
            "metadata": {"source": str(path), "type": path.suffix}
        })
    return docs

documents = load_documents("./docs")
print(f"Loaded {len(documents)} documents")
```

### 2. Chunking Strategy (30 min)

```python
from typing import Iterator

def chunk_document(doc: dict, chunk_size: int = 500, overlap: int = 50) -> Iterator[dict]:
    """Chunk a document into smaller pieces."""
    content = doc["content"]
    start = 0
    chunk_idx = 0

    while start < len(content):
        end = start + chunk_size
        chunk_text = content[start:end]

        yield {
            "id": f"{doc['id']}_chunk_{chunk_idx}",
            "content": chunk_text,
            "metadata": {
                **doc["metadata"],
                "chunk_idx": chunk_idx,
                "parent_id": doc["id"]
            }
        }

        start = end - overlap
        chunk_idx += 1

# Chunk all documents
chunks = []
for doc in documents:
    chunks.extend(chunk_document(doc))

print(f"Created {len(chunks)} chunks from {len(documents)} documents")
```

**Chunking Decision Tree**:
- Start with 500 tokens, no overlap
- If answers cut off → bigger chunks (1000)
- If too much noise → smaller chunks (250)
- If missing context → add overlap (50-100)

### 3. Embedding Generation (20 min)

```python
from openai import OpenAI
import numpy as np

client = OpenAI()

def get_embeddings(texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    """Get embeddings for a list of texts."""
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]

# Batch embed chunks (API rate limits apply)
batch_size = 100
all_embeddings = []

for i in range(0, len(chunks), batch_size):
    batch = chunks[i:i + batch_size]
    batch_texts = [c["content"] for c in batch]
    embeddings = get_embeddings(batch_texts)
    all_embeddings.extend(embeddings)
    print(f"Embedded {min(i + batch_size, len(chunks))}/{len(chunks)}")

# Attach embeddings to chunks
for chunk, embedding in zip(chunks, all_embeddings):
    chunk["embedding"] = embedding
```

### 4. Vector Store Setup (30 min)

```python
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# Initialize client
client = QdrantClient(":memory:")  # or url="localhost:6333"

# Create collection
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

# Upload chunks
points = [
    PointStruct(
        id=i,
        vector=chunk["embedding"],
        payload={"content": chunk["content"], **chunk["metadata"]}
    )
    for i, chunk in enumerate(chunks)
]

client.upsert(collection_name="documents", points=points)
print(f"Indexed {len(points)} chunks")
```

### 5. Retrieval Function (20 min)

```python
def retrieve(query: str, top_k: int = 5) -> list[dict]:
    """Retrieve relevant chunks for a query."""
    # Embed query
    query_embedding = get_embeddings([query])[0]

    # Search
    results = client.search(
        collection_name="documents",
        query_vector=query_embedding,
        limit=top_k
    )

    return [
        {
            "content": hit.payload["content"],
            "score": hit.score,
            "source": hit.payload.get("source", "unknown")
        }
        for hit in results
    ]

# Test retrieval
results = retrieve("How do I configure the system?")
for r in results:
    print(f"[{r['score']:.3f}] {r['content'][:100]}...")
```

### 6. Answer Generation (20 min)

```python
def generate_answer(query: str, context: list[dict]) -> str:
    """Generate answer using retrieved context."""
    context_text = "\n\n".join([c["content"] for c in context])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Answer the question based on the provided context. If the context doesn't contain the answer, say so."
            },
            {
                "role": "user",
                "content": f"Context:\n{context_text}\n\nQuestion: {query}"
            }
        ]
    )

    return response.choices[0].message.content

def rag_query(query: str) -> dict:
    """Full RAG pipeline."""
    context = retrieve(query, top_k=5)
    answer = generate_answer(query, context)
    return {"query": query, "answer": answer, "sources": context}
```

### 7. Create Evaluation Dataset (30 min)

```python
# Create golden set for evaluation
golden_set = [
    {
        "query": "How do I configure the system?",
        "expected_answer": "Configuration is done via the config.yaml file...",
        "expected_sources": ["docs/configuration.md"]
    },
    {
        "query": "What are the system requirements?",
        "expected_answer": "Python 3.11+, 8GB RAM...",
        "expected_sources": ["docs/requirements.md"]
    },
    # Add 10-20 examples covering different topics
]

# Save golden set
with open("eval/golden_set.jsonl", "w") as f:
    for item in golden_set:
        f.write(json.dumps(item) + "\n")
```

### 8. Evaluation Metrics (30 min)

```python
from typing import Callable

def evaluate_retrieval(golden_set: list[dict]) -> dict:
    """Evaluate retrieval quality."""
    hits_at_5 = 0
    mrr_sum = 0

    for item in golden_set:
        results = retrieve(item["query"], top_k=5)
        sources = [r["source"] for r in results]

        # Check if expected source is in top 5
        for expected in item["expected_sources"]:
            if any(expected in s for s in sources):
                hits_at_5 += 1
                # MRR
                for i, s in enumerate(sources):
                    if expected in s:
                        mrr_sum += 1 / (i + 1)
                        break
                break

    return {
        "hits_at_5": hits_at_5 / len(golden_set),
        "mrr": mrr_sum / len(golden_set)
    }

def evaluate_answers(golden_set: list[dict], judge_fn: Callable = None) -> dict:
    """Evaluate answer quality."""
    correct = 0

    for item in golden_set:
        result = rag_query(item["query"])

        # Simple: check if expected answer is contained
        if item["expected_answer"].lower() in result["answer"].lower():
            correct += 1
        # Or use LLM-as-judge (if judge_fn provided)

    return {"accuracy": correct / len(golden_set)}

# Run evaluation
retrieval_metrics = evaluate_retrieval(golden_set)
answer_metrics = evaluate_answers(golden_set)

print(f"Retrieval - Hits@5: {retrieval_metrics['hits_at_5']:.2%}")
print(f"Retrieval - MRR: {retrieval_metrics['mrr']:.3f}")
print(f"Answer Accuracy: {answer_metrics['accuracy']:.2%}")
```

### 9. Document Results (15 min)

```markdown
## RAG System Evaluation Report

### Configuration
- Embedding Model: text-embedding-3-small
- Chunk Size: 500 tokens, 50 overlap
- Vector Store: Qdrant
- LLM: gpt-4o-mini

### Retrieval Metrics
| Metric | Score |
|--------|-------|
| Hits@5 | 85% |
| MRR | 0.72 |

### Answer Metrics
| Metric | Score |
|--------|-------|
| Accuracy | 78% |

### Error Analysis
- [Example of retrieval miss]
- [Example of answer error]

### Next Steps
- [ ] Try larger chunk size for long-form answers
- [ ] Add re-ranking step
- [ ] Experiment with different embeddings
```

## Artifacts Produced

- `rag/ingest.py` - Ingestion pipeline
- `rag/retrieve.py` - Retrieval function
- `rag/answer.py` - Answer generation
- `eval/golden_set.jsonl` - Evaluation dataset
- `eval/run_evals.py` - Evaluation script
- `rag_report.md` - Documentation

## Quality Bar

- [ ] Chunking strategy documented
- [ ] Golden set with 10+ examples
- [ ] Retrieval metrics: Hits@5 > 70%
- [ ] Answer accuracy > 60%
- [ ] Error analysis completed

## Common Pitfalls

1. **No evaluation** - Always measure retrieval + answer quality
2. **Wrong chunk size** - Test with real queries
3. **Ignoring metadata** - Source tracking is essential
4. **No golden set** - Can't improve what you don't measure
