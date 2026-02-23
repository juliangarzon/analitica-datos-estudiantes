# Milestone 1: Exploratory Data Analysis Evaluation Rubric

**Course**: Data Analytics
**Universidad Cooperativa de Colombia**
**Instructor**: Julian Eduardo Garzon Giraldo, MsC

---

## Overview

Milestone 1 evaluates your ability to clean a dataset, perform univariate exploratory analysis, and conduct bivariate/multivariate analysis to uncover relationships in the data.

| Criterion | Weight | Max Points |
|-----------|--------|------------|
| Data Cleaning | 20% | 5 |
| Univariate Analysis | 20% | 5 |
| Bivariate/Multivariate Analysis | 25% | 5 |
| Statistics Application | 15% | 5 |
| Insights & Interpretation | 10% | 5 |
| Code Quality | 10% | 5 |
| **Total** | **100%** | **30** |

---

## Criterion 1: Data Cleaning (20%)

Evaluates the thoroughness and correctness of data preparation steps.

| Score | Description |
|-------|-------------|
| **5 - Excellent** | All data quality issues identified and handled appropriately. Missing values addressed with justified strategy (drop, fill, impute). Data types corrected. Duplicates detected and removed with explanation. String inconsistencies cleaned. Before/after comparison provided. |
| **4 - Good** | Most data quality issues addressed. Missing value strategy is reasonable. Data types mostly correct. Duplicates handled. Minor issues may remain but do not affect analysis. |
| **3 - Acceptable** | Basic cleaning performed (missing values dropped or filled). Some data type issues remain. Duplicates checked but handling may be incomplete. Limited documentation of cleaning decisions. |
| **2 - Below Expectations** | Minimal cleaning. Missing values handled without justification. Data type problems not addressed. No duplicate check. Cleaning steps not documented. |
| **1 - Not Acceptable** | No meaningful data cleaning performed, or cleaning introduces errors (e.g., dropping too many rows without explanation, filling missing values with inappropriate values). |

### Key Questions to Ask
- Were all missing values identified and handled with a justified strategy?
- Are data types appropriate for each column?
- Were duplicates checked and handled?
- Is there a before/after summary showing the impact of cleaning?

---

## Criterion 2: Univariate Analysis (20%)

Evaluates the depth and correctness of single-variable exploration.

| Score | Description |
|-------|-------------|
| **5 - Excellent** | All key variables analyzed individually. Numeric variables explored with histograms, boxplots, and summary statistics (mean, median, std, quartiles). Categorical variables explored with value counts and bar charts. Distributions described and interpreted. Outliers identified and discussed. |
| **4 - Good** | Most key variables analyzed. Appropriate chart types used for numeric and categorical variables. Summary statistics calculated. Some interpretation provided. Minor variables may be skipped. |
| **3 - Acceptable** | Several variables analyzed but not comprehensively. Charts created but may not always be the best type. Summary statistics present but interpretation is shallow. Some variables ignored without justification. |
| **2 - Below Expectations** | Few variables analyzed. Charts are basic or inappropriate for the data type. Limited summary statistics. No meaningful interpretation of distributions. |
| **1 - Not Acceptable** | Minimal or no univariate analysis. Charts are missing or incorrect. No summary statistics. No evidence of exploring individual variables. |

### What Makes Strong Univariate Analysis

**Strong Example:**
> "The distribution of water consumption is right-skewed (mean=145, median=98), indicating most consumers use moderate amounts while a few heavy users pull the average up. The IQR is 52-178, and we identified 23 outliers above 450 units."

**Weak Example:**
> "Here is a histogram of water consumption."

### Checklist
- [ ] Numeric variables: histogram + boxplot + descriptive statistics
- [ ] Categorical variables: value counts + bar chart
- [ ] Distribution shape described (normal, skewed, bimodal)
- [ ] Outliers identified and discussed
- [ ] All key variables covered (not just one or two)

---

## Criterion 3: Bivariate/Multivariate Analysis (25%)

Evaluates the depth and correctness of relationship exploration between variables.

| Score | Description |
|-------|-------------|
| **5 - Excellent** | Comprehensive correlation analysis with heatmap for numeric variables. Scatter plots for key variable pairs with trend lines or annotations. Cross-tabulations for categorical variable relationships. Grouped comparisons using groupby with meaningful aggregations. Relationships interpreted in context and connected to research questions. |
| **4 - Good** | Correlation matrix calculated and visualized. Several scatter plots for important relationships. Some cross-tabulations or grouped comparisons present. Interpretation connects findings to research questions. |
| **3 - Acceptable** | Basic correlation analysis performed but interpretation is shallow. A few scatter plots created but may not target the most relevant pairs. Limited cross-tabulations. Grouped comparisons present but not well explained. |
| **2 - Below Expectations** | Only scatter plots with no correlation analysis. No cross-tabulations or grouped comparisons. Relationships identified but not interpreted. Missing heatmap or correlation matrix. |
| **1 - Not Acceptable** | No bivariate or multivariate analysis performed, or analysis is fundamentally incorrect (e.g., correlating categorical variables without encoding, misinterpreting correlation coefficients). |

### What Makes Strong Bivariate Analysis

**Strong Example:**
> "Water consumption shows a moderate positive correlation with household size (r=0.62, p<0.001). The scatter plot reveals two distinct clusters: apartments (lower consumption, smaller households) and houses (higher consumption, larger households). Cross-tabulation confirms that residential type is a confounding variable."

**Weak Example:**
> "Here is a scatter plot of consumption vs household size."

### Checklist
- [ ] Correlation matrix calculated for all numeric variables
- [ ] Heatmap visualization of correlation matrix
- [ ] Scatter plots for top 3-5 correlated variable pairs
- [ ] Cross-tabulations for categorical variable relationships
- [ ] Grouped comparisons (groupby + aggregation) for key segments
- [ ] Relationships interpreted, not just displayed

---

## Criterion 4: Statistics Application (15%)

Evaluates correct use and interpretation of descriptive statistics.

| Score | Description |
|-------|-------------|
| **5 - Excellent** | Correct calculation and interpretation of central tendency (mean, median, mode), dispersion (std, IQR, range), and shape (skewness). Statistics chosen appropriately for data type. Comparisons between groups using groupby where relevant. Clear connection between statistics and research questions. |
| **4 - Good** | Most statistics correctly calculated and interpreted. Appropriate measures chosen for data type. Some group comparisons present. Connection to research questions is evident. |
| **3 - Acceptable** | Basic statistics calculated (mean, std) but interpretation may be incomplete. May use inappropriate measures for data type (e.g., mean for highly skewed data). Limited group comparisons. |
| **2 - Below Expectations** | Statistics calculated but not interpreted. May confuse measures or apply them incorrectly. No group comparisons. No connection to research questions. |
| **1 - Not Acceptable** | Statistics missing, incorrect, or misinterpreted. Demonstrates fundamental misunderstanding of descriptive statistics. |

### Key Concepts to Demonstrate
- When to use mean vs median (skewed distributions)
- Standard deviation vs IQR for measuring spread
- How outliers affect different statistics
- Groupby aggregations to compare subgroups

---

## Criterion 5: Insights & Interpretation (10%)

Evaluates the ability to extract meaningful findings from the analysis.

| Score | Description |
|-------|-------------|
| **5 - Excellent** | Clear, specific insights derived from the data. Findings directly address research questions. Unexpected patterns noted and discussed. Limitations acknowledged. Insights are actionable and relevant to stakeholders. |
| **4 - Good** | Solid insights that connect to research questions. Most findings are well-supported by the data. Some awareness of limitations. |
| **3 - Acceptable** | Insights present but may be obvious or surface-level. Connection to research questions exists but could be stronger. Limited discussion of what the findings mean. |
| **2 - Below Expectations** | Insights are vague, generic, or unsupported by the analysis. Research questions not addressed. No discussion of limitations. |
| **1 - Not Acceptable** | No insights provided, or stated conclusions contradict the data shown. |

### What Makes a Strong Insight

**Strong:**
> "Municipalities in the Andean region consume 35% less water per capita than coastal municipalities (median 87 vs 134 units), suggesting climate and water availability drive consumption patterns. This could inform differentiated conservation policies."

**Weak:**
> "Some places use more water than others."

---

## Criterion 6: Code Quality (10%)

Evaluates the technical quality and reproducibility of the notebook.

| Score | Description |
|-------|-------------|
| **5 - Excellent** | Code is clean, well-organized, and well-commented. Notebook runs top-to-bottom without errors. Markdown cells explain each section. Variable names are descriptive. No unnecessary code or output. |
| **4 - Good** | Code is organized and mostly commented. Notebook runs with minimal issues. Some markdown explanations present. |
| **3 - Acceptable** | Code works but may be disorganized. Limited comments. Some cells may need manual intervention to run. |
| **2 - Below Expectations** | Code has errors or requires significant manual fixes. No comments or markdown. Poor organization. |
| **1 - Not Acceptable** | Code does not run. Major errors throughout. No organization. |

### Code Quality Checklist
- [ ] Notebook runs top-to-bottom (Kernel > Restart & Run All)
- [ ] Markdown cells introduce each section
- [ ] Code cells have comments explaining non-obvious logic
- [ ] Variable names are descriptive (not x, y, df2, temp)
- [ ] No unnecessary print statements or debug output
- [ ] Imports at the top of the notebook

---

## Scoring Sheet Template

**Team Name**: ________________________
**Date**: ________________________
**Evaluator**: ________________________

| Criterion | Score (1-5) | Weight | Weighted Score | Comments |
|-----------|-------------|--------|----------------|----------|
| Data Cleaning | | 20% | | |
| Univariate Analysis | | 20% | | |
| Bivariate/Multivariate Analysis | | 25% | | |
| Statistics Application | | 15% | | |
| Insights & Interpretation | | 10% | | |
| Code Quality | | 10% | | |
| **Total** | | **100%** | | |

### Calculation
Weighted Score = (Score x Weight) for each criterion
Final Score = Sum of Weighted Scores

### Grade Conversion

| Total Weighted Score | Grade |
|---------------------|-------|
| 4.5 - 5.0 | A (Excellent) |
| 4.0 - 4.4 | B (Good) |
| 3.0 - 3.9 | C (Acceptable) |
| 2.0 - 2.9 | D (Needs Improvement) |
| Below 2.0 | F (Unacceptable) |

---

## Feedback Template

### Strengths
1.
2.
3.

### Areas for Improvement
1.
2.
3.

### Required Revisions (if any)
- [ ]
- [ ]

### Deadline for Revisions
________________________

---

## Common Deductions

| Issue | Typical Impact |
|-------|---------------|
| Dataset not from datos.gov.co (unapproved) | -1 to -2 points on Data Cleaning |
| No missing value strategy documented | -1 point on Data Cleaning |
| Only histograms, no boxplots or stats | -1 point on Univariate Analysis |
| Only scatter plots, no correlation analysis | -3 points on Bivariate/Multivariate Analysis |
| No grouped comparisons or cross-tabulations | -2 points on Bivariate/Multivariate Analysis |
| Missing heatmap for correlation matrix | -2 points on Bivariate/Multivariate Analysis |
| Statistics calculated but not interpreted | -1 point on Statistics Application |
| Notebook does not run top-to-bottom | -1 to -2 points on Code Quality |
| No markdown explanations in notebook | -1 point on Code Quality |
| Plagiarism or copied code without attribution | Automatic 0 + academic integrity review |

---

## Deliverables Checklist

Students must submit:
- [ ] Jupyter notebook (.ipynb) with complete EDA
- [ ] Dataset file or clear instructions to download it
- [ ] Notebook runs without errors (Kernel > Restart & Run All)
- [ ] All research questions addressed through univariate and bivariate analysis

---

## Appeals Process

Students may request a re-evaluation within 5 business days of receiving their score. Appeals must include:
1. Specific criterion being contested
2. Justification for why the score should be higher
3. Any supporting evidence not included in the original submission

Re-evaluations will be conducted by the instructor and, if necessary, a second faculty member.
