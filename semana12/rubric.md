# Milestone 2 Evaluation Rubric: Analysis Complete

**Course:** Data Analytics
**Week:** 12
**Total Points:** 100

---

## Scoring Scale

| Score | Level | Description |
|-------|-------|-------------|
| 5 | Excellent | Exceeds expectations; demonstrates mastery and insight |
| 4 | Good | Meets all requirements; solid, professional work |
| 3 | Satisfactory | Meets minimum requirements; acceptable but with gaps |
| 2 | Needs Improvement | Missing important elements; superficial analysis |
| 1 | Unsatisfactory | Major gaps; fundamental misunderstandings |

---

## 1. Data Preparation (20 points)

**Weight:** 20% of total grade

### Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Missing Value Handling | 5 | Strategy documented and justified |
| Outlier Treatment | 5 | Identified, analyzed, and handled appropriately |
| Data Type Corrections | 5 | All variables have correct types |
| Transformation Documentation | 5 | All changes tracked and explained |

### Scoring Guide

**5 - Excellent (18-20 points)**
- All missing values handled with appropriate strategies (deletion, imputation, flagging)
- Clear justification for each decision based on data characteristics
- Outliers identified using multiple methods (IQR, z-score, domain knowledge)
- Outlier treatment aligns with analysis goals (kept, capped, removed)
- All data types correct (dates parsed, categories encoded, numerics validated)
- Complete documentation of all transformations with code and rationale
- Data dictionary or schema provided

**4 - Good (14-17 points)**
- Missing values handled with reasonable strategies
- Some justification for decisions
- Outliers identified and addressed
- Most data types correct
- Transformations documented but may lack some rationale

**3 - Satisfactory (10-13 points)**
- Missing values handled but strategy may be inconsistent
- Minimal justification for decisions
- Outliers identified but treatment may be questionable
- Some data type issues remain
- Basic documentation of changes

**2 - Needs Improvement (6-9 points)**
- Missing values partially addressed
- No justification for decisions
- Outliers not systematically handled
- Multiple data type issues
- Poor or no documentation

**1 - Unsatisfactory (0-5 points)**
- Missing values ignored or improperly handled
- No awareness of data quality issues
- Outliers not considered
- Major data type problems
- No documentation of changes

---

## 2. Exploratory Analysis (20 points)

**Weight:** 20% of total grade

### Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Univariate Analysis | 5 | All variables explored individually |
| Bivariate Analysis | 5 | Relationships between variables examined |
| Pattern Identification | 5 | Meaningful patterns documented |
| Research Question Alignment | 5 | Analysis addresses stated questions |

### Scoring Guide

**5 - Excellent (18-20 points)**
- Complete univariate analysis of all relevant variables
- Distributions, central tendency, and variability examined
- Comprehensive bivariate analysis including target variable relationships
- Correlation analysis with interpretation
- Clear patterns identified and documented with evidence
- Segmentation or grouping explored where relevant
- All research questions directly addressed with findings
- Unexpected patterns noted and explored

**4 - Good (14-17 points)**
- Most variables analyzed individually
- Key bivariate relationships explored
- Several meaningful patterns identified
- Research questions mostly addressed
- Good depth of exploration

**3 - Satisfactory (10-13 points)**
- Basic univariate analysis performed
- Some bivariate analysis
- A few patterns noted
- Research questions partially addressed
- Surface-level exploration

**2 - Needs Improvement (6-9 points)**
- Incomplete univariate analysis
- Limited bivariate analysis
- Few or no patterns identified
- Research questions not clearly connected
- Shallow exploration

**1 - Unsatisfactory (0-5 points)**
- Minimal or no exploratory analysis
- No systematic approach to understanding data
- No patterns identified
- Research questions ignored
- No evidence of data exploration

---

## 3. Visualizations (20 points)

**Weight:** 20% of total grade

### Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Chart Type Selection | 5 | Appropriate charts for data and question |
| Visual Clarity | 5 | Clear, readable, properly formatted |
| Labeling and Titles | 5 | Complete, descriptive, professional |
| Insight Communication | 5 | Charts reveal and communicate insights |

### Scoring Guide

**5 - Excellent (18-20 points)**
- Chart types perfectly match data characteristics and analytical goals
- Histograms for distributions, scatter for relationships, bar for comparisons, etc.
- All charts are immediately readable without explanation
- Color used meaningfully (not decoratively)
- No chart junk, 3D effects, or unnecessary elements
- All axes labeled with variable names and units
- Titles describe the insight, not just the variables
- Legends clear and appropriately positioned
- Visualizations tell a story; insights are immediately apparent
- Best visualizations could stand alone in a report

**4 - Good (14-17 points)**
- Chart types mostly appropriate
- Charts are clear and readable
- Proper labeling throughout
- Insights are visible with minimal explanation

**3 - Satisfactory (10-13 points)**
- Chart types generally appropriate with some poor choices
- Charts readable but could be improved
- Most charts labeled, some missing elements
- Insights present but not always clear

**2 - Needs Improvement (6-9 points)**
- Inappropriate chart types used
- Charts difficult to read
- Missing or incorrect labels
- Insights not communicated effectively

**1 - Unsatisfactory (0-5 points)**
- Wrong chart types throughout
- Charts unreadable or confusing
- No proper labeling
- No insights communicated

---

## 4. Statistical Analysis (15 points)

**Weight:** 15% of total grade

### Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Method Selection | 5 | Correct statistical tests for questions |
| Assumption Checking | 5 | Test assumptions verified |
| Interpretation | 5 | Results correctly interpreted |

### Scoring Guide

**5 - Excellent (14-15 points)**
- Statistical tests match the research questions and data types
- Correlation for continuous-continuous, chi-square for categorical-categorical, etc.
- Parametric vs non-parametric selection justified
- Assumptions explicitly checked (normality, homogeneity, independence)
- Violations addressed appropriately
- P-values correctly interpreted (not as probability of hypothesis)
- Effect sizes reported alongside significance
- Practical significance discussed
- Confidence intervals used where appropriate
- Limitations of analysis acknowledged

**4 - Good (11-13 points)**
- Appropriate tests selected
- Some assumptions checked
- Generally correct interpretation
- Effect sizes or confidence intervals included

**3 - Satisfactory (8-10 points)**
- Tests mostly appropriate
- Limited assumption checking
- Basic interpretation, may have minor errors
- P-values reported but not deeply understood

**2 - Needs Improvement (4-7 points)**
- Some inappropriate test choices
- No assumption checking
- Interpretation errors present
- Over-reliance on p-values

**1 - Unsatisfactory (0-3 points)**
- Wrong tests used
- No understanding of assumptions
- Major interpretation errors
- Misuse of statistical concepts

---

## 5. Insights Quality (15 points)

**Weight:** 15% of total grade

### Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Actionability | 5 | Insights lead to potential actions |
| Research Question Answers | 5 | Original questions clearly addressed |
| ML Opportunities | 5 | Prediction possibilities identified |

### Scoring Guide

**5 - Excellent (14-15 points)**
- Insights are specific and actionable
- Clear recommendations or implications stated
- Findings would be valuable to stakeholders
- All research questions answered with evidence
- Answers are nuanced, acknowledging complexity
- Unexpected findings explored and explained
- Clear prediction target identified
- Promising features highlighted with reasoning
- Data readiness for ML assessed honestly
- Potential ML challenges identified

**4 - Good (11-13 points)**
- Most insights are actionable
- Research questions answered
- Some ML direction identified
- Good connection between EDA and next steps

**3 - Satisfactory (8-10 points)**
- Some actionable insights
- Research questions partially answered
- Basic ML opportunities noted
- Limited connection between findings and actions

**2 - Needs Improvement (4-7 points)**
- Insights are vague or not actionable
- Research questions not clearly answered
- ML direction unclear
- Findings disconnected from goals

**1 - Unsatisfactory (0-3 points)**
- No actionable insights
- Research questions ignored
- No consideration of ML phase
- No meaningful conclusions

---

## 6. Presentation (10 points)

**Weight:** 10% of total grade

### Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Storytelling | 3 | Clear narrative structure |
| Clarity | 3 | Concepts explained clearly |
| Time Management | 2 | Within time limit, well-paced |
| Q&A Handling | 2 | Responds well to questions |

### Scoring Guide

**5 - Excellent (9-10 points)**
- Presentation tells a coherent story from problem to insights
- Logical flow that builds understanding
- Concepts explained at appropriate level for audience
- Technical details accessible without oversimplification
- Presentation fits within 15 minutes
- Time well-distributed across sections
- All questions answered confidently and correctly
- Can explain methodology and defend decisions

**4 - Good (7-8 points)**
- Good narrative structure
- Concepts mostly clear
- Minor time issues (1-2 minutes over/under)
- Most questions handled well

**3 - Satisfactory (5-6 points)**
- Basic structure present
- Some explanations unclear
- Noticeable time management issues
- Can answer some questions

**2 - Needs Improvement (3-4 points)**
- Poor structure
- Confusing explanations
- Significantly over/under time
- Struggles with questions

**1 - Unsatisfactory (0-2 points)**
- No clear structure
- Cannot explain concepts
- Major time violations
- Cannot answer basic questions

---

## Score Sheet

**Team Name:** _______________________
**Date:** _______________________

| Category | Max Points | Score | Comments |
|----------|------------|-------|----------|
| Data Preparation | 20 | | |
| Exploratory Analysis | 20 | | |
| Visualizations | 20 | | |
| Statistical Analysis | 15 | | |
| Insights Quality | 15 | | |
| Presentation | 10 | | |
| **TOTAL** | **100** | | |

---

## Grade Conversion

| Score | Grade | Description |
|-------|-------|-------------|
| 90-100 | A | Excellent work, ready for ML phase |
| 80-89 | B | Good work, minor improvements needed |
| 70-79 | C | Satisfactory, notable areas to address |
| 60-69 | D | Needs significant improvement |
| Below 60 | F | Does not meet minimum requirements |

---

## Feedback Summary

### Strengths


### Areas for Improvement


### Recommendations for Milestone 3


---

## Evaluator Notes

Use this space for additional observations during the presentation:
