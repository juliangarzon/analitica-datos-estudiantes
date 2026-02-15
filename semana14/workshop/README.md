# Week 14 Workshop: Build Your First Machine Learning Model

## Overview

In this workshop, you will build, evaluate, and interpret a Decision Tree model using the Water Consumption dataset. You will practice the full ML workflow: data preparation, train/test split, model training, evaluation, and overfitting analysis.

**Duration:** 2 hours (independent work)

**Deadline:** Before Week 15 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Prepare a dataset for machine learning (select features, handle missing values)
2. Split data into training and test sets
3. Train a Decision Tree model (both Regressor and Classifier)
4. Evaluate model performance using appropriate metrics
5. Detect and address overfitting by adjusting model parameters

---

## Dataset

**Source:** datos.gov.co - Water Consumption Data

**Description:** Water consumption records containing:
- Consumption measurements across different locations
- Temporal data (dates, periods)
- Categorical attributes (type, zone, etc.)
- Numeric features for prediction

---

## Workshop Structure

### Part 1: Data Preparation

Before building models:
1. Load and explore the dataset
2. Identify numeric columns
3. Select a target variable (for regression)
4. Select feature columns
5. Handle missing values
6. Split data into training and testing sets (80/20)

### Part 2: Decision Tree Regressor

Build a regression model to predict a continuous value:
1. Create a DecisionTreeRegressor with max_depth=5
2. Train on training data
3. Predict on test data
4. Calculate RMSE, MAE, and R-squared
5. Check for overfitting (train vs test score)

### Part 3: Experiment with max_depth

Understand overfitting through experimentation:
1. Try max_depth values: 2, 3, 5, 10, 20, None
2. Record train and test R-squared for each
3. Plot the overfitting curve
4. Identify the best depth for your data

### Part 4: Decision Tree Classifier (Bonus)

Convert the problem to classification:
1. Create consumption categories (Low, Medium, High)
2. Train a DecisionTreeClassifier
3. Evaluate with accuracy_score
4. Check for overfitting

### Part 5: Interpretation and Reflection

Write a brief analysis:
1. What is the best max_depth for your model? Why?
2. How well does the model predict? Is R-squared acceptable?
3. What features seem most important? (hint: model.feature_importances_)
4. What would you try next to improve the model?

---

## Files Provided

| File | Description |
|------|-------------|
| `workshop_starter.ipynb` | Starter notebook with structure and empty cells |
| `workshop_solution.ipynb` | Complete solution (only look after attempting!) |

---

## Instructions

### Step 1: Setup

1. Open `workshop_starter.ipynb` in Jupyter or VS Code
2. Run the setup cell to load libraries and dataset
3. Explore the data to understand its structure

### Step 2: Data Preparation

1. Identify numeric columns
2. Choose your target variable
3. Select feature columns (remove IDs and the target)
4. Drop rows with missing values
5. Split into train/test sets

### Step 3: Model Building

Follow the sklearn pattern:

```python
# The sklearn pattern (memorize this!)
from sklearn.tree import DecisionTreeRegressor

# 1. Create
model = DecisionTreeRegressor(max_depth=5, random_state=42)

# 2. Train
model.fit(X_train, y_train)

# 3. Predict
y_pred = model.predict(X_test)

# 4. Evaluate
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
```

### Step 4: Overfitting Analysis

```python
# Compare train vs test
r2_train = r2_score(y_train, model.predict(X_train))
r2_test = r2_score(y_test, model.predict(X_test))
gap = r2_train - r2_test

# Gap > 0.10 means overfitting
```

---

## Grading Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| Data Preparation | 20 | Clean, well-prepared data with clear target/features |
| Decision Tree Regressor | 30 | Model correctly trained and evaluated |
| Overfitting Analysis | 25 | Multiple depths tested, overfitting curve plotted |
| Classifier (Bonus) | 10 | Classification version attempted |
| Interpretation | 15 | Clear reflection on results and next steps |

**Total: 100 points**

---

## Tips for Success

### Before You Start
- Review Week 14 slides on ML concepts
- Make sure scikit-learn is installed (`pip install scikit-learn`)

### While Working
- Use `random_state=42` for reproducibility
- Always check for overfitting (train vs test gap)
- Comment your code to explain your decisions
- Start with max_depth=5, then experiment

### Common Mistakes to Avoid
- Forgetting to split data before training (data leakage)
- Using test data during training
- Not handling missing values before training
- Using max_depth=None (unlimited) without checking for overfitting
- Comparing R-squared between different datasets (only compare models on the same test set)

---

## Metrics Reference

### Regression Metrics

| Metric | What It Measures | Good Value |
|--------|-----------------|-----------|
| RMSE | Average error magnitude (same units as target) | Small relative to target range |
| MAE | Average absolute error (easier to interpret) | Small relative to target range |
| R-squared | Proportion of variance explained (0-1) | Close to 1.0 |

### Classification Metrics

| Metric | What It Measures | Good Value |
|--------|-----------------|-----------|
| Accuracy | % of correct predictions | > 80% (depends on task) |

---

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the deadline.

Ensure that:
- All cells have been executed (Kernel > Restart & Run All)
- Decision Tree Regressor is trained and evaluated
- Overfitting analysis is complete (multiple depths tested)
- Interpretation section is written

---

## Connection to Final Project

These skills directly apply to your Milestone 3:

| Workshop Skill | Project Application |
|----------------|---------------------|
| Data preparation | Prepare your datos.gov.co dataset for ML |
| Decision Tree training | Add a predictive model to your project |
| Overfitting analysis | Ensure your model generalizes well |
| Interpretation | Explain your model's predictions to stakeholders |

---

## Resources

- scikit-learn Decision Trees: https://scikit-learn.org/stable/modules/tree.html
- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
- Train/Test Split: https://scikit-learn.org/stable/modules/cross_validation.html

---

*Week 14 - Data Analytics Course - Universidad Cooperativa de Colombia*
