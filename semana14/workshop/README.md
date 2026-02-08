# Week 14 Workshop: ML Models - Classification & Regression

## Overview

In this workshop, you will build, evaluate, and compare multiple machine learning models using the Water Consumption dataset. You will work with both regression and classification problems, learning to select the best model based on performance metrics.

**Duration:** 2-3 hours (independent work)

**Deadline:** Before Week 15 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Build and train at least 3 different ML models
2. Evaluate models using appropriate metrics (RMSE, MAE, R-squared for regression; accuracy, precision, recall for classification)
3. Create and interpret confusion matrices
4. Calculate and visualize feature importance
5. Document model selection rationale with supporting evidence

---

## Dataset

**Source:** datos.gov.co - Water Consumption Data

**Description:** Water consumption records containing:
- Consumption measurements across different locations
- Temporal data (dates, periods)
- Categorical attributes (type, zone, etc.)
- Numeric features for prediction

This is the same dataset you explored in Week 13.

---

## Workshop Structure

### Part 1: Data Preparation

Before building models:
1. Load and explore the dataset
2. Handle missing values
3. Encode categorical variables
4. Select features and target variable(s)
5. Split data into training and testing sets (80/20)

### Part 2: Build and Compare 3+ Models

You must implement AT LEAST 3 models. Choose from:

| Model Type | Regression Version | Classification Version |
|------------|-------------------|----------------------|
| Linear/Logistic | `LinearRegression` | `LogisticRegression` |
| Decision Tree | `DecisionTreeRegressor` | `DecisionTreeClassifier` |
| Random Forest | `RandomForestRegressor` | `RandomForestClassifier` |
| Gradient Boosting | `GradientBoostingRegressor` | `GradientBoostingClassifier` |
| K-Nearest Neighbors | `KNeighborsRegressor` | `KNeighborsClassifier` |

For each model:
- Train on the training set
- Evaluate on the test set
- Record all metrics

### Part 3: Create Confusion Matrix (Classification)

If you perform classification:
1. Generate predictions on the test set
2. Create a confusion matrix using `confusion_matrix()`
3. Visualize the matrix as a heatmap
4. Interpret: What types of errors is the model making?

For regression, create a residual analysis instead:
1. Calculate residuals (actual - predicted)
2. Plot residual distribution
3. Identify any patterns or outliers

### Part 4: Calculate Feature Importance

Using your best tree-based model (Decision Tree or Random Forest):
1. Extract feature importances
2. Rank features from most to least important
3. Visualize with a horizontal bar chart
4. Discuss: Do the important features make sense?

### Part 5: Document Model Selection Rationale

Write a 1-page analysis that includes:
1. Summary of all models tested and their performance
2. Which model you recommend and WHY
3. Discussion of trade-offs (accuracy vs interpretability, speed, etc.)
4. Potential improvements for future work

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

1. Check for missing values and handle them
2. Identify your target variable (regression: continuous value; classification: categorical)
3. Select relevant features
4. Encode categorical variables if needed
5. Split into train/test sets

### Step 3: Model Building

For each of your 3+ models:

```python
# The sklearn pattern (memorize this!)
from sklearn.MODEL_TYPE import ModelName

# 1. Create
model = ModelName(parameters)

# 2. Train
model.fit(X_train, y_train)

# 3. Predict
y_pred = model.predict(X_test)

# 4. Evaluate
score = model.score(X_test, y_test)
```

### Step 4: Evaluation

**For Regression:**
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

**For Classification:**
```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

accuracy = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
```

### Step 5: Confusion Matrix Visualization

```python
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
```

### Step 6: Feature Importance

```python
# For tree-based models
importance = model.feature_importances_
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': importance
}).sort_values('importance', ascending=False)
```

### Step 7: Documentation

Write your model selection rationale addressing:
- Which metrics did you prioritize and why?
- How did the models compare?
- What are the limitations of your chosen model?
- What would you try next to improve performance?

---

## Grading Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| Data Preparation | 15 | Clean, well-prepared data |
| Model Implementation | 30 | At least 3 models correctly implemented |
| Evaluation Metrics | 20 | Correct metrics calculated and interpreted |
| Confusion Matrix/Residuals | 15 | Proper visualization and interpretation |
| Feature Importance | 10 | Calculated and visualized |
| Model Selection Rationale | 10 | Clear, evidence-based recommendation |

**Total: 100 points**

---

## Tips for Success

### Before You Start
- Review Week 13 slides on ML fundamentals
- Review Week 14 slides on model types
- Make sure scikit-learn is installed

### While Working
- Start simple (Linear/Logistic Regression) before complex models
- Always check for overfitting (train vs test performance)
- Use `random_state=42` for reproducibility
- Comment your code to explain your decisions

### Common Mistakes to Avoid
- Using test data during training (data leakage)
- Forgetting to handle missing values
- Not scaling features when required (for some algorithms)
- Comparing models using only one metric
- Choosing the most complex model without justification

### If Stuck
- Re-read the sklearn documentation
- Check that your X and y have the right shapes
- Make sure you are using the right model type (Regressor vs Classifier)
- Only check the solution notebook as a last resort

---

## Metrics Reference

### Regression Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| RMSE | sqrt(mean((y - y_pred)^2)) | Average error in same units as target |
| MAE | mean(abs(y - y_pred)) | Average absolute error |
| R-squared | 1 - SS_res/SS_tot | Proportion of variance explained (0-1) |

### Classification Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Accuracy | (TP + TN) / Total | Overall correctness |
| Precision | TP / (TP + FP) | Of predicted positives, how many are correct? |
| Recall | TP / (TP + FN) | Of actual positives, how many did we find? |
| F1-Score | 2 * (Precision * Recall) / (Precision + Recall) | Harmonic mean of precision and recall |

### Confusion Matrix

```
                Predicted
              Neg    Pos
Actual  Neg   TN     FP
        Pos   FN     TP
```

- **True Negative (TN):** Correctly predicted negative
- **False Positive (FP):** Incorrectly predicted positive (Type I error)
- **False Negative (FN):** Incorrectly predicted negative (Type II error)
- **True Positive (TP):** Correctly predicted positive

---

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the deadline.

Ensure that:
- All cells have been executed (Kernel > Restart & Run All)
- At least 3 models are implemented and evaluated
- Confusion matrix or residual analysis is complete
- Feature importance is calculated and visualized
- Model selection rationale is written

---

## Connection to Final Project

These skills are essential for your final project:

| Workshop Skill | Project Application |
|----------------|---------------------|
| Model building | Train models on your datos.gov.co dataset |
| Model comparison | Select the best approach for your problem |
| Feature importance | Identify key drivers in your data |
| Documentation | Justify your methodology in your report |

---

## Resources

- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
- Model Selection: https://scikit-learn.org/stable/model_selection.html
- Confusion Matrix: https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix
- Feature Importance: https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html

---

*Week 14 - Data Analytics Course - Universidad Cooperativa de Colombia*
