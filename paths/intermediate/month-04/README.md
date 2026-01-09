# Month 04: Deep Learning

**Focus**: Build and train neural networks with PyTorch.

---

## Why It Matters

Deep learning powers most modern AI applications — from computer vision to NLP to generative AI. Understanding neural networks is essential for any AI practitioner. PyTorch is the industry-standard framework for research and production.

**Job Relevance**: Required for ML engineering and AI research roles; valuable for all AI practitioners.

---

## Prerequisites

- Month 01-03 complete
- Understanding of gradient descent concept
- Basic linear algebra (matrices, vectors)

---

## Learning Goals

**Tier 1 Technologies**:
- Deep Learning (intro)
- Computer Vision basics
- RNN, LSTM

**Tier 2 Technologies**:
- PyTorch (primary focus)
- CNN architectures
- TensorFlow (awareness)
- GPU basics (optional)

**Skills**:
- Neural network architecture
- Training and optimization
- Model debugging
- Transfer learning basics

---

## Main Project: Image Classifier

Build and train a CNN image classifier from scratch, then apply transfer learning.

### Deliverables

1. **Custom CNN** trained on a dataset
2. **Transfer Learning Model** using pretrained weights
3. **Training Pipeline** with proper validation
4. **Model Comparison** report
5. **GitHub Repository** with notebooks and scripts

### Definition of Done

- [ ] Dataset loaded and preprocessed
- [ ] Custom CNN architecture defined
- [ ] Training loop implemented
- [ ] Validation monitoring in place
- [ ] Model saves best checkpoint
- [ ] Transfer learning model created
- [ ] Both models evaluated and compared
- [ ] Training curves visualized
- [ ] Predictions demonstrated on test images
- [ ] Code is modular and documented

---

## Stretch Goals

- [ ] Data augmentation implemented
- [ ] Learning rate scheduling
- [ ] Multiple pretrained backbones compared
- [ ] Model deployed as API

---

## Weekly Cadence

### Week 1: PyTorch Fundamentals
- PyTorch tensors and operations
- Dataset and DataLoader
- Basic neural network
- Training loop basics

### Week 2: Build Custom CNN
- CNN architecture
- Training with validation
- Debugging and improving

### Week 3: Transfer Learning
- Load pretrained model
- Fine-tune for your task
- Compare with custom model

### Week 4: Ship & Document
- Create comparison report
- Visualize results
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 4 on deep learning. I want to build an image classifier.
Help me plan the PyTorch learning curve and project setup.
```

### Building
```
/ship-mvp

My CNN has:
- 3 conv layers
- Training accuracy: 85%
- Validation accuracy: 78%
Is this gap concerning? What should I try next?
```

### Debugging
```
/debug-learning

My model's validation loss is increasing while training loss decreases.
I think it's overfitting. What should I try?
```

### Review
```
/harden

Review my PyTorch code for:
- Best practices
- Memory efficiency
- Code organization
```

---

## How to Publish

### Demo
- Show training progress
- Demonstrate predictions on new images
- Compare custom vs transfer learning

### Write-up
- "Building My First Neural Network: A Deep Learning Journey"
- Include architecture diagrams
- Share training curves and insights

---

## Resources

### Datasets
- CIFAR-10, CIFAR-100
- Fashion-MNIST
- Custom dataset from Kaggle

### Skill Playbooks
- [Experiment Plan](../../../.claude/skills/experiment-plan.md)

### Documentation
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/)

---

## Next Month Preview

**Month 05**: NLP Foundations — Apply deep learning to text with transformers.
