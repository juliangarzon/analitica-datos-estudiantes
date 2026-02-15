# Week 5 Workshop: Univariate Analysis

## Overview

| Field | Value |
|-------|-------|
| **Topic** | EDA Part 1 - Univariate Analysis |
| **Dataset** | Water Consumption (HISTORICO_CONSUMO) |
| **Duration** | 60-90 minutes |
| **Deliverable** | Completed notebook with analysis of 3 variables |

---

## Objective

Apply the **5-step univariate analysis framework** to three different variables from the water consumption dataset. Document your findings and determine the appropriate statistics for each variable based on its distribution.

---

## The 5-Step Univariate Framework

For each variable, you must complete:

| Step | What to Do | Key Questions |
|------|------------|---------------|
| 1. **Identify** | Check data type, count non-nulls | Is it numeric or categorical? Any missing values? |
| 2. **Summarize** | Calculate mean, median, mode | Which measure is most appropriate? Why? |
| 3. **Spread** | Calculate std, variance, IQR | How much variability exists? |
| 4. **Visualize** | Create histogram and boxplot | What shape is the distribution? |
| 5. **Detect** | Find outliers using IQR method | How many outliers? What might cause them? |

---

## Variables to Analyze

You must analyze the following **3 variables**:

### Variable 1: CONSUMO_FACTURADO
- **Description:** Billed water consumption in cubic meters (m3)
- **Expected finding:** Right-skewed distribution with upper outliers
- **Story to investigate:** Who are the heavy users?

### Variable 2: VALOR_FACTURADO
- **Description:** Billed amount in Colombian Pesos (COP)
- **Expected finding:** Similar pattern to consumption (they are correlated)
- **Story to investigate:** Does the billing match consumption patterns?

### Variable 3: NUMERO_SUSCRIPTORES
- **Description:** Number of subscribers/users in each municipality
- **Expected finding:** Right-skewed (few large municipalities, many small ones)
- **Story to investigate:** Urban vs rural distribution

---

## Deliverables Checklist

For **each of the 3 variables**, your notebook must include:

- [ ] Data type and non-null count
- [ ] Mean, median, and mode values
- [ ] Mean/median ratio with interpretation
- [ ] Standard deviation and IQR
- [ ] Distribution type classification (choose one):
  - Normal (symmetric)
  - Right-skewed
  - Left-skewed
  - Bimodal
- [ ] Histogram with mean and median lines
- [ ] Box plot
- [ ] Outlier bounds (lower and upper)
- [ ] Number and percentage of outliers
- [ ] One-sentence interpretation

---

## GroupBy Section

After analyzing each variable individually, use **GroupBy** to compare statistics across groups:

| Task | GroupBy Column | Value Column | Operation |
|------|---------------|-------------|-----------|
| 1 | USO (use type) | CONSUMO_FACTURADO | .mean() |
| 2 | ESTRATO (stratum) | CONSUMO_FACTURADO | .median() |
| 3 | DEPARTAMENTO | CONSUMO_FACTURADO | .count() and .sum() |

**Pattern:** `df.groupby('GROUP')['VALUE'].operation()`

---

## Summary Table

At the end of your notebook, create a summary table like this:

| Variable | Mean | Median | Distribution | Outliers (%) | Best Measure |
|----------|------|--------|--------------|--------------|--------------|
| CONSUMO_FACTURADO | ? | ? | ? | ? | ? |
| VALOR_FACTURADO | ? | ? | ? | ? | ? |
| NUMERO_SUSCRIPTORES | ? | ? | ? | ? | ? |

---

## Grading Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Completeness** | 30 | All 3 variables analyzed with all 5 steps |
| **Correctness** | 25 | Calculations are correct and verified |
| **Visualization** | 20 | Histograms and boxplots are properly labeled |
| **Interpretation** | 15 | Each variable has a meaningful interpretation |
| **Summary table** | 10 | Final summary table is complete and accurate |
| **Total** | 100 | |

---

## Tips for Success

1. **Handle missing values first**
   - Use `df[var].dropna()` when calculating statistics
   - Document how many values are missing

2. **Label your plots**
   - Include axis labels and titles
   - Add legend for mean/median lines

3. **Interpret, don't just calculate**
   - Numbers alone are not enough
   - What does each finding mean in context?

4. **Compare variables**
   - Are there similarities in their distributions?
   - What might explain the patterns you see?

5. **Document your decisions**
   - Explain why you chose median over mean (if applicable)
   - Justify your outlier conclusions

---

## Submission

- **File name:** `workshop_completed.ipynb`
- **Location:** Submit through the LMS
- **Deadline:** Before Week 6 class

---

## Resources

- **Dataset source:** [datos.gov.co - HISTORICO_CONSUMO](https://www.datos.gov.co/dataset/HISTORICO-CONSUMO/wcpc-hgdr)
- **pandas documentation:** https://pandas.pydata.org/docs/
- **matplotlib documentation:** https://matplotlib.org/stable/contents.html

---

*Week 5 - Data Analytics Course*
