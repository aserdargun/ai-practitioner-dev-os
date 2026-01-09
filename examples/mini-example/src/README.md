# Source Code

This directory contains the main application code.

## Files

| File | Purpose |
|------|---------|
| `model.py` | Model definition and inference |
| `train.py` | Training script with sample data |
| `serve.py` | FastAPI service for predictions |

## Usage

```bash
# Train the model
python train.py

# Start the service
python serve.py
```

## Code Organization

```
src/
├── model.py      # Core ML logic (model class, predict method)
├── train.py      # Training pipeline (load data, train, save)
└── serve.py      # API layer (endpoints, request handling)
```

This separation follows the principle of separating concerns:
- **model.py**: Pure ML logic, no I/O
- **train.py**: Training orchestration
- **serve.py**: HTTP interface
