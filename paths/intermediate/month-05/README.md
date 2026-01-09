# Month 05: NLP Foundations

**Focus**: Process and classify text using modern NLP techniques.

---

## Why It Matters

Natural Language Processing is at the heart of LLMs, chatbots, search engines, and countless applications. Understanding text processing, embeddings, and classification is essential before diving into more advanced LLM work.

**Job Relevance**: High demand for NLP skills across all AI roles; foundation for LLM engineering.

---

## Prerequisites

- Month 01-04 complete
- Basic deep learning understanding
- Familiarity with PyTorch

---

## Learning Goals

**Tier 1 Technologies**:
- Text Mining
- NLTK (basics)
- Word2Vec, GloVe, FastText
- RNN, LSTM

**Tier 2 Technologies**:
- Hugging Face Transformers
- BERT, GPT concepts
- Embeddings
- GenSim

**Skills**:
- Text preprocessing
- Tokenization
- Embeddings and similarity
- Text classification

---

## Main Project: Text Classification System

Build a text classification system using both traditional and transformer-based approaches.

### Deliverables

1. **Text Preprocessing Pipeline** handling various text formats
2. **Traditional ML Classifier** (TF-IDF + sklearn)
3. **Transformer-based Classifier** (Hugging Face)
4. **Comparison Analysis** of approaches
5. **GitHub Repository** with documented code

### Definition of Done

- [ ] Dataset collected and cleaned
- [ ] Text preprocessing pipeline complete
- [ ] TF-IDF + Logistic Regression baseline
- [ ] BERT/DistilBERT classifier implemented
- [ ] Both models evaluated on same test set
- [ ] Comparison report written
- [ ] Inference code works on new text
- [ ] Tests for preprocessing
- [ ] Documentation complete
- [ ] Code is modular

---

## Stretch Goals

- [ ] Multi-label classification
- [ ] Model deployed as API
- [ ] Active learning for labeling
- [ ] Error analysis deep dive

---

## Weekly Cadence

### Week 1: Text Processing
- Text cleaning and normalization
- Tokenization approaches
- TF-IDF features
- Build baseline classifier

### Week 2: Embeddings & Transformers
- Word embeddings (Word2Vec)
- Introduction to Hugging Face
- Load and use pretrained models

### Week 3: Fine-tune Transformer
- Fine-tune BERT for classification
- Training and validation
- Hyperparameter tuning

### Week 4: Compare & Ship
- Evaluation and comparison
- Error analysis
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 5 on NLP. I want to build a sentiment classifier.
Help me plan the text processing and model comparison approach.
```

### Building
```
/ship-mvp

I have:
- TF-IDF baseline: 82% accuracy
- Fine-tuned DistilBERT: 91% accuracy
What should I include in my comparison analysis?
```

### Debugging
```
/debug-learning

My transformer model is much slower to train than expected.
I'm running on CPU. What are my options?
```

### Research
```
Researcher, help me understand the difference between
BERT, RoBERTa, and DistilBERT for text classification.
```

---

## How to Publish

### Demo
- Show classification on example texts
- Compare traditional vs transformer
- Demonstrate preprocessing

### Write-up
- "From TF-IDF to BERT: My NLP Journey"
- Include performance comparisons
- Discuss when to use each approach

---

## Resources

### Datasets
- IMDb Reviews (sentiment)
- AG News (topic classification)
- Custom dataset

### Documentation
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Hugging Face Course](https://huggingface.co/course)
- [NLTK Documentation](https://www.nltk.org/)

---

## Next Month Preview

**Month 06**: LLM Applications — Build a chatbot with retrieval-augmented generation.
