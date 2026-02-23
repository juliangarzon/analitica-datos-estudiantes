# Week 4 Workshop: Data Filtering & Selection

## Overview

| Field | Value |
|-------|-------|
| Topic | Data Filtering & Selection |
| Dataset | Traffic Accident Vehicles (`vehiculos_accidentes`) |
| Duration | ~2 hours |
| Deliverable | Completed notebook with filtering exercises |

Practice filtering techniques to answer analytical questions about vehicles involved in traffic accidents across Colombia. This is independent work with scaffolded hints.

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

**Source:** Ministerio de Transporte via datos.gov.co - Vehiculos Involucrados en un Accidente de Transito

**URL:** https://www.datos.gov.co/resource/6jmc-vaxk

**Size:** ~20,000 records of vehicles involved in traffic accidents in Colombia (December 2022-2025).

### Columns

| Column | Description | Type | Example |
|--------|-------------|------|---------|
| `marca_vehiculo` | Vehicle brand | text | AKT, YAMAHA, CHEVROLET |
| `modelo_vehiculo` | Model year | int | 2026, 2015, 1998 |
| `tipo_vehiculo` | Vehicle type | text | MOTOCICLETA, AUTOMOVIL, CAMIONETA |
| `edad_vehiculo` | Vehicle age in years | float | 1, 10, 25 |
| `fecha_accidente` | Accident date (month/year) | text | 12/2025, 12/2023 |
| `gravedad_accidente` | Accident severity | text | CON HERIDOS, CON MUERTOS |
| `departamento_accidente` | Department | text | ANTIOQUIA, BOGOTA D.C. |
| `municipio_accidente` | Municipality | text | MEDELLIN, BOGOTA, CALI |
| `autoridad_de_transito` | Transit authority | text | STRIA DE TTOyTTE MEDELLIN |

**Loading:** Data is loaded from `../data/vehiculos_accidentes.csv`. No cleaning is needed for this dataset (it is already clean).

---

## Workshop Structure

### Part 1: Single Condition Filters (20 min)
Practice individual filters with each comparison operator. Build confidence with the basic pattern before combining.

### Part 2: Combining Conditions (30 min)
Use AND, OR, and NOT to answer questions that require multiple criteria. Practice both boolean indexing and .isin().

### Part 3: Convenience Methods (20 min)
Use .isin(), .between(), .str.contains(), .str.startswith(), and .query() for common filtering patterns.

### Part 4: Analytical Questions (30 min)
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
2. Run the setup cell to load the dataset
3. Review the dataset structure (columns, value counts, etc.)

### Step 2: Work Through Parts 1-4

For each task:
1. Read the question carefully
2. Translate the question into a filter condition
3. Write and run the code (use the hints provided)
4. Interpret the result (how many rows? which vehicle types? which departments?)

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

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the Week 5 class.

Ensure that:
- All cells have been executed (run all)
- Your code produces the expected outputs
- Your interpretation cells are filled in

---

## Resources

- Pandas Boolean Indexing: https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing
- Pandas .query() Method: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html

---

*Week 4 - Data Analytics Course - Universidad Cooperativa de Colombia*
