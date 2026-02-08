# Week 13 Workshop: Introduction to Machine Learning

## ML Data Preparation for Water Consumption Prediction

### Overview

In this workshop, you will prepare the Water Consumption dataset for machine learning, making thoughtful decisions about features, target variables, and data preprocessing. You will document your reasoning at each step, which is a critical skill for real-world ML projects.

**Duration:** 2-3 hours (independent work)

**Deadline:** Before Week 14 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Define a clear ML problem statement from a dataset
2. Select and justify appropriate features for prediction
3. Handle data preprocessing for machine learning
4. Implement train/test split with proper methodology
5. Apply feature scaling correctly
6. Build and interpret a baseline Decision Tree model
7. Document ML decisions with clear rationale

---

## Dataset

**Source:** datos.gov.co - HISTORICO_CONSUMO (Water Consumption)

**Description:** Historical water consumption data from Colombian municipalities containing:
- Consumption volumes (m3)
- Billing amounts (COP)
- Number of subscribers
- Usage types (residential, commercial, industrial)
- Geographic information (department, municipality)
- Time dimension (year)

This is the same dataset you explored in Weeks 4 and 5 (EDA).

---

## Workshop Structure

### Part 1: Problem Definition

You will define a clear ML problem by:

| Task | What you will do |
|------|-----------------|
| 1.1 | Explore potential target variables |
| 1.2 | Choose between classification vs regression |
| 1.3 | Write a formal problem statement |
| 1.4 | Justify your choice |

### Part 2: Feature Selection

You will select and prepare features by:

| Task | What you will do |
|------|-----------------|
| 2.1 | Identify all potential features |
| 2.2 | Eliminate features that would cause data leakage |
| 2.3 | Handle categorical variables (encoding) |
| 2.4 | Document your feature selection rationale |

### Part 3: Data Preparation

You will prepare data for ML by:

| Task | What you will do |
|------|-----------------|
| 3.1 | Handle missing values |
| 3.2 | Perform train/test split |
| 3.3 | Apply feature scaling |
| 3.4 | Verify data integrity after preprocessing |

### Part 4: Baseline Model

You will build a simple model to:

| Task | What you will do |
|------|-----------------|
| 4.1 | Train a Decision Tree model |
| 4.2 | Evaluate model performance |
| 4.3 | Interpret the results |
| 4.4 | Identify potential improvements |

### Part 5: Documentation

You will create a summary that:

| Task | What you will do |
|------|-----------------|
| 5.1 | Summarize all preprocessing decisions |
| 5.2 | Document feature selection rationale |
| 5.3 | Record baseline model performance |
| 5.4 | List next steps for Week 14 |

---

## Files Provided

| File | Description |
|------|-------------|
| `workshop_starter.ipynb` | Starter notebook with structure and hints |
| `workshop_solution.ipynb` | Complete solution (only consult after attempting!) |

---

## Instructions

### Step 1: Setup

1. Open `workshop_starter.ipynb` in Jupyter or VS Code
2. Run the setup cell to load libraries and dataset
3. Review the dataset structure (you should be familiar with it from Weeks 4-5)

### Step 2: Problem Definition (Part 1)

For this workshop, you will focus on a **classification** problem:

**Goal:** Predict whether a municipality's water consumption is HIGH or LOW.

Complete these tasks:
1. Define "HIGH" and "LOW" consumption (use median as threshold)
2. Create the target variable
3. Verify class balance
4. Write a formal problem statement

**Example problem statement:**
> "Given a municipality's characteristics (number of subscribers, usage type, year), predict whether their water consumption will be above or below the median consumption level."

### Step 3: Feature Selection (Part 2)

Think critically about which features to use:

1. **Cannot use:**
   - CONSUMO_FACTURADO (this IS the target)
   - VALOR_FACTURADO (directly derived from consumption)

2. **Consider using:**
   - NUMERO_SUSCRIPTORES (number of subscribers)
   - USO (usage type - needs encoding)
   - ANNO (year)
   - DEPARTAMENTO (department - needs encoding)

3. **Document your reasoning:**
   - Why did you include each feature?
   - Why did you exclude certain features?
   - What assumptions are you making?

### Step 4: Data Preparation (Part 3)

Follow these steps carefully:

1. **Handle missing values:**
   - Check for missing values in selected features
   - Decide: Drop rows or impute values?
   - Document your decision

2. **Train/Test Split:**
   - Use 80/20 split
   - Set random_state=42 for reproducibility
   - Verify class distribution in both sets

3. **Feature Scaling:**
   - Apply StandardScaler
   - Remember: fit_transform on train, transform on test
   - Explain why this order matters

### Step 5: Baseline Model (Part 4)

Build your first model:

1. Create a DecisionTreeClassifier with max_depth=3
2. Train on the training set
3. Evaluate on the test set
4. Create a confusion matrix
5. Interpret the results

### Step 6: Documentation (Part 5)

Complete the documentation section:

1. Fill in the feature selection table
2. Summarize preprocessing decisions
3. Record baseline performance metrics
4. List improvements for next week

---

## Grading Criteria

This workshop is for practice and feedback. Focus on:

| Criterion | What we look for |
|-----------|------------------|
| Problem Definition | Clear problem statement with justification |
| Feature Selection | Thoughtful selection with documented rationale |
| Data Preparation | Correct implementation of split and scaling |
| Model Implementation | Working model with proper evaluation |
| Documentation | Clear, complete documentation of all decisions |

---

## Tips for Success

### Before You Start
- Review Week 13 slides on ML fundamentals
- Remember the difference between classification and regression
- Think about what "data leakage" means

### While Working
- Document your decisions as you make them (not at the end)
- Test each step before moving to the next
- If stuck, simplify the problem first

### Common Mistakes to Avoid
- Using the target variable as a feature (data leakage!)
- Fitting the scaler on test data (data leakage!)
- Forgetting to encode categorical variables
- Not checking class balance in train/test sets

### If Stuck
- Re-read the cell instructions
- Check the scikit-learn documentation
- Review the in-class exercise
- Only check the solution notebook as a last resort

---

## Key Concepts Reference

### Train/Test Split
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing
    random_state=42     # For reproducibility
)
```

### StandardScaler
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit AND transform
X_test_scaled = scaler.transform(X_test)        # Only transform
```

### Label Encoding
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])
```

### Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Evaluation Metrics
```python
from sklearn.metrics import accuracy_score, confusion_matrix

accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
```

---

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the deadline.

Ensure that:
- [ ] All cells have been executed (Kernel > Restart & Run All)
- [ ] Problem statement is clearly defined
- [ ] Feature selection is documented with rationale
- [ ] Train/test split is correctly implemented
- [ ] Feature scaling is properly applied
- [ ] Baseline model is trained and evaluated
- [ ] All documentation sections are complete

---

## Connection to Project

These techniques are essential for your final project:

| Workshop Skill | Project Application |
|----------------|---------------------|
| Problem definition | Framing your project's ML question |
| Feature selection | Choosing predictors for your model |
| Data preparation | Preprocessing your datos.gov.co dataset |
| Model building | Implementing predictions for Milestone 3 |
| Documentation | ML methodology section of your report |

---

## Resources

- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
- Train/Test Split: https://scikit-learn.org/stable/modules/cross_validation.html
- Decision Trees: https://scikit-learn.org/stable/modules/tree.html
- Feature Scaling: https://scikit-learn.org/stable/modules/preprocessing.html

---

*Week 13 - Data Analytics Course - Universidad Cooperativa de Colombia*
