# Week 3 Workshop: Data Cleaning

## Overview

In this workshop, you will practice data cleaning techniques using the Health Indicators dataset (Mortality and Morbidity) from Colombia's Ministry of Health and Social Protection.

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

**Source:** Ministerio de Salud y Proteccion Social via datos.gov.co

**Description:** Mortality and morbidity indicators for Colombian municipalities including mortality rates (general, infant, neonatal, fetal, maternal), birth indicators (low weight, cesarean rate, institutional deliveries, prenatal checkups), and teen fertility rates.

**Size:** 532 rows (dirty version, ~512 after cleaning) x 15 columns (one row per municipality per year)

**Loading:** Data is loaded from a local CSV file at `../data/indicadores_salud.csv`

**Key columns:** `ano`, `departamento`, `municipio`, `mortalidad_general`, `mortalidad_infantil`, `bajo_peso_nacer`, `partos_institucionales`, `partos_cesarea`

---

## Workshop Structure

### Part 1: Initial Inspection
Run the inspection ritual (shape, head, dtypes, isnull, describe) and diagnose the 5 issues.

### Parts 2-6: Fix the Issues
Each part addresses one data quality issue with code and documentation:

| Part | Issue | Technique |
|------|-------|-----------|
| 2 | Missing values | `fillna()` with 0 for mortalidad_materna, median for rates, `dropna(subset=...)` for departamento |
| 3 | Data types | `pd.to_numeric()`, `astype()`, `str.replace()` for ano and cod_municipio |
| 4 | Duplicates | `duplicated()`, `drop_duplicates()` |
| 5 | Text inconsistencies | `str.upper()`, `str.strip()` on departamento |
| 6 | Invalid values | `describe()` min/max, boolean masks, domain validation on percentage columns |

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
- Check `ano` and `cod_municipio` types early, they may not be what you expect
- Remember: `fillna()` returns a new object, use assignment
- Percentage columns like `bajo_peso_nacer`, `partos_cesarea`, `partos_institucionales` should be between 0 and 100
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
| Type conversion | Ensure `ano` and code columns are integers, rates are floats |
| Duplicate removal | Remove any duplicated records |
| Text standardization | Standardize department and municipality names for grouping |
| Domain validation | Check that mortality rates and percentages fall within valid ranges |
| Documentation | Data cleaning section of your report |

---

## Resources

- Pandas Missing Data Guide: https://pandas.pydata.org/docs/user_guide/missing_data.html
- Real Python - Data Cleaning: https://realpython.com/python-data-cleaning-numpy-pandas/
- Kaggle Learn - Data Cleaning: https://www.kaggle.com/learn/data-cleaning

---

*Week 3 - Data Analytics Course - Universidad Cooperativa de Colombia*
