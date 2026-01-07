# Month 8: NLP Basics

**Focus**: Process and analyze text data

---

## Why It Matters

Natural Language Processing enables:
- Sentiment analysis
- Text classification
- Information extraction
- Search and retrieval

With LLMs becoming central to AI, understanding NLP fundamentals is essential.

---

## Prerequisites

- Months 1-7 completed
- ML basics (classification)
- Python string manipulation

---

## Learning Goals

By the end of this month, you will:

1. **Text Preprocessing**
   - [ ] Tokenization
   - [ ] Stopword removal
   - [ ] Stemming and lemmatization
   - [ ] Text normalization

2. **Text Representation**
   - [ ] Bag of Words
   - [ ] TF-IDF
   - [ ] Word embeddings (Word2Vec, GloVe)
   - [ ] Document embeddings

3. **NLP Tasks**
   - [ ] Text classification
   - [ ] Sentiment analysis
   - [ ] Named entity recognition (intro)
   - [ ] Topic modeling (intro)

4. **Tools**
   - [ ] NLTK basics
   - [ ] scikit-learn text features
   - [ ] spaCy introduction

---

## Main Project: Text Classification System

Build a system that classifies text documents.

### Deliverables

1. **Classification notebook** (`text_classification.ipynb`)
   - Data exploration
   - Text preprocessing pipeline
   - Feature engineering
   - Model training and evaluation

2. **NLP module** (`nlp/`)
   - `preprocess.py` - Text cleaning functions
   - `features.py` - Feature extraction
   - `classify.py` - Classification logic

3. **Model artifacts**
   - Trained model
   - Vectorizer
   - Label encoder

4. **Demo script** (`demo.py`)
   - Classify new text
   - Show confidence scores

### Definition of Done

- [ ] Text preprocessing pipeline works
- [ ] Multiple representations compared (BoW, TF-IDF)
- [ ] Model achieves >80% accuracy
- [ ] Demo script classifies new text
- [ ] Code is modular and reusable
- [ ] Documentation complete

### Dataset Suggestions

- [IMDB Reviews](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- [News Classification](https://www.kaggle.com/rmisra/news-category-dataset)
- [Spam Detection](https://www.kaggle.com/uciml/sms-spam-collection-dataset)
- Customer support tickets

---

## Stretch Goals

- [ ] Add word embedding features
- [ ] Implement topic modeling
- [ ] Create a simple chatbot
- [ ] Build text similarity search

---

## Weekly Breakdown

### Week 1: Text Preprocessing
- Tokenization techniques
- Cleaning and normalization
- Stopwords and stemming
- Building preprocessing pipeline

### Week 2: Text Representation
- Bag of Words
- TF-IDF features
- Word embeddings intro
- Comparing representations

### Week 3: Classification
- Text classification pipeline
- Model training
- Evaluation metrics for text
- Error analysis

### Week 4: Project & Advanced
- Complete classification system
- Topic modeling intro
- Named entity recognition intro
- Documentation

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 8: NLP Basics.
Help me understand text processing fundamentals.
```

### Preprocessing Help
```
I have text data that includes:
[describe issues - HTML, special chars, etc.]

What preprocessing steps should I apply?
Show me the code.
```

### Feature Comparison
```
I'm comparing text features for classification:
- Bag of Words
- TF-IDF
- Word2Vec embeddings

Explain when to use each and show me how to implement them.
```

### Classification Setup
```
I want to classify [type of text] into [categories].
My dataset has [n] samples.

Walk me through setting up the classification pipeline.
```

### Error Analysis
```
My text classifier has:
- Accuracy: 75%
- Most errors on category: [category]

Help me analyze these errors:
[show example misclassifications]
```

### Improving Performance
```
My TF-IDF + Logistic Regression model achieves 78% accuracy.
What techniques could improve this?

Options I'm considering:
- N-grams
- Word embeddings
- Different algorithms
```

---

## How to Publish

### Demo

Showcase your text classifier:
1. The classification task
2. Preprocessing pipeline
3. Model performance
4. Live classification demo

### Write-up

Cover:
- Text preprocessing decisions
- Feature engineering approach
- Model selection
- Real-world considerations

### Portfolio

- Working classifier with demo
- Modular, reusable code
- Clear documentation

---

## Resources

### NLTK
- [NLTK Book](https://www.nltk.org/book/)
- [NLTK Documentation](https://www.nltk.org/)

### spaCy
- [spaCy 101](https://spacy.io/usage/spacy-101)
- [spaCy Course](https://course.spacy.io/)

### Text Classification
- [scikit-learn Text Tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

### Embeddings
- [Word2Vec Tutorial](https://radimrehurek.com/gensim/models/word2vec.html)

---

## Next Month

[Month 9: Deep Learning Intro](../month-09/README.md) - Neural networks fundamentals
