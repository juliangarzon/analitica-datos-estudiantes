# Week 10 In-Class Exercise: DAX Measures for Birth Weight Analysis

## Power BI Essentials - Calculated Measures Practice

**Duration:** 30 minutes

**Dataset:** Nacidos Vivos (Birth Records) from datos.gov.co

**Source:** [https://www.datos.gov.co/en/Salud-y-Protecci-n-Social/nacimientos/26g4-ekt3](https://www.datos.gov.co/en/Salud-y-Protecci-n-Social/nacimientos/26g4-ekt3)

---

## Objectives

By completing this exercise, you will:

1. Create your first DAX calculated measure
2. Use the CALCULATE function with filters
3. Compare average birth weight by gender
4. Understand the difference between measures and calculated columns

---

## Prerequisites

Before starting, ensure you have:

- [ ] Power BI Desktop installed
- [ ] Birth Records dataset loaded (CSV or direct connection)
- [ ] Data model visible in Model View

---

## Exercise: Average Birth Weight by Gender

### Context

You have been asked to analyze birth weight patterns in Colombian birth records. The health department wants to know if there are differences in average birth weight between male and female newborns.

### Key Fields in the Dataset

| Field Name | Description | Example Values |
|------------|-------------|----------------|
| PESO | Birth weight in grams | 2500, 3200, 3800 |
| SEXO | Gender of newborn | 1 = Male, 2 = Female |
| ANO | Year of birth | 2016, 2017, 2018 |
| DEPARTAMENTO | Department (state) | Antioquia, Bogota |

---

## Step-by-Step Instructions

### Step 1: Open Power BI Desktop and Load Data

1. Open Power BI Desktop
2. Click **Home** > **Get Data** > **Text/CSV**
3. Navigate to your nacidos_vivos.csv file
4. Click **Load** (or Transform Data if you need to clean first)

---

### Step 2: Create Your First Measure - Overall Average

1. In the **Fields** pane (right side), right-click on your table name
2. Select **New Measure**
3. In the formula bar, type:

```dax
Average Birth Weight =
AVERAGE('nacidos_vivos'[PESO])
```

4. Press **Enter**
5. Format the measure: In **Measure Tools** > **Format** > Select "Whole Number"

**Expected Result:** You should see a new measure icon (calculator symbol) appear under your table.

---

### Step 3: Create Measure for Male Average

1. Right-click on your table > **New Measure**
2. Type the following DAX formula:

```dax
Avg Weight Male =
CALCULATE(
    AVERAGE('nacidos_vivos'[PESO]),
    'nacidos_vivos'[SEXO] = 1
)
```

3. Press **Enter**

**What this does:**
- `CALCULATE()` - Modifies the filter context
- `AVERAGE('nacidos_vivos'[PESO])` - The base calculation
- `'nacidos_vivos'[SEXO] = 1` - The filter condition (1 = Male)

---

### Step 4: Create Measure for Female Average

1. Right-click on your table > **New Measure**
2. Type the following DAX formula:

```dax
Avg Weight Female =
CALCULATE(
    AVERAGE('nacidos_vivos'[PESO]),
    'nacidos_vivos'[SEXO] = 2
)
```

3. Press **Enter**

---

### Step 5: Create a Comparison Visual

1. Click on a blank area of your report canvas
2. From **Visualizations** pane, select **Clustered Bar Chart**
3. Add the following to the visual:
   - **Y-axis:** Leave empty (we want totals)
   - **X-axis:** Drag both measures:
     - `Avg Weight Male`
     - `Avg Weight Female`

4. Alternatively, create a **Card** visual for each measure:
   - Select **Card** visualization
   - Drag `Avg Weight Male` to the Values field
   - Repeat for `Avg Weight Female`

---

### Step 6: Create the Difference Measure (Bonus)

1. Create a new measure to calculate the difference:

```dax
Weight Difference (M-F) =
[Avg Weight Male] - [Avg Weight Female]
```

2. Add this measure to a Card visual

**Expected Result:** You should see a positive or negative number indicating the difference in grams.

---

## Expected Results

After completing all steps, your report should show:

```
+----------------------------------+
|  Average Birth Weight (All)     |
|  ~3,100 grams                   |
+----------------------------------+

+----------------------------------+
|  Male Average    | Female Average|
|  ~3,150 grams    | ~3,050 grams  |
+----------------------------------+

+----------------------------------+
|  Difference (M-F)               |
|  ~100 grams                     |
+----------------------------------+
```

Note: Actual values will depend on your dataset. The pattern typically shows males slightly heavier than females.

---

## Verification Checklist

Before finishing, verify:

- [ ] You have 4 measures created (visible with calculator icon)
- [ ] Each measure shows a value when added to a Card visual
- [ ] The difference measure equals Male minus Female
- [ ] Values are formatted as whole numbers (no decimals)

---

## Common Errors and Solutions

### Error 1: "Cannot find column PESO"

**Cause:** Column name mismatch

**Solution:** Check exact column names in your data. Names are case-sensitive in DAX. Use the format: `'TableName'[ColumnName]`

---

### Error 2: Measure shows blank

**Cause:** Filter eliminates all rows

**Solution:**
- Check if SEXO values are 1/2 or "M"/"F"
- Adjust your filter accordingly:

```dax
-- If SEXO contains text values:
Avg Weight Male =
CALCULATE(
    AVERAGE('nacidos_vivos'[PESO]),
    'nacidos_vivos'[SEXO] = "Masculino"
)
```

---

### Error 3: "Circular dependency detected"

**Cause:** Measure references itself incorrectly

**Solution:** Ensure measure names do not match column names. Use descriptive names like "Avg Weight Male" not just "PESO".

---

## Understanding DAX: Key Concepts

### Measure vs Calculated Column

| Aspect | Measure | Calculated Column |
|--------|---------|-------------------|
| When calculated | At query time | When data loads |
| Storage | Not stored | Stored in model |
| Context | Responds to filters | Row-by-row |
| Use for | Aggregations, KPIs | Categorization, grouping |

### The CALCULATE Function

```
CALCULATE( <expression>, <filter1>, <filter2>, ... )
```

- First argument: What to calculate
- Remaining arguments: Filters to apply
- Filters are combined with AND logic

---

## Reflection Questions

Answer these in your notebook or discuss with a partner:

1. Why do we use a measure instead of a calculated column for averages?

2. What would happen if you added a Department slicer to your report? Would the measures recalculate?

3. How would you modify the formula to show average weight only for births in 2018?

---

## Extension Challenge (If Time Permits)

Create measures for:

1. **Count of Births by Gender**
```dax
Count Male =
CALCULATE(
    COUNT('nacidos_vivos'[PESO]),
    'nacidos_vivos'[SEXO] = 1
)
```

2. **Low Birth Weight Percentage** (under 2500g)
```dax
Low Weight Pct =
DIVIDE(
    CALCULATE(
        COUNT('nacidos_vivos'[PESO]),
        'nacidos_vivos'[PESO] < 2500
    ),
    COUNT('nacidos_vivos'[PESO])
) * 100
```

---

## Submission

This is an in-class exercise. Show your instructor:

1. The 4 measures you created
2. A simple visual comparing male vs female averages
3. Your answer to at least one reflection question

---

## Resources

- [DAX Guide - CALCULATE](https://dax.guide/calculate/)
- [DAX Guide - AVERAGE](https://dax.guide/average/)
- [Microsoft Learn - DAX Basics](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-quickstart-learn-dax-basics)

---

*Power BI is not just a visualization tool - it is a complete analytics platform. DAX is the language that unlocks its full potential.*
