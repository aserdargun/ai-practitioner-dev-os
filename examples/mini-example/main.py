#!/usr/bin/env python3
"""
Mini Example: Complete ML Pipeline in ~100 lines

Demonstrates: data loading, preprocessing, training, evaluation, inference.
"""

import pickle
from pathlib import Path

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data():
    """Load the Iris dataset."""
    iris = load_iris()
    return iris.data, iris.target, iris.target_names


def preprocess(X, y, test_size=0.2, random_state=42):
    """Split and scale data."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def train(X_train, y_train):
    """Train a logistic regression classifier."""
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test, target_names):
    """Evaluate the model and print metrics."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=target_names)
    return accuracy, report, y_pred


def predict(model, scaler, X_new):
    """Make predictions on new data."""
    X_scaled = scaler.transform(X_new)
    return model.predict(X_scaled)


def save_model(model, scaler, path="model.pkl"):
    """Save model and scaler to file."""
    with open(path, "wb") as f:
        pickle.dump({"model": model, "scaler": scaler}, f)


def load_model(path="model.pkl"):
    """Load model and scaler from file."""
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data["model"], data["scaler"]


def main():
    """Run the complete ML pipeline."""
    print("=" * 50)
    print("Mini ML Pipeline: Iris Classification")
    print("=" * 50)

    # Step 1: Load data
    print("\n[1] Loading data...")
    X, y, target_names = load_data()
    print(f"    Samples: {len(X)}, Features: {X.shape[1]}")
    print(f"    Classes: {list(target_names)}")

    # Step 2: Preprocess
    print("\n[2] Preprocessing...")
    X_train, X_test, y_train, y_test, scaler = preprocess(X, y)
    print(f"    Train: {len(X_train)}, Test: {len(X_test)}")

    # Step 3: Train
    print("\n[3] Training model...")
    model = train(X_train, y_train)
    print("    Model: LogisticRegression")

    # Step 4: Evaluate
    print("\n[4] Evaluating...")
    accuracy, report, y_pred = evaluate(model, X_test, y_test, target_names)
    print(f"    Accuracy: {accuracy:.2%}")
    print("\n    Classification Report:")
    print("    " + report.replace("\n", "\n    "))

    # Step 5: Save
    print("\n[5] Saving model...")
    save_model(model, scaler)
    print("    Saved to: model.pkl")

    # Step 6: Demo inference
    print("\n[6] Demo inference...")
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Likely setosa
    prediction = predict(model, scaler, sample)
    print(f"    Input: {sample[0]}")
    print(f"    Prediction: {target_names[prediction[0]]}")

    print("\n" + "=" * 50)
    print("Pipeline complete!")
    print("=" * 50)

    return accuracy


if __name__ == "__main__":
    main()
