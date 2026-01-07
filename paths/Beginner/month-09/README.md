# Month 9: Deep Learning Introduction

**Focus**: Understand neural networks and deep learning fundamentals

---

## Why It Matters

Deep learning powers modern AI breakthroughs:
- Image recognition
- Language models
- Speech processing
- Generative AI

Understanding neural network fundamentals helps you:
- Use pre-trained models effectively
- Fine-tune for specific tasks
- Know when deep learning is (and isn't) appropriate

---

## Prerequisites

- Months 1-8 completed
- Strong ML foundation
- Linear algebra basics helpful

---

## Learning Goals

By the end of this month, you will:

1. **Neural Network Fundamentals**
   - [ ] Perceptrons and activation functions
   - [ ] Forward propagation
   - [ ] Backpropagation intuition
   - [ ] Loss functions and optimization

2. **Building Networks**
   - [ ] Layers and architectures
   - [ ] Fully connected networks
   - [ ] Convolutional layers (intro)
   - [ ] Recurrent layers (intro)

3. **Training Practices**
   - [ ] Batch sizes and epochs
   - [ ] Learning rate selection
   - [ ] Regularization (dropout, L2)
   - [ ] Early stopping

4. **PyTorch Basics**
   - [ ] Tensors and operations
   - [ ] Building models
   - [ ] Training loops
   - [ ] GPU basics (if available)

---

## Main Project: Image Classifier

Build a neural network that classifies images.

### Deliverables

1. **Classification notebook** (`image_classifier.ipynb`)
   - Data loading and preprocessing
   - Model architecture
   - Training process
   - Evaluation and visualization

2. **Model module** (`model/`)
   - `dataset.py` - Data loading
   - `network.py` - Model architecture
   - `train.py` - Training loop
   - `predict.py` - Inference

3. **Training artifacts**
   - Saved model weights
   - Training curves (loss, accuracy)
   - Sample predictions

4. **Documentation**
   - Architecture description
   - Training decisions
   - Results analysis

### Definition of Done

- [ ] Model trains successfully
- [ ] Achieves >85% test accuracy
- [ ] Training curves show convergence
- [ ] Can classify new images
- [ ] Code is well-organized
- [ ] Documentation complete

### Dataset Suggestions

- [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist)
- [Fashion-MNIST](https://pytorch.org/vision/stable/datasets.html#fashion-mnist)
- [CIFAR-10](https://pytorch.org/vision/stable/datasets.html#cifar)
- Custom image dataset

---

## Stretch Goals

- [ ] Implement data augmentation
- [ ] Try transfer learning
- [ ] Visualize learned features
- [ ] Deploy model with Gradio

---

## Weekly Breakdown

### Week 1: Neural Network Theory
- Perceptron and activation functions
- Multi-layer networks
- Forward and backward propagation
- Loss functions and gradients

### Week 2: PyTorch Basics
- Tensors and autograd
- Building simple models
- Training loops
- GPU operations

### Week 3: CNNs for Images
- Convolutional layers
- Pooling and architecture
- Image preprocessing
- Transfer learning intro

### Week 4: Project Completion
- Build image classifier
- Train and evaluate
- Analyze results
- Document learnings

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 9: Deep Learning Intro.
Help me understand neural network fundamentals.
```

### Concept Explanation
```
Explain [backpropagation / activation functions / etc] in simple terms:
- The intuition
- Why it's important
- Visual/mathematical representation
- Code example
```

### PyTorch Help
```
I'm trying to [task] in PyTorch.
Here's my current code:
[paste code]

What's wrong and how do I fix it?
```

### Architecture Design
```
I'm building a classifier for [dataset description].
Input size: [dimensions]
Output classes: [number]

What architecture should I use?
Walk me through the layers.
```

### Training Issues
```
My model is [not converging / overfitting / etc]:
- Loss: [values over epochs]
- Train accuracy: [value]
- Test accuracy: [value]

What's happening and how do I fix it?
```

### GPU Setup
```
I have a [GPU type] and want to use it with PyTorch.
Walk me through:
1. Checking GPU availability
2. Moving model to GPU
3. Moving data to GPU
4. Common pitfalls
```

---

## How to Publish

### Demo

Show your image classifier:
1. Sample images and predictions
2. Training curves
3. Confusion matrix
4. Interesting failure cases

### Write-up

Cover:
- Neural network intuition
- Architecture decisions
- Training process
- What you learned

### Portfolio

- Trained model with demo
- Clean notebook
- Visualizations of training

---

## Resources

### Theory
- [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Deep Learning Book](https://www.deeplearningbook.org/)

### PyTorch
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [PyTorch 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)

### Practice
- [Fast.ai Course](https://course.fast.ai/)

---

## Next Month

[Month 10: Web Development](../month-10/README.md) - Flask, APIs, and deployment
