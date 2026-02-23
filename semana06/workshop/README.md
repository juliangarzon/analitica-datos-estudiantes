# Week 6 Workshop: Bivariate & Multivariate Analysis

## Saber Pro Test Scores - Deep Dive into Relationships

**Duration:** 2 hours (homework or in-class workshop)

**Dataset:** Saber Pro university test scores (datos.gov.co)

**Source:** https://www.datos.gov.co/resource/g6ci-7e9g

---

## Objectives

By completing this workshop, you will:

1. Build a complete correlation matrix analysis of test scores
2. Test if relationships change by institution type or socioeconomic group
3. Generate 5 actionable insights from bivariate analysis
4. Practice the critical thinking skill of distinguishing correlation from causation

---

## Dataset Description

The **Saber Pro** exam is Colombia's national standardized test for university students. This dataset contains 25,362 records with test scores across multiple competency areas and demographic information.

### Key Variables

**Test Scores (numeric):**
- `puntaje_global` - Overall global score (composite)
- `punt_comp_ciud` - Citizen competency score
- `punt_comu_escr` - Written communication score
- `punt_ingles` - English score
- `punt_lect_crit` - Critical reading score
- `punt_razo_cuant` - Quantitative reasoning score

**Grouping Variables (categorical):**
- `sexo` - Gender ("Hombres" / "Mujeres")
- `estrato` - Socioeconomic stratum (1-6, ND, NE)
- `tipo_col` - Institution type ("Oficial" / "Privado")
- `dep_proc` - Department of origin
- `year` - Year of exam

---

## Workshop Tasks

### Part 1: Complete Correlation Matrix Analysis (45 minutes)

**Task 1.1: Calculate and Visualize Correlations**

1. Calculate the correlation matrix for the 6 test score columns
2. Create a professional heatmap visualization with:
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

### Part 2: Test Relationships by Group (45 minutes)

**Task 2.1: Select Key Variables**

Choose two numeric variables from your top correlations and one grouping variable.
For example:
- `punt_razo_cuant` vs `puntaje_global` grouped by `tipo_col`
- `punt_ingles` vs `punt_lect_crit` grouped by `sexo`

**Task 2.2: Calculate Correlations by Group**

1. Group the data by your chosen categorical variable
2. Calculate the correlation for each group
3. Create a summary table showing:
   - Group name
   - Sample size (n)
   - Correlation coefficient (r)

**Task 2.3: Visualize Differences**

1. Create a scatter plot colored by group (use top 5 groups if many categories)
2. Compare the slopes visually
3. Answer: Does the relationship change significantly by group?

**Task 2.4: Simpson's Paradox Check**

1. Calculate the overall correlation (all data combined)
2. Calculate correlations for each subgroup
3. Document any cases where subgroup patterns differ from overall pattern

---

### Part 3: Generate 5 Actionable Insights (30 minutes)

Based on your bivariate and multivariate analysis, generate 5 insights that could inform education policy.

**For each insight, document:**

1. **Finding:** What did you discover? (Be specific with numbers)
2. **So What?:** Why does this matter for education?
3. **Now What?:** What action could be taken based on this finding?
4. **Caution:** Is this correlation or causation? What confounding variables might exist?

**Example Insight Template:**

```
Insight #1: [Title]
---------------------------------------------------------
Finding: There is a strong positive correlation (r = 0.XX)
         between [Variable A] and [Variable B].

So What?: This suggests that [interpretation of impact]

Now What?: Universities could [specific action]

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

3. **Group Comparison Table**
   | Group | n | r | Notes |
   |-------|---|---|-------|
   | ... | ... | ... | ... |

4. **5 Actionable Insights** (documented as shown above)

---

## Grading Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| Correlation Analysis | 25 | Correct calculations, complete matrix |
| Visualizations | 25 | Clear, labeled, professional charts |
| Group Comparison | 20 | Correct grouping and comparison |
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
df[score_cols].corr()

# Single correlation
df['punt_razo_cuant'].corr(df['puntaje_global'])

# Correlation by group
df.groupby('tipo_col').apply(lambda x: x['punt_razo_cuant'].corr(x['puntaje_global']))

# Heatmap
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0)

# Scatter with regression
sns.regplot(x='punt_razo_cuant', y='puntaje_global', data=df)

# Scatter with color by category
sns.scatterplot(x='punt_razo_cuant', y='puntaje_global', hue='tipo_col', data=df)
```

---

## Files Provided

- `workshop_starter.ipynb` - Starter notebook with structure and helper functions
- `workshop_solution.ipynb` - Complete solution (for reference after completion)

---

## Submission

Submit your completed notebook via the course platform by [deadline].

Name your file: `Week6_Workshop_[YourName].ipynb`

---

*Good luck! Remember: Correlation does NOT equal causation!*
