# Month 05: Deep Learning Foundations

## Why It Matters

Deep learning powers modern AI breakthroughs. This month builds your understanding of neural networks from first principles, preparing you for NLP, computer vision, and beyond.

**Job Relevance**: Deep learning is essential for cutting-edge AI roles. Understanding fundamentals helps you debug, optimize, and innovate.

---

## Prerequisites

- Month 01-04 completed
- Linear algebra basics
- Classical ML understanding

---

## Learning Goals

### Tier 1 Focus
- Neural network fundamentals
- Backpropagation and gradients
- Activation functions
- Loss functions
- RNN and LSTM architectures
- CNN fundamentals

### Tier 2 Focus
- PyTorch mastery
- TensorFlow overview
- Training loop patterns
- GPU training
- Model checkpointing
- Transfer learning basics

### Tier 3 Preview
- CUDA programming concepts
- Performance optimization
- Distributed training

---

## Main Project: Neural Network from Scratch + PyTorch

Build neural networks that:
1. Implement basic NN from scratch (NumPy only)
2. Build same network in PyTorch
3. Train on image classification (MNIST/CIFAR)
4. Implement CNN for better performance
5. Track experiments and visualize training

### Deliverables

1. **`scratch/`** - NumPy-only neural network
2. **`pytorch/`** - PyTorch implementations
3. **`training/`** - Training scripts and configs
4. **`models/`** - Saved model checkpoints
5. **`notebooks/`** - Learning notebooks
6. **`tests/`** - Unit tests

### Definition of Done

- [ ] NumPy neural network achieves >90% on MNIST
- [ ] PyTorch CNN achieves >95% on MNIST
- [ ] Training curves visualized
- [ ] Experiments tracked with MLflow
- [ ] Model checkpointing works
- [ ] Transfer learning example

---

## Week-by-Week Plan

### Week 1: Neural Networks from Scratch

**Focus**: Understand fundamentals deeply.

- Forward propagation
- Backpropagation
- Gradient descent
- Activation functions
- Build MLP from scratch

**Milestone**: NumPy neural network training on MNIST.

### Week 2: PyTorch Fundamentals

**Focus**: Master the framework.

- Tensors and autograd
- nn.Module and layers
- Optimizers and loss functions
- DataLoader and datasets
- Training loops

**Milestone**: Same network in PyTorch, faster training.

### Week 3: Convolutional Networks

**Focus**: Learn spatial architectures.

- Convolution operations
- Pooling layers
- CNN architectures (LeNet, VGG, ResNet concepts)
- Data augmentation
- Batch normalization

**Milestone**: CNN achieving >95% on MNIST or CIFAR-10.

### Week 4: Advanced Topics

**Focus**: Production patterns.

- Transfer learning
- Model checkpointing
- Learning rate scheduling
- GPU training
- Experiment tracking

**Milestone**: Complete training pipeline with best practices.

---

## Stretch Goals

- Implement attention mechanism
- Try different architectures (ResNet, DenseNet)
- Add mixed precision training
- Implement early stopping
- Build custom dataset pipeline

---

## Claude Prompts

### Planning
```
/plan-week
```

### Architecture Questions
```
As the Researcher, explain the tradeoffs between different CNN architectures.
```

### Debugging Training
```
/debug-learning

My model loss isn't decreasing. Here's my training loop...
```

### Code Review
```
/harden

Review my PyTorch training code for correctness and efficiency.
```

---

## How to Publish

### Demo Script
```python
# demo.py
import torch
from pytorch.models import CNN
from pytorch.utils import load_image

model = CNN.load("models/best_cnn.pt")
image = load_image("sample.png")
prediction = model(image)
print(f"Predicted class: {prediction.argmax()}")
```

### Write-Up Topics
- Building neural networks from scratch
- PyTorch vs TensorFlow comparison
- CNN architecture decisions
- Training tips and tricks

---

## Resources

- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Deep Learning Book](https://www.deeplearningbook.org/)
- [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- Skill: `.claude/skills/baseline-model-and-card.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 5
```
