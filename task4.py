# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZAEmz7DzNQkwEeHcIKhZ3j3wqw8smtJO
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np

# Load the spam data from a CSV file
def load_data(filepath):
    data = pd.read_csv(filepath)
    X = data.drop('Class', axis=1)
    y = data['Class']
    return X, y

# Split data into training and testing sets
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test

# Train a logistic regression model
def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=200)  # Increase max_iter if convergence issues occur
    model.fit(X_train, y_train)
    return model

# Evaluate the model using confusion matrix
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    return cm

def main():
    filepath = 'spam-data.csv'  # Adjust the path to where your spam-data.csv is located
    X, y = load_data(filepath)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    cm = evaluate_model(model, X_test, y_test)
    print("Confusion Matrix:")
    print(cm)

if __name__ == "__main__":
    main()