# Month 9: Deep Learning Introduction

**Theme**: Enter the world of neural networks.

## Why It Matters

Deep learning powers modern AI—image recognition, language models, recommendation systems. Understanding neural network fundamentals prepares you for advanced AI work and helps you leverage pre-trained models.

## Prerequisites

- Month 5-6 completed (ML fundamentals)
- Linear algebra basics (vectors, matrices)
- Python numpy proficiency

## Learning Goals

### Neural Network Basics (Week 1)
- [ ] Neurons and activation functions
- [ ] Feedforward networks
- [ ] Loss functions
- [ ] Backpropagation intuition
- [ ] Gradient descent variants

### Building Networks (Week 2-3)
- [ ] PyTorch or TensorFlow/Keras basics
- [ ] Creating simple networks
- [ ] Training loops
- [ ] Batching and epochs
- [ ] Overfitting prevention (dropout, regularization)

### Practical Deep Learning (Week 4)
- [ ] CNN introduction for images
- [ ] Transfer learning concepts
- [ ] Model saving and loading
- [ ] GPU basics (optional)

## Main Project: Digit Recognizer

Build a neural network to classify handwritten digits.

### Dataset
MNIST or Fashion-MNIST (included in PyTorch/Keras).

### Deliverables
1. Basic neural network:
   - Multi-layer perceptron
   - Training with validation
   - >95% accuracy

2. Improved network:
   - Convolutional layers
   - Data augmentation
   - >98% accuracy target

3. Learning notebook:
   - Visualize training progress
   - Show confusion matrix
   - Display misclassified examples

### Definition of Done
- [ ] MLP achieves >95% accuracy
- [ ] CNN improves on MLP
- [ ] Training visualized (loss curves)
- [ ] Can classify new images
- [ ] Understand what each layer does
- [ ] Code documented

## Stretch Goals

- [ ] Try different architectures
- [ ] Implement learning rate scheduling
- [ ] Add batch normalization
- [ ] Create real-time webcam demo
- [ ] Explore pretrained models

## Weekly Breakdown

### Week 1: Foundations
- Neural network concepts
- Activation functions
- Install PyTorch/Keras
- First "Hello World" network

### Week 2: Building Networks
- MLP for MNIST
- Training loops
- Validation and monitoring
- Debug training issues

### Week 3: CNNs
- Convolution concept
- Build CNN
- Improve accuracy
- Data augmentation

### Week 4: Polish & Ship
- Error analysis
- Documentation
- Demo prep
- Portfolio entry

## Claude Prompts

### Planning
```
/plan-week
Month 9 Week 2 - Focus on building neural networks
I'm using PyTorch, starting with MNIST
```

### Concept Help
```
Ask the Researcher to explain backpropagation
intuitively. I want to understand how neural
networks learn, not just use them.
```

### Building
```
Ask the Builder to help me create a CNN
for MNIST in PyTorch with proper training
and validation loops.
```

### Debugging
```
/debug-learning
My model's accuracy is stuck at 50%.
Training loss is decreasing but validation isn't.
What could be wrong?
```

## How to Publish

### Demo
1. Show the MNIST dataset
2. Explain network architecture
3. Show training progress
4. Demonstrate predictions
5. Show failure cases

### Write-up Topics
- How neural networks learn
- MLP vs CNN comparison
- Training challenges faced
- What I'd do differently

### Portfolio Entry
- Network architecture diagram
- Training curves
- Example predictions

## Resources

### Deep Learning
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Fast.ai Course](https://course.fast.ai/) — Practical deep learning
- [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — Visual explanations

### Frameworks
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Keras Documentation](https://keras.io/)

### Practice
- [Kaggle Digit Recognizer](https://www.kaggle.com/c/digit-recognizer)

## Tips

1. **Start simple** — 2-3 layers before going deep
2. **Monitor training** — Plot loss curves, catch problems early
3. **Validate always** — Use validation set from the start
4. **Learn one framework** — PyTorch or Keras, not both at once
5. **Understand, don't just copy** — Know why things work
