# Week 5 Workshop: Univariate Analysis

## Overview

| Field | Value |
|-------|-------|
| **Topic** | EDA Part 1 - Univariate Analysis |
| **Dataset** | Evaluaciones Agropecuarias (EVA) |
| **Duration** | 60-90 minutes |
| **Deliverable** | Completed notebook with analysis of 3 variables |

---

## Objective

Apply the **5-step univariate analysis framework** to three different variables from the agricultural evaluations dataset. Document your findings and determine the appropriate statistics for each variable based on its distribution.

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

### Variable 1: producci_n_t
- **Description:** Agricultural production in tons
- **Expected finding:** Right-skewed distribution (few high-production crops dominate)
- **Story to investigate:** Which crops or regions produce the most?

### Variable 2: rea_sembrada_ha
- **Description:** Area planted in hectares
- **Expected finding:** Right-skewed (few large-area operations, many small farms)
- **Story to investigate:** Does more land always mean more production?

### Variable 3: rendimiento_t_ha
- **Description:** Yield in tons per hectare (production / area)
- **Expected finding:** Less skewed than raw production (ratio variable normalizes for farm size)
- **Story to investigate:** Which crops are the most efficient per hectare?

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
| 1 | grupo_de_cultivo (crop group) | producci_n_t | .mean() |
| 2 | ciclo_de_cultivo (crop cycle) | rendimiento_t_ha | .median() |
| 3 | departamento | producci_n_t | .count() and .sum() |

**Pattern:** `df.groupby('GROUP')['VALUE'].operation()`

---

## Summary Table

At the end of your notebook, create a summary table like this:

| Variable | Mean | Median | Distribution | Outliers (%) | Best Measure |
|----------|------|--------|--------------|--------------|--------------|
| producci_n_t | ? | ? | ? | ? | ? |
| rea_sembrada_ha | ? | ? | ? | ? | ? |
| rendimiento_t_ha | ? | ? | ? | ? | ? |

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
   - What does each finding mean in the context of Colombian agriculture?

4. **Compare variables**
   - Are there similarities in their distributions?
   - Why might yield behave differently from raw production?

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

- **Dataset source:** [datos.gov.co - Evaluaciones Agropecuarias](https://www.datos.gov.co/resource/2pnw-mmge)
- **pandas documentation:** https://pandas.pydata.org/docs/
- **matplotlib documentation:** https://matplotlib.org/stable/contents.html

---

*Week 5 - Data Analytics Course*
