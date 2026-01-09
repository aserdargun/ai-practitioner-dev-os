# Month 06: NLP & Embeddings

## Why It Matters

Natural Language Processing powers chatbots, search, and LLM applications. This month builds your understanding of text processing, embeddings, and modern transformer-based NLP.

**Job Relevance**: NLP skills are in high demand. Understanding embeddings and transformers is essential for LLM-based applications.

---

## Prerequisites

- Month 01-05 completed
- PyTorch proficiency
- Deep learning fundamentals

---

## Learning Goals

### Tier 1 Focus
- Text preprocessing
- NLTK for NLP basics
- Word embeddings (Word2Vec, GloVe, FastText)
- Text classification
- Sentiment analysis

### Tier 2 Focus
- Hugging Face Transformers
- BERT, GPT, T5 architectures
- Fine-tuning pre-trained models
- Embeddings for similarity
- LangChain introduction

### Tier 3 Preview
- Large language models
- Prompt engineering
- Efficient fine-tuning (LoRA, QLoRA)

---

## Main Project: Text Classification & Similarity System

Build an NLP system that:
1. Preprocesses text data
2. Creates embeddings with multiple methods
3. Fine-tunes a transformer for classification
4. Builds a semantic similarity search
5. Evaluates and compares approaches

### Deliverables

1. **`preprocessing/`** - Text cleaning and tokenization
2. **`embeddings/`** - Embedding generation code
3. **`models/`** - Fine-tuned transformer
4. **`similarity/`** - Semantic search implementation
5. **`eval/`** - Evaluation scripts
6. **`demo.py`** - Interactive demo

### Definition of Done

- [ ] Text preprocessing pipeline
- [ ] Word2Vec/GloVe embeddings working
- [ ] Transformer fine-tuned for classification
- [ ] Semantic similarity search with BERT embeddings
- [ ] Evaluation metrics documented
- [ ] Demo showing all capabilities

---

## Week-by-Week Plan

### Week 1: Text Preprocessing & Classical NLP

**Focus**: Foundation of text processing.

- Tokenization and normalization
- NLTK for NLP tasks
- TF-IDF representations
- Basic text classification
- Regular expressions for text

**Milestone**: Text preprocessing pipeline and TF-IDF baseline.

### Week 2: Word Embeddings

**Focus**: Semantic representations.

- Word2Vec (skip-gram, CBOW)
- GloVe embeddings
- FastText for OOV handling
- Embedding visualization
- Similarity computations

**Milestone**: Embeddings trained/loaded, similarity working.

### Week 3: Transformers & Fine-tuning

**Focus**: Modern NLP with Hugging Face.

- Transformer architecture basics
- Hugging Face ecosystem
- BERT for classification
- Fine-tuning strategies
- Model evaluation

**Milestone**: Fine-tuned BERT classifier achieving target metrics.

### Week 4: Similarity Search & Integration

**Focus**: Practical applications.

- Sentence embeddings
- Semantic similarity search
- Vector similarity (cosine, dot product)
- LangChain introduction
- Full system integration

**Milestone**: Complete NLP system with search and classification.

---

## Stretch Goals

- Add named entity recognition
- Implement summarization
- Try different transformer architectures
- Add multilingual support
- Build question-answering system

---

## Claude Prompts

### Planning
```
/plan-week
```

### NLP Best Practices
```
As the Researcher, what are the best practices for text preprocessing?
```

### Fine-tuning Help
```
As the Builder, help me fine-tune BERT for my classification task.
```

### Model Evaluation
```
Use the Experiment Plan skill to compare embedding methods.
```

### Review
```
/harden

Review my NLP pipeline for best practices.
```

---

## How to Publish

### Demo Script
```python
# demo.py
from embeddings import get_embedding
from models import TextClassifier
from similarity import SemanticSearch

# Classification
classifier = TextClassifier.load("models/bert_classifier")
text = "This product is amazing!"
label = classifier.predict(text)
print(f"Sentiment: {label}")

# Similarity
search = SemanticSearch.load("similarity/index")
results = search.find_similar("machine learning algorithms")
print(f"Similar documents: {results}")
```

### Write-Up Topics
- Evolution of text representations
- Fine-tuning transformers for classification
- Building semantic search systems
- Comparing embedding methods

---

## Resources

- [Hugging Face Course](https://huggingface.co/course)
- [NLTK Book](https://www.nltk.org/book/)
- [Jay Alammar's Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [LangChain Docs](https://python.langchain.com/)

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 6
```
