# Week 3 Workshop: Data Cleaning

## Overview

In this workshop, you will practice data cleaning techniques using the Education Statistics dataset from Colombia's Ministry of Education (MEN_ESTADISTICAS).

**Duration:** 2 hours (independent work)

**Deadline:** Before Week 4 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Diagnose data quality issues systematically
2. Handle missing values using appropriate strategies (drop vs. fill)
3. Convert data types correctly
4. Detect and remove duplicate rows
5. Standardize text inconsistencies
6. Document your cleaning decisions with rationale
7. Identify invalid values using domain knowledge

---

## Dataset

**Source:** Ministerio de Educacion Nacional (MEN) via datos.gov.co

**Description:** Education statistics from the Colombian Ministry of Education containing:
- Coverage rates (net and gross) by education level
- Dropout, approval, failure, and repetition rates
- Population data (ages 5-16) by department
- Historical data across multiple years (2011-2024)

**Size:** 482 rows (dirty version, ~462 after cleaning) x 37 columns (one row per department per year)

**Loading:** Data is loaded from a local CSV file at `../data/educacion_estadisticas.csv`

**Key columns:** `ano`, `departamento`, `poblacion_5_16`, `cobertura_neta`, `desercion`, `aprobacion`, `reprobacion`, `repitencia`

---

## Workshop Structure

### Part 1: Initial Inspection
Run the inspection ritual (shape, head, dtypes, isnull, describe) and diagnose the 5 issues.

### Parts 2-6: Fix the Issues
Each part addresses one data quality issue with code and documentation:

| Part | Issue | Technique |
|------|-------|-----------|
| 2 | Missing values | `fillna()` with 0 or median, `dropna(subset=...)` |
| 3 | Data types | `pd.to_numeric()`, `astype()`, `str.replace()` |
| 4 | Duplicates | `duplicated()`, `drop_duplicates()` |
| 5 | Text inconsistencies | `str.upper()`, `str.strip()` |
| 6 | Invalid values | `describe()` min/max, boolean masks, domain validation |

### Part 7: Final Verification
Compare original vs. cleaned dataset statistics, confirm all issues resolved.

### Part 8: Reflection
Answer questions about your cleaning experience and project application.

---

## Files Provided

| File | Description |
|------|-------------|
| `workshop_starter.ipynb` | Starter notebook with scaffolded exercises (hints and structure provided) |
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

### Step 3: Verification

Compare the original and cleaned datasets to quantify your improvements.

### Step 4: Reflection

Answer the reflection questions at the end:
- What was the most challenging issue?
- How would you handle this in your project?
- What decisions would require domain expertise?

---

## Grading Criteria

This workshop is for practice and feedback. Focus on:

| Criterion | What we look for |
|-----------|------------------|
| Completeness | All 5 issues attempted |
| Correctness | Appropriate techniques used |
| Documentation | Cleaning decisions explained with rationale |
| Code Quality | Clean, readable code with comments |

---

## Tips for Success

### Before You Start
- Read through the entire notebook to understand the scope
- Review your class notes on `fillna()`, `dropna()`, `astype()`, `drop_duplicates()`

### While Working
- Check the data type BEFORE converting (some columns may already be correct)
- Remember: `fillna()` returns a new object, use assignment
- Always verify your fix worked before moving to the next issue

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
| Duplicate removal | Remove any duplicated records |
| Text standardization | Standardize categorical values for grouping |
| Domain validation | Identify impossible values using domain knowledge |
| Documentation | Data cleaning section of your report |

---

## Resources

- Pandas Missing Data Guide: https://pandas.pydata.org/docs/user_guide/missing_data.html
- Real Python - Data Cleaning: https://realpython.com/python-data-cleaning-numpy-pandas/
- Kaggle Learn - Data Cleaning: https://www.kaggle.com/learn/data-cleaning

---

*Week 3 - Data Analytics Course - Universidad Cooperativa de Colombia*
