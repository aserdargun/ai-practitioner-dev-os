# Month 11: Advanced ML & Performance

## Why It Matters

Advanced ML techniques and model optimization unlock new capabilities and efficiencies. This month covers cutting-edge topics that differentiate senior practitioners.

**Job Relevance**: Companies need people who can optimize models for production, implement privacy-preserving ML, and work with advanced architectures.

---

## Prerequisites

- Month 01-10 completed
- Deep learning proficiency
- Production deployment experience

---

## Learning Goals

### Tier 2 Focus (Consolidation)
- LoRA and QLoRA for efficient fine-tuning
- Model optimization basics

### Tier 3 Focus
- ONNX for model portability
- TensorRT for NVIDIA optimization
- CUDA programming basics
- TFLite for mobile/edge
- Federated Learning
- Graph Neural Networks
- Reinforcement Learning introduction

---

## Main Project: Optimized ML System

Build an optimized ML system that:
1. Converts PyTorch model to ONNX
2. Optimizes with TensorRT
3. Benchmarks performance improvements
4. Implements efficient fine-tuning (LoRA)
5. Explores federated learning concepts

### Deliverables

1. **`optimization/`** - Model conversion and optimization
2. **`benchmarks/`** - Performance benchmarks
3. **`finetuning/`** - LoRA/QLoRA implementation
4. **`federated/`** - Federated learning experiment
5. **`edge/`** - Edge deployment (TFLite)
6. **`docs/`** - Optimization guide

### Definition of Done

- [ ] PyTorch → ONNX conversion works
- [ ] TensorRT optimization showing speedup
- [ ] Benchmark suite with metrics
- [ ] LoRA fine-tuning on custom task
- [ ] Federated learning POC running
- [ ] Edge deployment working
- [ ] Optimization guide documented

---

## Week-by-Week Plan

### Week 1: ONNX & Model Portability

**Focus**: Model format conversion.

- ONNX format understanding
- PyTorch to ONNX export
- ONNX Runtime inference
- Model validation
- Performance comparison

**Milestone**: ONNX model running with validated outputs.

### Week 2: TensorRT & GPU Optimization

**Focus**: NVIDIA optimization.

- TensorRT basics
- ONNX to TensorRT conversion
- Precision (FP16, INT8)
- Batching strategies
- Performance profiling

**Milestone**: TensorRT model with measured speedup.

### Week 3: Efficient Fine-tuning

**Focus**: PEFT techniques.

- LoRA concepts
- QLoRA for memory efficiency
- Hugging Face PEFT library
- Fine-tuning LLMs
- Evaluation

**Milestone**: LoRA fine-tuned model for custom task.

### Week 4: Advanced Topics

**Focus**: Cutting-edge ML.

- Federated Learning concepts
- NVIDIA FLARE introduction
- Graph Neural Networks overview
- Edge deployment (TFLite)
- Reinforcement Learning basics

**Milestone**: Federated learning POC and edge deployment.

---

## Stretch Goals

- Implement GNN for graph data
- Build RL agent for simple environment
- Add quantization-aware training
- Implement model distillation
- Build multi-GPU training

---

## Claude Prompts

### Planning
```
/plan-week
```

### Optimization Strategy
```
As the Researcher, what's the best optimization path for my transformer model?
```

### LoRA Help
```
As the Builder, help me implement LoRA fine-tuning for classification.
```

### Performance Debugging
```
/debug-learning

My TensorRT conversion is failing. Here's the error...
```

### Review
```
/harden

Review my model optimization pipeline.
```

---

## How to Publish

### Demo Script
```python
# demo.py
import time
from optimization import PyTorchModel, ONNXModel, TensorRTModel

# Load models
pytorch_model = PyTorchModel.load("models/pytorch.pt")
onnx_model = ONNXModel.load("models/model.onnx")
trt_model = TensorRTModel.load("models/model.trt")

# Benchmark
inputs = generate_sample_inputs(100)

for name, model in [("PyTorch", pytorch_model),
                     ("ONNX", onnx_model),
                     ("TensorRT", trt_model)]:
    start = time.time()
    for inp in inputs:
        model.predict(inp)
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.2f}s ({100/elapsed:.1f} samples/sec)")
```

### Write-Up Topics
- Model optimization journey
- ONNX for portability
- TensorRT speedups
- LoRA for efficient fine-tuning
- Federated learning concepts

---

## Resources

- [ONNX Documentation](https://onnx.ai/)
- [TensorRT Developer Guide](https://docs.nvidia.com/deeplearning/tensorrt/)
- [Hugging Face PEFT](https://huggingface.co/docs/peft)
- [NVIDIA FLARE](https://nvidia.github.io/NVFlare/)
- [TFLite Guide](https://www.tensorflow.org/lite/guide)

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 11
```
