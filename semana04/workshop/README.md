# Week 4 Workshop: Data Filtering & Selection

## Overview

In this workshop, you will practice advanced data filtering techniques using the Education Statistics dataset from Colombia's Ministry of Education (MEN_ESTADISTICAS). You will answer real analytical questions by building single and combined filters.

**Duration:** 2 hours (independent work)

**Deadline:** Before Week 5 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Select rows using boolean indexing with comparison operators
2. Combine multiple filter conditions with & (AND), | (OR), ~ (NOT)
3. Use convenience methods: .isin(), .between(), .str.contains()
4. Use .query() for clean filter syntax
5. Answer analytical questions by translating them into filter code

---

## Dataset

**Source:** Ministerio de Educacion Nacional (MEN) via datos.gov.co

**Description:** Same Education Statistics dataset from Week 3, containing:
- Coverage rates (net and gross) by education level
- Dropout, approval, failure, and repetition rates
- Population data (ages 5-16) by department
- Historical data across multiple years (2011-2024)

**Loading:** Data is loaded from `../../semana03/data/educacion_estadisticas.csv`. A quick-clean setup cell applies the Week 3 cleaning steps before you start filtering.

---

## Workshop Structure

### Part 1: Single Condition Filters
Practice individual filters with each comparison operator. Build confidence with the basic pattern before combining.

### Part 2: Combining Conditions
Use AND, OR, and NOT to answer questions that require multiple criteria. Practice with both boolean indexing and .query().

### Part 3: Convenience Methods
Use .isin(), .between(), and .str.contains() for common filtering patterns.

### Part 4: Analytical Questions
Translate real questions into filter code and interpret the results. This is the core skill for EDA.

### Part 5: Reflection
Document your approach and connect filtering skills to your project.

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
2. Run the setup cell to load and quick-clean the dataset
3. Review the dataset structure

### Step 2: Work Through Parts 1-4

For each task:
1. Read the question carefully
2. Translate the question into a filter condition
3. Write and run the code
4. Interpret the result (how many rows? which departments?)

### Step 3: Reflection

Answer the reflection questions at the end about your filtering approach and project application.

---

## Grading Criteria

This workshop is for practice and feedback. Focus on:

| Criterion | What we look for |
|-----------|------------------|
| Completeness | All tasks attempted |
| Correctness | Filters produce expected results |
| Interpretation | Results are explained, not just printed |
| Code Quality | Clean, readable code with comments |

---

## Tips for Success

### Before You Start
- Review the slides on boolean indexing, AND/OR/NOT, and convenience methods
- Familiarize yourself with the column names (run `df.columns.tolist()`)

### While Working
- Always wrap conditions in parentheses when combining with & or |
- Use `na=False` with `.str.contains()` to avoid NaN errors
- Print `len(result)` after each filter to verify the result size makes sense
- Store conditions in named variables for readability

### If Stuck
- Re-read the task instructions and check the pattern examples
- Try building the filter one condition at a time
- Check your class notes or slides
- Only check the solution notebook as a last resort

---

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the deadline.

Ensure that:
- All cells have been executed (run all)
- Your code produces the expected outputs
- Your interpretation cells are filled in

---

## Connection to Project

These filtering skills are essential for Milestone 1:

| Workshop Skill | Project Application |
|----------------|---------------------|
| Single conditions | Focus on a specific year, region, or category |
| Combined conditions | Answer complex questions about your data |
| .isin() | Select specific categories for comparison |
| .between() | Define ranges for numeric analysis |
| .str.contains() | Search within text columns |
| .query() | Write clean, readable filters |

---

## Resources

- Pandas Boolean Indexing: https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing
- Pandas .query() Method: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
- Real Python - Filtering DataFrames: https://realpython.com/python-data-cleaning-numpy-pandas/

---

*Week 4 - Data Analytics Course - Universidad Cooperativa de Colombia*
