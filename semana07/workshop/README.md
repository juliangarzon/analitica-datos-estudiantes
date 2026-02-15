# Week 7 Workshop: Bivariate & Multivariate Analysis

## Water Consumption Dataset - Deep Dive into Relationships

**Duration:** 2 hours (homework or in-class workshop)

**Dataset:** HISTORICO_CONSUMO (Water Consumption Data)

---

## Objectives

By completing this workshop, you will:

1. Build a complete correlation matrix analysis
2. Test if relationships change by municipality
3. Generate 5 actionable insights from bivariate analysis
4. Practice the critical thinking skill of distinguishing correlation from causation

---

## Workshop Tasks

### Part 1: Complete Correlation Matrix Analysis (45 minutes)

**Task 1.1: Calculate and Visualize Correlations**

1. Load the water consumption dataset
2. Calculate the correlation matrix for all numeric variables
3. Create a professional heatmap visualization with:
   - Clear color scheme (RdYlGn or coolwarm)
   - Annotation showing correlation values
   - Appropriate title and labels

**Task 1.2: Identify Key Correlations**

1. Extract all unique correlations (not duplicates, not diagonal)
2. Rank them by absolute value
3. Document the top 5 correlations with their:
   - Variable pair
   - Correlation coefficient (r)
   - Interpretation (positive/negative, strong/moderate/weak)

**Task 1.3: Scatter Plot Analysis**

For each of the top 3 correlations:
1. Create a scatter plot with regression line
2. Check for non-linear patterns
3. Identify any outliers that might affect the correlation
4. Document your observations

---

### Part 2: Test Relationships by Municipality (45 minutes)

**Task 2.1: Select Key Variables**

Choose two numeric variables that showed interesting correlation in Part 1.
For example:
- CONSUMO_FACTURADO vs NUMERO_SUSCRIPTORES
- CONSUMO_FACTURADO vs VALOR_FACTURADO

**Task 2.2: Calculate Correlations by Group**

1. Group the data by MUNICIPIO (or DEPARTAMENTO if too many municipalities)
2. Calculate the correlation for each group
3. Create a summary table showing:
   - Municipality name
   - Sample size (n)
   - Correlation coefficient (r)

**Task 2.3: Visualize Differences**

1. Create a scatter plot colored by municipality (use top 5-10 municipalities)
2. Compare the slopes visually
3. Answer: Does the relationship change significantly by municipality?

**Task 2.4: Simpson's Paradox Check**

1. Calculate the overall correlation (all data combined)
2. Calculate correlations for each subgroup
3. Document any cases where subgroup patterns differ from overall pattern

---

### Part 3: Generate 5 Actionable Insights (30 minutes)

Based on your bivariate and multivariate analysis, generate 5 insights that could inform decision-making.

**For each insight, document:**

1. **Finding:** What did you discover? (Be specific with numbers)
2. **So What?:** Why does this matter for the water utility company?
3. **Now What?:** What action could be taken based on this finding?
4. **Caution:** Is this correlation or causation? What confounding variables might exist?

**Example Insight Template:**

```
Insight #1: [Title]
---------------------------------------------------------
Finding: There is a strong positive correlation (r = 0.XX)
         between [Variable A] and [Variable B].

So What?: This suggests that [interpretation of business impact]

Now What?: The utility company could [specific action]

Caution: This is correlation, not causation. Possible
         confounding variable: [variable that might explain both]
```

---

## Deliverables

Your completed workshop should include:

1. **Jupyter Notebook** with:
   - All code cells executed
   - Clear markdown explanations
   - Professional visualizations
   - Answers to all questions

2. **Correlation Summary Table**
   | Variable 1 | Variable 2 | r | Interpretation |
   |------------|------------|---|----------------|
   | ... | ... | ... | ... |

3. **Municipality Comparison Table**
   | Municipality | n | r | Notes |
   |--------------|---|---|-------|
   | ... | ... | ... | ... |

4. **5 Actionable Insights** (documented as shown above)

---

## Grading Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| Correlation Analysis | 25 | Correct calculations, complete matrix |
| Visualizations | 25 | Clear, labeled, professional charts |
| Municipality Comparison | 20 | Correct grouping and comparison |
| Insights Quality | 20 | Specific, actionable, well-reasoned |
| Code Quality | 10 | Clean, commented, reproducible |
| **Total** | **100** | |

---

## Tips for Success

### Correlation Interpretation Guide

| r Value | Interpretation |
|---------|---------------|
| 0.7 to 1.0 | Strong positive |
| 0.3 to 0.7 | Moderate positive |
| 0.0 to 0.3 | Weak positive |
| -0.3 to 0.0 | Weak negative |
| -0.7 to -0.3 | Moderate negative |
| -1.0 to -0.7 | Strong negative |

### Common Pitfalls to Avoid

1. **Assuming causation from correlation**
   - Always ask: "Could there be a third variable?"
   - Use phrases like "is associated with" not "causes"

2. **Ignoring sample size**
   - Small groups can show spurious correlations
   - Report n alongside r

3. **Missing non-linear relationships**
   - Always create scatter plots, not just numbers
   - Correlation only measures LINEAR relationships

4. **Forgetting about outliers**
   - Outliers can artificially inflate or deflate correlation
   - Consider robust alternatives if outliers are present

### Key Python Functions

```python
# Correlation matrix
df.corr()

# Single correlation
df['var1'].corr(df['var2'])

# Correlation by group
df.groupby('category').apply(lambda x: x['var1'].corr(x['var2']))

# Heatmap
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0)

# Scatter with regression
sns.regplot(x='var1', y='var2', data=df)

# Scatter with color by category
sns.scatterplot(x='var1', y='var2', hue='category', data=df)
```

---

## Files Provided

- `workshop_starter.ipynb` - Starter notebook with structure
- `workshop_solution.ipynb` - Complete solution (for reference after completion)

---

## Submission

Submit your completed notebook via the course platform by [deadline].

Name your file: `Week5_Workshop_[YourName].ipynb`

---

*Good luck! Remember: Correlation does NOT equal causation!*
