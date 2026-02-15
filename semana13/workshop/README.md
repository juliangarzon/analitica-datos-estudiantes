# Week 13 Workshop: Inferential Statistics - Confidence Intervals & Hypothesis Testing

## Overview

In this workshop, you will apply inferential statistics techniques to draw conclusions about population parameters using the Education Statistics dataset from Colombia's Ministry of Education (MEN_ESTADISTICAS).

**Duration:** 2-3 hours (independent work)

**Deadline:** Before Week 14 class

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Calculate and interpret confidence intervals for different metrics
2. Formulate and test statistical hypotheses
3. Perform and interpret t-tests for group comparisons
4. Translate statistical results into business language
5. Visualize statistical significance effectively

---

## Dataset

**Source:** datos.gov.co - MEN_ESTADISTICAS

**Description:** Education statistics from the Colombian Ministry of Education containing:
- Enrollment numbers by department, municipality, and education level
- Dropout and graduation rates
- Demographic breakdowns (gender, urban/rural, etc.)
- Historical data across multiple years

This is the same dataset you worked with in Week 3 (Data Cleaning) and subsequent weeks.

---

## Workshop Structure

### Part 1: Confidence Intervals for 3 Metrics

You will calculate 95% confidence intervals for:

| Metric | What it tells us |
|--------|------------------|
| 1. Mean enrollment | Average number of students per record |
| 2. Dropout rate | Average dropout percentage |
| 3. Approval rate | Average approval/pass rate |

For each, you must:
- Calculate the CI manually AND using scipy
- Interpret the CI in plain language
- Visualize the CI on a distribution plot

### Part 2: Hypothesis Testing (2 Tests)

You will perform two hypothesis tests:

| Test | Comparison |
|------|------------|
| 1. Urban vs Rural | Compare dropout rates between urban and rural areas |
| 2. Time Comparison | Compare enrollment between two different years |

For each test, you must:
- State the null and alternative hypotheses
- Perform the appropriate test (t-test)
- Report the t-statistic and p-value
- Make a decision at alpha = 0.05
- Write a conclusion in business language

### Part 3: Business Interpretation

Translate your findings into language that a non-technical stakeholder (e.g., Ministry official, school administrator) would understand.

### Part 4: Visualization of Statistical Significance

Create publication-quality visualizations that:
- Show the distributions being compared
- Indicate whether differences are significant
- Include confidence intervals where appropriate

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
2. Run the setup cell to load libraries and dataset
3. Review the dataset structure

### Step 2: Confidence Intervals (Part 1)

For each of the 3 metrics:
1. Extract the relevant column
2. Calculate sample statistics (mean, std, n)
3. Compute the confidence interval
4. Verify using `scipy.stats.t.interval()`
5. Create a visualization
6. Write the interpretation

### Step 3: Hypothesis Tests (Part 2)

For each of the 2 tests:
1. Define H0 and H1 clearly
2. Prepare the two groups
3. Check assumptions (sample size, approximate normality)
4. Perform the t-test using `scipy.stats.ttest_ind()`
5. Report results and make a decision
6. Write the conclusion

### Step 4: Business Interpretation (Part 3)

Write a brief executive summary (5-7 sentences) that:
- Summarizes key findings
- Explains what they mean for education policy
- Avoids statistical jargon

### Step 5: Visualization (Part 4)

Create at least 2 visualizations:
1. A comparison plot (boxplot or distribution overlay) with significance annotation
2. A confidence interval plot showing the 3 metrics

---

## Grading Criteria

This workshop is for practice and feedback. Focus on:

| Criterion | What we look for |
|-----------|------------------|
| Completeness | All tasks attempted |
| Correctness | Proper statistical methods used |
| Interpretation | Results explained correctly, avoiding common p-value mistakes |
| Visualization | Clear, informative plots with proper labels |
| Business Language | Technical findings translated for non-technical audience |

---

## Tips for Success

### Before You Start
- Review the class slides on confidence intervals and hypothesis testing
- Remember the formula: CI = mean +/- t * (std / sqrt(n))
- Know the difference between t-test types (independent vs paired)

### While Working
- Always check for missing values before calculations
- Use `dropna()` to clean data before statistical tests
- Remember: p-value < 0.05 means reject H0 (at alpha = 0.05)
- Statistical significance != practical significance

### Common Mistakes to Avoid
- Saying "p-value is the probability H0 is true" (WRONG!)
- Using paired t-test when groups are independent
- Forgetting to state your hypotheses before testing
- Ignoring sample size when interpreting results

### If Stuck
- Re-read the cell instructions carefully
- Check the scipy.stats documentation
- Try a simpler version first
- Only check the solution notebook as a last resort

---

## Key Formulas Reference

### Confidence Interval for Mean
```
CI = x_bar +/- t_critical * (s / sqrt(n))

Where:
- x_bar = sample mean
- t_critical = t-value for desired confidence level
- s = sample standard deviation
- n = sample size
```

### Standard Error
```
SE = s / sqrt(n)
```

### T-Statistic (two independent samples)
```
t = (x1_bar - x2_bar) / sqrt(s1^2/n1 + s2^2/n2)
```

### Decision Rule
```
If p-value < alpha: Reject H0
If p-value >= alpha: Fail to reject H0
```

---

## Submission

Submit your completed `workshop_starter.ipynb` via the course LMS before the deadline.

Ensure that:
- All cells have been executed (Kernel > Restart & Run All)
- All confidence intervals are calculated and interpreted
- Both hypothesis tests are complete with conclusions
- The business summary is written
- Visualizations are clear and labeled

---

## Connection to Project

These techniques will be essential for your final project:

| Workshop Skill | Project Application |
|----------------|---------------------|
| Confidence intervals | Estimate population parameters from your sample |
| Hypothesis testing | Compare groups in your datos.gov.co dataset |
| Business interpretation | Executive summary section of your report |
| Statistical visualization | Results section of your presentation |

---

## Resources

- scipy.stats documentation: https://docs.scipy.org/doc/scipy/reference/stats.html
- Understanding p-values: https://www.nature.com/articles/nmeth.2698
- Common statistical mistakes: https://www.nature.com/articles/nmeth.2900
- Visualizing uncertainty: https://clauswilke.com/dataviz/

---

*Week 13 - Data Analytics Course - Universidad Cooperativa de Colombia*
