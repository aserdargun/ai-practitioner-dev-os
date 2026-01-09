# Skill: RAG with Evals

Build a Retrieval-Augmented Generation system with proper evaluation.

## Trigger

Use this skill when:
- Building a Q&A system over documents
- Creating a knowledge base chatbot
- Implementing semantic search
- Need LLM to answer from your data

## Prerequisites

- Document corpus to index
- LLM API access (OpenAI, Anthropic, etc.)
- Vector database or embedding store
- Golden set of Q&A pairs for evaluation

## Steps

### 1. Prepare Documents (20 min)

```python
from pathlib import Path

def load_documents(directory):
    """Load documents from a directory."""
    documents = []
    for file_path in Path(directory).glob("**/*.md"):
        with open(file_path, 'r') as f:
            documents.append({
                'content': f.read(),
                'source': str(file_path),
            })
    return documents

documents = load_documents("./docs")
print(f"Loaded {len(documents)} documents")
```

### 2. Chunk Documents (15 min)

```python
def chunk_document(doc, chunk_size=500, overlap=50):
    """Split document into overlapping chunks."""
    content = doc['content']
    chunks = []

    start = 0
    while start < len(content):
        end = start + chunk_size
        chunk_text = content[start:end]

        chunks.append({
            'content': chunk_text,
            'source': doc['source'],
            'chunk_id': len(chunks),
        })

        start = end - overlap

    return chunks

all_chunks = []
for doc in documents:
    all_chunks.extend(chunk_document(doc))

print(f"Created {len(all_chunks)} chunks")
```

### 3. Create Embeddings (20 min)

```python
import openai

def get_embeddings(texts, model="text-embedding-ada-002"):
    """Get embeddings for a list of texts."""
    response = openai.embeddings.create(
        model=model,
        input=texts
    )
    return [item.embedding for item in response.data]

# Batch embedding
batch_size = 100
embeddings = []
for i in range(0, len(all_chunks), batch_size):
    batch = [c['content'] for c in all_chunks[i:i+batch_size]]
    embeddings.extend(get_embeddings(batch))

# Attach embeddings to chunks
for chunk, embedding in zip(all_chunks, embeddings):
    chunk['embedding'] = embedding
```

### 4. Index in Vector Store (15 min)

```python
# Simple in-memory store (use Pinecone, Qdrant, etc. for production)
import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = None

    def add(self, chunks):
        self.chunks = chunks
        self.embeddings = np.array([c['embedding'] for c in chunks])

    def search(self, query_embedding, top_k=5):
        query = np.array(query_embedding)
        # Cosine similarity
        similarities = np.dot(self.embeddings, query) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query)
        )
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [(self.chunks[i], similarities[i]) for i in top_indices]

store = SimpleVectorStore()
store.add(all_chunks)
```

### 5. Build RAG Pipeline (20 min)

```python
def rag_query(question, store, llm_model="gpt-4"):
    """Full RAG pipeline."""

    # Step 1: Embed query
    query_embedding = get_embeddings([question])[0]

    # Step 2: Retrieve relevant chunks
    results = store.search(query_embedding, top_k=5)

    # Step 3: Build context
    context = "\n\n---\n\n".join([
        f"Source: {r[0]['source']}\n{r[0]['content']}"
        for r in results
    ])

    # Step 4: Generate answer
    prompt = f"""Answer the question based on the context below.
If the context doesn't contain the answer, say "I don't have enough information."

Context:
{context}

Question: {question}

Answer:"""

    response = openai.chat.completions.create(
        model=llm_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return {
        'question': question,
        'answer': response.choices[0].message.content,
        'sources': [r[0]['source'] for r in results],
        'context_used': context,
    }
```

### 6. Create Golden Set (15 min)

```python
# Create evaluation dataset
golden_set = [
    {
        "question": "What is the purpose of the /status command?",
        "expected_answer": "Display current progress snapshot",
        "expected_sources": [".claude/commands/status.md"],
    },
    {
        "question": "How do I add a best practice?",
        "expected_answer": "Use the /add-best-practice command",
        "expected_sources": [".claude/commands/add-best-practice.md"],
    },
    # Add 10-20 Q&A pairs
]

# Save as JSONL
import json
with open("eval/golden_set.jsonl", "w") as f:
    for item in golden_set:
        f.write(json.dumps(item) + "\n")
```

### 7. Evaluate RAG System (30 min)

```python
def evaluate_rag(store, golden_set):
    """Evaluate RAG system on golden set."""
    results = []

    for item in golden_set:
        response = rag_query(item['question'], store)

        # Retrieval evaluation
        retrieved_sources = set(response['sources'])
        expected_sources = set(item['expected_sources'])
        retrieval_hit = len(retrieved_sources & expected_sources) > 0

        # Answer evaluation (simplified - use LLM judge for better)
        answer_contains_key_info = any(
            keyword.lower() in response['answer'].lower()
            for keyword in item['expected_answer'].split()[:3]
        )

        results.append({
            'question': item['question'],
            'retrieval_hit': retrieval_hit,
            'answer_quality': answer_contains_key_info,
            'generated_answer': response['answer'],
            'expected_answer': item['expected_answer'],
        })

    # Aggregate metrics
    retrieval_accuracy = sum(r['retrieval_hit'] for r in results) / len(results)
    answer_accuracy = sum(r['answer_quality'] for r in results) / len(results)

    print(f"Retrieval Accuracy: {retrieval_accuracy:.1%}")
    print(f"Answer Quality: {answer_accuracy:.1%}")

    return results

eval_results = evaluate_rag(store, golden_set)
```

### 8. Iterate and Improve (ongoing)

Based on evaluation:
- **Low retrieval**: Adjust chunk size, overlap, or embedding model
- **Low answer quality**: Improve prompts, use better LLM
- **Specific failures**: Add to golden set and debug

## Artifacts Produced

- [ ] `rag/ingest.py` — Document loading and chunking
- [ ] `rag/retrieve.py` — Vector search
- [ ] `rag/answer.py` — LLM generation
- [ ] `eval/golden_set.jsonl` — Evaluation dataset
- [ ] `eval/run_evals.py` — Evaluation script
- [ ] `rag_metrics.json` — Latest evaluation results

## Quality Bar

- [ ] At least 80% retrieval accuracy on golden set
- [ ] At least 70% answer quality on golden set
- [ ] Sources included in responses
- [ ] "Don't know" responses for out-of-scope questions
- [ ] Golden set has 10+ diverse questions
- [ ] Evaluation is automated and reproducible

## Common Pitfalls

1. **Chunks too large**
   - LLM can't process; retrieval less precise

2. **No evaluation**
   - You don't know if it's working

3. **Ignoring retrieval failures**
   - Check what's being retrieved, not just answers

4. **Hallucination**
   - Add "don't know" handling and source citation

5. **Golden set too easy**
   - Include edge cases and adversarial queries
