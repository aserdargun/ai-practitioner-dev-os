# Skill: RAG + Evaluation

Build Retrieval-Augmented Generation systems with proper evaluation.

---

## When to Use

- Building Q&A systems over documents
- Creating knowledge bases with LLM interfaces
- Implementing semantic search
- Evaluating retrieval and generation quality

---

## Prerequisites

```bash
pip install langchain langchain-openai chromadb sentence-transformers ragas
```

---

## The RAG Playbook

### Phase 1: Document Loading (10 minutes)

```python
from langchain.document_loaders import (
    TextLoader,
    PyPDFLoader,
    DirectoryLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load documents
loader = DirectoryLoader(
    "data/documents/",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)
documents = loader.load()

print(f"Loaded {len(documents)} documents")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")
```

### Phase 2: Embedding and Indexing (15 minutes)

```python
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="data/chroma_db"
)

# Persist
vectorstore.persist()
print("Vector store created and persisted")
```

### Phase 3: Retrieval Setup (10 minutes)

```python
# Create retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# Test retrieval
query = "What is the main topic of the documents?"
retrieved_docs = retriever.get_relevant_documents(query)

print(f"Retrieved {len(retrieved_docs)} documents")
for i, doc in enumerate(retrieved_docs):
    print(f"\n--- Document {i+1} ---")
    print(doc.page_content[:200] + "...")
```

### Phase 4: RAG Chain (15 minutes)

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create prompt template
template = """Answer the question based only on the following context:

Context:
{context}

Question: {question}

Answer the question directly and concisely. If the answer is not in the context, say "I don't have enough information to answer this question."
"""

prompt = ChatPromptTemplate.from_template(template)

# Helper to format docs
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Create RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Test the chain
response = rag_chain.invoke("What is the main topic?")
print(response)
```

### Phase 5: Evaluation Dataset (15 minutes)

Create a test dataset:

```python
# evaluation_data.py
evaluation_questions = [
    {
        "question": "What is the main purpose of the system?",
        "ground_truth": "The system is designed to...",
        "contexts": []  # Will be filled by retriever
    },
    {
        "question": "How does feature X work?",
        "ground_truth": "Feature X works by...",
        "contexts": []
    },
    # Add more questions...
]

# Generate contexts for each question
for item in evaluation_questions:
    docs = retriever.get_relevant_documents(item["question"])
    item["contexts"] = [doc.page_content for doc in docs]
    item["answer"] = rag_chain.invoke(item["question"])
```

### Phase 6: Evaluation with RAGAS (20 minutes)

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from datasets import Dataset

# Prepare dataset for RAGAS
eval_data = {
    "question": [item["question"] for item in evaluation_questions],
    "answer": [item["answer"] for item in evaluation_questions],
    "contexts": [item["contexts"] for item in evaluation_questions],
    "ground_truth": [item["ground_truth"] for item in evaluation_questions],
}

dataset = Dataset.from_dict(eval_data)

# Run evaluation
result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ],
)

print("Evaluation Results:")
print(result)

# Convert to DataFrame for analysis
df = result.to_pandas()
print("\nDetailed Results:")
print(df)
```

### Phase 7: Custom Metrics (Optional)

```python
def calculate_retrieval_metrics(questions, retriever, ground_truth_docs):
    """Calculate precision and recall for retrieval."""
    results = []

    for q, gt_docs in zip(questions, ground_truth_docs):
        retrieved = retriever.get_relevant_documents(q)
        retrieved_ids = set(doc.metadata.get("id") for doc in retrieved)
        gt_ids = set(gt_docs)

        precision = len(retrieved_ids & gt_ids) / len(retrieved_ids) if retrieved_ids else 0
        recall = len(retrieved_ids & gt_ids) / len(gt_ids) if gt_ids else 0

        results.append({
            "question": q,
            "precision": precision,
            "recall": recall,
            "f1": 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        })

    return results


def evaluate_answer_quality(question, answer, ground_truth, llm):
    """Use LLM to evaluate answer quality."""
    eval_prompt = f"""Evaluate the following answer on a scale of 1-5:

Question: {question}
Expected Answer: {ground_truth}
Actual Answer: {answer}

Score (1-5) and brief explanation:"""

    response = llm.invoke(eval_prompt)
    return response.content
```

---

## Checklist

- [ ] Documents loaded and chunked
- [ ] Embeddings generated
- [ ] Vector store created and persisted
- [ ] Retriever configured
- [ ] RAG chain built
- [ ] Evaluation dataset created
- [ ] RAGAS metrics computed
- [ ] Results analyzed
- [ ] Improvements identified

---

## Evaluation Metrics Explained

| Metric | What It Measures | Good Score |
|--------|-----------------|------------|
| **Faithfulness** | Is the answer grounded in context? | > 0.8 |
| **Answer Relevancy** | Does answer address the question? | > 0.8 |
| **Context Precision** | Are retrieved docs relevant? | > 0.7 |
| **Context Recall** | Are all needed docs retrieved? | > 0.7 |

---

## Common Improvements

1. **Low faithfulness**: Improve prompt to emphasize using only context
2. **Low relevancy**: Tune retriever k value, improve chunking
3. **Low precision**: Use reranking, improve embeddings
4. **Low recall**: Increase k, use hybrid search (BM25 + semantic)

---

## Production Considerations

- Cache embeddings for repeated queries
- Use async operations for better throughput
- Monitor latency: retrieval + generation time
- Log queries and responses for continuous improvement
- Implement feedback loops for human evaluation
