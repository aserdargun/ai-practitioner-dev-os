# Mini Example: Iris Classifier

A minimal end-to-end ML project demonstrating the complete workflow in ~100 lines.

## What This Demonstrates

1. **Data Loading** - Load the Iris dataset
2. **Preprocessing** - Split data, scale features
3. **Training** - Train a simple classifier
4. **Evaluation** - Compute accuracy and generate report
5. **Inference** - Make predictions on new data

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run the full pipeline
python main.py

# Run tests
pytest
```

## Output

Running `python main.py` will:
1. Load and preprocess the Iris dataset
2. Train a logistic regression classifier
3. Print evaluation metrics
4. Save the trained model

## Code Structure

```
mini-example/
├── main.py           # Complete 100-line pipeline
├── test_main.py      # Tests
├── pyproject.toml    # Dependencies
└── README.md         # This file
```

## Use This As

- A template for your first ML project
- A reference for project structure
- A starting point for Month 1-2 projects

## Next Steps

After understanding this example:
1. Try modifying the model type
2. Add more evaluation metrics
3. Save predictions to a file
4. Add data visualization
