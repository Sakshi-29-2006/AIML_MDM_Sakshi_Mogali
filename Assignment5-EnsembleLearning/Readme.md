
# Breast Cancer Classification Using Ensemble Learning

## Project Overview
This project implements and compares individual machine learning classifiers with ensemble learning techniques for breast cancer classification using the Breast Cancer Wisconsin dataset.

## Dataset
- Dataset: Breast Cancer Wisconsin (Diagnostic)
- Total Samples: 569
- Features: 30 numerical features
- Classes: Malignant and Benign
- Source: Scikit-learn

## Machine Learning Models

### Base Models
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

### Ensemble Models
- Stacking Classifier
- AdaBoost Classifier
- Hard Voting Classifier

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Classification Report
- Confusion Matrix

## Requirements
Install the required Python libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

**Note:** Scikit-learn version 1.2 or later is recommended.


## Output
- Performance comparison of all models.
- Classification reports.
- Confusion matrices.
- Graphical comparison of evaluation metrics.
- CSV file containing model evaluation results.
