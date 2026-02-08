# Week 3 Workshop: Data Manipulation & Cleaning

## Overview

In this workshop, you will practice data cleaning and manipulation techniques using the Education Statistics dataset from Colombia's Ministry of Education (MEN_ESTADISTICAS).

**Duration:** 2-3 hours (independent work)

**Deadline:** Before Week 4 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Identify and diagnose data quality issues
2. Handle missing values using appropriate strategies
3. Convert data types correctly
4. Filter data with multiple conditions
5. Aggregate data using GroupBy operations
6. Document your cleaning decisions

---

## Dataset

**Source:** datos.gov.co - MEN_ESTADISTICAS

**Description:** Education statistics from the Colombian Ministry of Education containing:
- Enrollment numbers by department, municipality, and education level
- Dropout and graduation rates
- Demographic breakdowns (gender, urban/rural, etc.)
- Historical data across multiple years

**Size:** ~14,585 records, 41+ columns

---

## Workshop Structure

### Part 1: Data Quality Assessment (5 issues to fix)

You will diagnose and fix these 5 common data quality issues:

| Issue | Description | Technique |
|-------|-------------|-----------|
| 1 | Missing values in numeric columns | `fillna()` |
| 2 | Missing values in categorical columns | `dropna()` or `fillna()` |
| 3 | Incorrect data types | `astype()` |
| 4 | Duplicate rows | `drop_duplicates()` |
| 5 | Inconsistent categorical values | `str.upper()`, `str.strip()` |

### Part 2: Data Aggregation Tasks

After cleaning, you will perform aggregation analyses:

1. **By Region:** Total enrollment by department
2. **By Education Level:** Average dropout rate by education level (primary, secondary, etc.)
3. **By Year:** Trend analysis of key metrics over time
4. **Combined:** Multi-level grouping (department + year + level)

---

## Files Provided

| File | Description |
|------|-------------|
| `workshop_starter.ipynb` | Starter notebook with empty cells for your work |
| `workshop_solution.ipynb` | Complete solution (only look after attempting!) |

---

## Instructions

### Step 1: Setup

1. Open `workshop_starter.ipynb` in Jupyter or VS Code
2. Run the setup cell to load the dataset
3. Review the dataset structure

### Step 2: Data Quality Assessment

For each of the 5 issues:
1. Diagnose the problem (use inspection techniques)
2. Document what you found
3. Apply the appropriate fix
4. Verify the fix worked

### Step 3: Data Aggregation

Complete each aggregation task:
1. Write the GroupBy code
2. Interpret the results
3. Answer the analysis questions

### Step 4: Documentation

Answer the reflection questions at the end:
- What was the most challenging issue?
- How would you handle this in your project?
- What decisions would require domain expertise?

---

## Grading Criteria

This workshop is for practice and feedback. Focus on:

| Criterion | What we look for |
|-----------|------------------|
| Completeness | All tasks attempted |
| Correctness | Appropriate techniques used |
| Documentation | Cleaning decisions explained |
| Code Quality | Clean, readable code with comments |

---

## Tips for Success

### Before You Start
- Read through the entire notebook to understand the scope
- Review your class notes on `fillna()`, `dropna()`, `astype()`, `groupby()`

### While Working
- Check the data type BEFORE converting (some columns may already be correct)
- Remember: `fillna()` returns a new object, use assignment or `inplace=True`
- Use parentheses around each condition when filtering: `(cond1) & (cond2)`

### If Stuck
- Re-read the cell instructions carefully
- Check the professor notes from class
- Try a simpler version first, then expand
- Only check the solution notebook as a last resort

---

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the deadline.

Ensure that:
- All cells have been executed (run all)
- Your code produces the expected outputs
- Your documentation cells are filled in

---

## Connection to Project

These exact techniques will be needed for Milestone 1:

| Workshop Skill | Project Application |
|----------------|---------------------|
| Missing value handling | Clean your datos.gov.co dataset |
| Type conversion | Ensure numeric columns are numeric |
| GroupBy | Create summary statistics by category |
| Documentation | Data cleaning section of your report |

---

## Resources

- Pandas Missing Data Guide: https://pandas.pydata.org/docs/user_guide/missing_data.html
- Real Python - Data Cleaning: https://realpython.com/python-data-cleaning-numpy-pandas/
- Kaggle Learn - Data Cleaning: https://www.kaggle.com/learn/data-cleaning

---

*Week 3 - Data Analytics Course - Universidad Cooperativa de Colombia*
