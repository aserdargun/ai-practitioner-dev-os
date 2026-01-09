# Month 8: Natural Language Processing Basics

**Theme**: Enter the world of text data and language understanding.

## Why It Matters

Text data is everywhere—reviews, documents, social media, customer support. NLP lets you extract value from this unstructured data. With the rise of LLMs, NLP skills are more valuable than ever.

## Prerequisites

- Month 6 completed (classification)
- Python string operations
- Basic understanding of probability

## Learning Goals

### Text Processing (Week 1)
- [ ] Text cleaning and normalization
- [ ] Tokenization
- [ ] Stop words removal
- [ ] Stemming and lemmatization
- [ ] Regular expressions basics

### Text Representation (Week 2)
- [ ] Bag of Words
- [ ] TF-IDF
- [ ] Word embeddings concepts
- [ ] Word2Vec introduction
- [ ] Document similarity

### NLP Applications (Week 3-4)
- [ ] Text classification
- [ ] Sentiment analysis
- [ ] Named Entity Recognition (NER) basics
- [ ] Topic modeling (LDA)
- [ ] NLTK library

## Main Project: Sentiment Analyzer

Build a sentiment analysis system for product reviews.

### Dataset
Use Amazon reviews or movie reviews from NLTK/Kaggle.

### Deliverables
1. Text processing pipeline:
   - Cleaning functions
   - Tokenization
   - Vectorization (TF-IDF)

2. Sentiment classifier:
   - Multiple models compared
   - Handle class balance
   - Evaluation on test set

3. Analysis notebook:
   - Word clouds by sentiment
   - Most predictive words
   - Error analysis

### Definition of Done
- [ ] Complete text processing pipeline
- [ ] 3+ classifiers compared
- [ ] >80% accuracy on sentiment
- [ ] Visualization of results
- [ ] Can classify new reviews
- [ ] Code documented

## Stretch Goals

- [ ] Try word embeddings
- [ ] Build aspect-based sentiment
- [ ] Create simple Streamlit demo
- [ ] Add multi-language support
- [ ] Explore BERT embeddings

## Weekly Breakdown

### Week 1: Text Processing
- Text cleaning
- Tokenization
- NLTK basics
- Process review dataset

### Week 2: Representation
- Bag of Words
- TF-IDF
- Implement vectorizers
- Explore word frequencies

### Week 3: Classification
- Build sentiment classifier
- Compare models
- Tune and evaluate
- Error analysis

### Week 4: Polish & Ship
- Visualizations
- Documentation
- Demo prep
- Portfolio entry

## Claude Prompts

### Planning
```
/plan-week
Month 8 Week 1 - Focus on text processing
I want to build a solid preprocessing pipeline
```

### Building
```
Ask the Builder to help me create a text
preprocessing class that handles cleaning,
tokenization, and TF-IDF vectorization.
```

### Concept Help
```
Ask the Researcher to explain TF-IDF intuitively.
Why does it work better than raw word counts?
```

### Review
```
Ask the Reviewer to review my text classification
pipeline. Am I preprocessing correctly?
Any NLP-specific issues?
```

## How to Publish

### Demo
1. Show raw review text
2. Demonstrate preprocessing
3. Show vectorized representation
4. Classify sample reviews
5. Explain predictions

### Write-up Topics
- Text preprocessing decisions
- Why TF-IDF works
- Sentiment analysis challenges
- Interesting patterns found

### Portfolio Entry
- Clear preprocessing code
- Model comparison
- Example predictions

## Resources

### NLP Basics
- [NLTK Book](https://www.nltk.org/book/) — Free online
- [Spacy Course](https://course.spacy.io/en/)

### Text Classification
- [scikit-learn Text](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

### Videos
- [Stanford NLP YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z)

### Practice
- [Kaggle NLP Getting Started](https://www.kaggle.com/c/nlp-getting-started)

## Tips

1. **Clean thoroughly** — Garbage in, garbage out
2. **Look at errors** — They reveal preprocessing gaps
3. **Domain matters** — Twitter text ≠ legal documents
4. **Start simple** — TF-IDF + Logistic Regression is a strong baseline
5. **Preserve examples** — Keep original text for debugging
