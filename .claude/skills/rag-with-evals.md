# Skill: RAG with Evals

**Tier**: 1-2 (Beginner to Intermediate)

Build a Retrieval-Augmented Generation system with proper evaluation.

---

## Trigger

Use this skill when:
- Building Q&A over documents
- Need LLM with custom knowledge
- Creating a chatbot with domain expertise

## Prerequisites

- [ ] Document corpus (PDFs, text files, etc.)
- [ ] OpenAI API key or similar LLM access
- [ ] Python environment with required packages

## Steps

### Step 1: Set Up Environment (10 min)

```python
# Install required packages
# pip install langchain openai chromadb tiktoken

import os
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Set API key
os.environ["OPENAI_API_KEY"] = "your-key-here"  # Use env var in production!
```

**Checkpoint**: Environment set up with required packages.

### Step 2: Load and Chunk Documents (15 min)

```python
# Load documents
loader = DirectoryLoader(
    './documents/',
    glob="**/*.txt",
    loader_cls=TextLoader
)
documents = loader.load()
print(f"Loaded {len(documents)} documents")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")

# Preview a chunk
print(f"\nSample chunk:\n{chunks[0].page_content[:500]}...")
```

**Checkpoint**: Documents loaded and chunked appropriately.

### Step 3: Create Vector Store (10 min)

```python
# Create embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Test retrieval
query = "What is the main topic?"
docs = vectorstore.similarity_search(query, k=3)
print(f"Retrieved {len(docs)} documents for query: '{query}'")
for i, doc in enumerate(docs):
    print(f"\n--- Doc {i+1} ---\n{doc.page_content[:200]}...")
```

**Checkpoint**: Vector store created and retrieval working.

### Step 4: Build RAG Chain (10 min)

```python
# Create LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Test the chain
result = qa_chain({"query": "What is the main topic of these documents?"})
print(f"Answer: {result['result']}")
print(f"\nSources: {len(result['source_documents'])} documents")
```

**Checkpoint**: RAG chain working end-to-end.

### Step 5: Create Evaluation Dataset (20 min)

Create `golden_set.jsonl`:

```json
{"question": "What is X?", "expected_answer": "X is...", "context_should_contain": "relevant keywords"}
{"question": "How do you do Y?", "expected_answer": "To do Y, you...", "context_should_contain": "step, process"}
{"question": "When was Z introduced?", "expected_answer": "Z was introduced in...", "context_should_contain": "date, year"}
```

```python
import json

# Load golden set
golden_set = []
with open('golden_set.jsonl', 'r') as f:
    for line in f:
        golden_set.append(json.loads(line))

print(f"Loaded {len(golden_set)} evaluation examples")
```

**Checkpoint**: Golden evaluation set created (10-20 examples minimum).

### Step 6: Run Evaluation (20 min)

```python
from typing import List, Dict
import re

def evaluate_rag(qa_chain, golden_set: List[Dict]) -> Dict:
    results = []

    for item in golden_set:
        question = item['question']
        expected = item['expected_answer']
        context_keywords = item.get('context_should_contain', '').split(', ')

        # Get RAG response
        response = qa_chain({"query": question})
        answer = response['result']
        sources = response['source_documents']

        # Evaluate retrieval (context relevance)
        context_text = ' '.join([doc.page_content for doc in sources])
        keywords_found = sum(1 for kw in context_keywords if kw.lower() in context_text.lower())
        retrieval_score = keywords_found / len(context_keywords) if context_keywords else 1

        # Evaluate answer (simple keyword overlap - use LLM grader for production)
        expected_words = set(expected.lower().split())
        answer_words = set(answer.lower().split())
        overlap = len(expected_words & answer_words) / len(expected_words) if expected_words else 0

        results.append({
            'question': question,
            'expected': expected,
            'actual': answer,
            'retrieval_score': retrieval_score,
            'answer_score': overlap
        })

    # Aggregate metrics
    avg_retrieval = sum(r['retrieval_score'] for r in results) / len(results)
    avg_answer = sum(r['answer_score'] for r in results) / len(results)

    return {
        'num_examples': len(results),
        'avg_retrieval_score': avg_retrieval,
        'avg_answer_score': avg_answer,
        'detailed_results': results
    }

# Run evaluation
eval_results = evaluate_rag(qa_chain, golden_set)
print(f"\nEvaluation Results:")
print(f"  Retrieval Score: {eval_results['avg_retrieval_score']:.2%}")
print(f"  Answer Score: {eval_results['avg_answer_score']:.2%}")
```

**Checkpoint**: Evaluation pipeline working with metrics.

### Step 7: Document Results (10 min)

```markdown
## RAG System Evaluation: [Project Name]

### System Configuration
- Embedding model: OpenAI text-embedding-ada-002
- LLM: GPT-3.5-turbo
- Chunk size: 1000 tokens
- Chunk overlap: 200 tokens
- Retrieved docs: 3

### Corpus Statistics
- Documents: X
- Chunks: Y
- Avg chunk length: Z tokens

### Evaluation Results

| Metric | Score |
|--------|-------|
| Retrieval Relevance | X% |
| Answer Quality | Y% |

### Sample Results
| Question | Expected | Actual | Score |
|----------|----------|--------|-------|
| Q1 | ... | ... | X% |
| Q2 | ... | ... | Y% |

### Failure Analysis
- [Pattern 1]: [Description and fix]
- [Pattern 2]: [Description and fix]

### Recommendations
1. [Improvement 1]
2. [Improvement 2]
```

**Checkpoint**: Results documented with clear metrics.

## Artifacts Produced

- [ ] Vector store (persisted)
- [ ] RAG chain code
- [ ] Golden evaluation set (JSONL)
- [ ] Evaluation script
- [ ] Results documentation

## Quality Bar

✅ **Done when**:
- RAG answers questions correctly
- Retrieval returns relevant chunks
- Evaluation set has 10+ examples
- Metrics are documented
- Failure cases analyzed

## Common Pitfalls

- **No evaluation**: Always measure before claiming success
- **Small chunks**: Chunks too small lose context
- **Large chunks**: Chunks too large dilute relevance
- **Wrong k**: Too few docs miss info; too many add noise

## Example Prompt

```
I want to build a Q&A system over our company documentation (50 markdown files).

Help me:
1. Set up the RAG pipeline
2. Create an evaluation dataset
3. Measure retrieval and answer quality

The docs cover product features, API reference, and troubleshooting guides.
```

## Related Skills

- [API Shipping Checklist](api-shipping-checklist.md) - Deploy RAG as API
- [EDA to Insight](eda-to-insight.md) - Analyze your corpus
