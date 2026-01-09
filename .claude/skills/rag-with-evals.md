# Skill: RAG with Evals

Build a Retrieval-Augmented Generation system with proper evaluation.

## Trigger

Use this skill when:
- Building Q&A over documents
- Creating chatbots with knowledge bases
- Augmenting LLMs with external data
- Need factual, grounded responses

## Prerequisites

- [ ] Document corpus prepared
- [ ] LLM API access (OpenAI, Anthropic, etc.)
- [ ] Vector database choice made
- [ ] Evaluation criteria defined

## Steps

### 1. Document Preparation (30 min)

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load documents
loader = DirectoryLoader('./documents', glob="**/*.md")
documents = loader.load()

# Chunk documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks from {len(documents)} documents")
```

**Document**:
- Source documents and format
- Chunking strategy rationale
- Chunk size and overlap decisions

### 2. Create Embeddings (20 min)

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma  # or FAISS, Pinecone, etc.

# Initialize embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create vector store
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./vectorstore"
)

# Persist
vectorstore.persist()
```

### 3. Build Retrieval (20 min)

```python
# Basic retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# Test retrieval
query = "What is the main topic?"
docs = retriever.get_relevant_documents(query)
for doc in docs:
    print(f"Score: {doc.metadata.get('score', 'N/A')}")
    print(f"Content: {doc.page_content[:200]}...")
    print("---")
```

**Retrieval options**:
- Similarity search (default)
- MMR (Maximum Marginal Relevance) for diversity
- Hybrid search (keyword + semantic)

### 4. Build Generation (20 min)

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Prompt template
template = """Use the following context to answer the question.
If you don't know the answer based on the context, say "I don't know."

Context:
{context}

Question: {question}

Answer:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# Build chain
llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

# Test
result = qa_chain({"query": "What is the main topic?"})
print(result["result"])
```

### 5. Create Evaluation Dataset (30 min)

```python
# Golden set format
golden_set = [
    {
        "question": "What is X?",
        "expected_answer": "X is...",
        "relevant_docs": ["doc1.md", "doc2.md"],
        "category": "factual"
    },
    # ... more examples
]

# Save as JSONL
import json
with open('eval/golden_set.jsonl', 'w') as f:
    for item in golden_set:
        f.write(json.dumps(item) + '\n')
```

**Target**: 20-50 representative questions covering:
- Factual recall
- Multi-hop reasoning
- Edge cases
- Questions that should return "I don't know"

### 6. Evaluate Retrieval (30 min)

```python
def evaluate_retrieval(retriever, golden_set):
    """Evaluate retrieval quality."""
    results = []

    for item in golden_set:
        retrieved = retriever.get_relevant_documents(item["question"])
        retrieved_ids = [doc.metadata.get("source") for doc in retrieved]

        # Calculate metrics
        relevant = set(item["relevant_docs"])
        retrieved_set = set(retrieved_ids)

        precision = len(relevant & retrieved_set) / len(retrieved_set) if retrieved_set else 0
        recall = len(relevant & retrieved_set) / len(relevant) if relevant else 0

        results.append({
            "question": item["question"],
            "precision": precision,
            "recall": recall,
            "retrieved": retrieved_ids
        })

    return results

# Aggregate metrics
avg_precision = sum(r["precision"] for r in results) / len(results)
avg_recall = sum(r["recall"] for r in results) / len(results)
```

### 7. Evaluate Generation (30 min)

```python
def evaluate_generation(qa_chain, golden_set):
    """Evaluate end-to-end RAG quality."""
    results = []

    for item in golden_set:
        response = qa_chain({"query": item["question"]})

        # Manual or LLM-based evaluation
        # Option 1: Exact match
        exact_match = response["result"].lower() == item["expected_answer"].lower()

        # Option 2: LLM-as-judge
        judge_prompt = f"""
        Question: {item["question"]}
        Expected: {item["expected_answer"]}
        Actual: {response["result"]}

        Rate the actual answer: correct, partially_correct, or incorrect
        """
        # ... call judge LLM

        results.append({
            "question": item["question"],
            "expected": item["expected_answer"],
            "actual": response["result"],
            "exact_match": exact_match
        })

    return results
```

### 8. Document Results (20 min)

```markdown
## RAG Evaluation Report

### Retrieval Metrics
- Precision@4: X.XX
- Recall@4: X.XX
- MRR: X.XX

### Generation Metrics
- Accuracy: X.XX
- Faithfulness: X.XX
- Relevance: X.XX

### Failure Analysis
- [Category 1]: X failures — [pattern observed]
- [Category 2]: X failures — [pattern observed]

### Recommendations
- [Improvement 1]
- [Improvement 2]
```

## Artifacts

| Artifact | Description |
|----------|-------------|
| `rag/ingest.py` | Document processing script |
| `rag/retrieve.py` | Retrieval logic |
| `rag/answer.py` | Generation chain |
| `eval/golden_set.jsonl` | Evaluation dataset |
| `eval/results.json` | Evaluation results |
| `rag_card.md` | System documentation |

## Quality Bar

- [ ] Golden set has 20+ diverse questions
- [ ] Retrieval precision > 70%
- [ ] Generation accuracy > 80%
- [ ] "I don't know" handling tested
- [ ] Source attribution working
- [ ] Failure modes documented

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 6-8 hours |
| Practiced | 3-4 hours |
| Expert | 2-3 hours |

## Common Pitfalls

- Not evaluating retrieval separately from generation
- Golden set too small or not representative
- Chunk size not tuned for content type
- No handling for out-of-scope questions
- Not testing with adversarial queries
