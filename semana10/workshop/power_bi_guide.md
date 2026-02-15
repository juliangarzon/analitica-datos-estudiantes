# Power BI Step-by-Step Guide

## Complete Reference for Birth Records Dashboard

This guide provides detailed instructions with expected outcomes for every step of the Power BI workshop.

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Power Query: Data Import and Cleaning](#2-power-query-data-import-and-cleaning)
3. [DAX Formulas Reference](#3-dax-formulas-reference)
4. [Creating Visualizations](#4-creating-visualizations)
5. [Adding Interactivity](#5-adding-interactivity)
6. [Design Best Practices](#6-design-best-practices)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Getting Started

### 1.1 Power BI Desktop Installation

If you have not installed Power BI Desktop:

1. Go to [Microsoft Power BI Download](https://powerbi.microsoft.com/desktop/)
2. Click "Download free"
3. Run the installer
4. Sign in with your Microsoft account (optional for desktop use)

**Expected:** Power BI Desktop opens with a blank canvas.

### 1.2 Power BI Interface Overview

```
+----------------------------------------------------------+
|  RIBBON (Home, Insert, Modeling, View, Help)              |
+----------------------------------------------------------+
|                                   |                       |
|                                   |  VISUALIZATIONS       |
|      CANVAS                       |  (chart types)        |
|      (where you build)            |                       |
|                                   |  FIELDS               |
|                                   |  (your data)          |
|                                   |                       |
+----------------------------------------------------------+
|  VIEWS: Report | Data | Model                             |
+----------------------------------------------------------+
```

### 1.3 The Three Views

| View | Purpose | When to Use |
|------|---------|-------------|
| Report | Build visualizations | Creating dashboard |
| Data | See raw data | Verify transformations |
| Model | Manage relationships | Multiple tables |

---

## 2. Power Query: Data Import and Cleaning

### 2.1 Opening Power Query

**Path:** Home > Transform Data

**Expected:** Power Query Editor window opens.

### 2.2 Power Query Interface

```
+----------------------------------------------------------+
|  RIBBON (Home, Transform, Add Column, View)               |
+----------------------------------------------------------+
|  QUERIES    |          DATA PREVIEW           | APPLIED   |
|  (tables)   |                                 | STEPS     |
|             |                                 |           |
+----------------------------------------------------------+
```

### 2.3 Step-by-Step Data Cleaning

#### Step 1: Rename the Query

1. In Queries pane, right-click your query
2. Select "Rename"
3. Type: `nacidos_vivos`
4. Press Enter

**Expected:** Query name changes in the left pane.

---

#### Step 2: Promote Headers (if needed)

If your first row contains headers but they are not recognized:

1. Click **Home** > **Use First Row as Headers**

**Expected:** Column headers change from "Column1, Column2..." to actual names.

---

#### Step 3: Rename Columns

For each column you want to rename:

1. Double-click the column header
2. Type the new name
3. Press Enter

**Rename these columns:**

```
PESO            -> Birth_Weight_Grams
SEXO            -> Gender_Code
ANO             -> Year
MES             -> Month
DEPARTAMENTO    -> Department
MUNICIPIO       -> Municipality
AREA            -> Area_Code
```

**Applied Steps:** You will see "Renamed Columns" appear.

---

#### Step 4: Change Data Types

1. Click the icon to the left of each column header (shows current type)
2. Select the correct type:

| Column | Type |
|--------|------|
| Birth_Weight_Grams | Whole Number |
| Gender_Code | Whole Number |
| Year | Whole Number |
| Month | Whole Number |
| Department | Text |
| Municipality | Text |
| Area_Code | Whole Number |

**Expected:** Type icons change (123 for numbers, ABC for text).

---

#### Step 5: Add Conditional Columns for Labels

**Add Gender Label:**

1. Click **Add Column** > **Conditional Column**
2. Configure:
   - New column name: `Gender`
   - If `Gender_Code` equals `1` then `Male`
   - Else if `Gender_Code` equals `2` then `Female`
   - Else `Unknown`
3. Click OK

**Expected:** New column "Gender" appears with text values.

---

**Add Area Label:**

1. Click **Add Column** > **Conditional Column**
2. Configure:
   - New column name: `Area_Type`
   - If `Area_Code` equals `1` then `Urban`
   - Else if `Area_Code` equals `2` then `Rural`
   - Else `Unknown`
3. Click OK

**Expected:** New column "Area_Type" appears with text values.

---

#### Step 6: Filter Out Invalid Data

**Remove Zero Weights:**

1. Click dropdown arrow on `Birth_Weight_Grams` column
2. Select "Number Filters" > "Greater Than"
3. Enter: `0`
4. Click OK

**Expected:** Row count decreases. Check the status bar at bottom.

---

**Remove Null Values:**

1. Click dropdown on `Gender` column
2. Uncheck "(null)" and "(blank)" if present
3. Click OK

**Expected:** Only valid records remain.

---

#### Step 7: Remove Unnecessary Columns

1. Select columns you do not need (hold Ctrl to select multiple)
2. Right-click > **Remove Columns**

Keep only:
- Birth_Weight_Grams
- Gender
- Year
- Month
- Department
- Municipality
- Area_Type

**Expected:** Only essential columns remain.

---

#### Step 8: Close and Apply

1. Click **Home** > **Close & Apply**
2. Wait for data to load

**Expected:** Power Query closes, data appears in Fields pane.

---

## 3. DAX Formulas Reference

### 3.1 Creating a Measure

1. In Fields pane, right-click your table name
2. Select **New Measure**
3. Type your formula in the formula bar
4. Press Enter

**Expected:** Measure appears with calculator icon.

---

### 3.2 All DAX Measures for This Workshop

#### Measure 1: Total Births

```dax
Total Births =
COUNT('nacidos_vivos'[Birth_Weight_Grams])
```

**Purpose:** Counts all birth records.

**Expected Result:** A whole number (e.g., 150,000).

**Format:** Whole Number, use thousand separator.

---

#### Measure 2: Average Birth Weight

```dax
Avg Birth Weight =
AVERAGE('nacidos_vivos'[Birth_Weight_Grams])
```

**Purpose:** Calculates mean birth weight.

**Expected Result:** Around 3,000-3,200 grams.

**Format:** Whole Number with "g" suffix.

To add suffix:
1. Select measure in Fields pane
2. In Measure Tools > Format > Format: Custom
3. Enter: `#,##0 "g"`

---

#### Measure 3: Low Birth Weight Percentage

```dax
Low Weight Pct =
VAR TotalBirths = COUNT('nacidos_vivos'[Birth_Weight_Grams])
VAR LowWeightBirths =
    CALCULATE(
        COUNT('nacidos_vivos'[Birth_Weight_Grams]),
        'nacidos_vivos'[Birth_Weight_Grams] < 2500
    )
RETURN
    DIVIDE(LowWeightBirths, TotalBirths, 0) * 100
```

**Purpose:** Percentage of births under 2500g (WHO low birth weight threshold).

**Expected Result:** Typically 5-15%.

**Format:** Number with 1 decimal, add "%" suffix.

---

#### Measure 4: Average Weight - Male

```dax
Avg Weight Male =
CALCULATE(
    AVERAGE('nacidos_vivos'[Birth_Weight_Grams]),
    'nacidos_vivos'[Gender] = "Male"
)
```

**Purpose:** Average weight for male births only.

**Expected Result:** Slightly higher than overall average.

---

#### Measure 5: Average Weight - Female

```dax
Avg Weight Female =
CALCULATE(
    AVERAGE('nacidos_vivos'[Birth_Weight_Grams]),
    'nacidos_vivos'[Gender] = "Female"
)
```

**Purpose:** Average weight for female births only.

**Expected Result:** Slightly lower than overall average.

---

#### Measure 6: Weight Difference by Gender

```dax
Weight Diff (M-F) =
[Avg Weight Male] - [Avg Weight Female]
```

**Purpose:** Difference in grams between male and female averages.

**Expected Result:** Positive number (males typically heavier).

---

#### Measure 7: Urban Birth Percentage

```dax
Urban Pct =
VAR TotalBirths = COUNT('nacidos_vivos'[Birth_Weight_Grams])
VAR UrbanBirths =
    CALCULATE(
        COUNT('nacidos_vivos'[Birth_Weight_Grams]),
        'nacidos_vivos'[Area_Type] = "Urban"
    )
RETURN
    DIVIDE(UrbanBirths, TotalBirths, 0) * 100
```

**Purpose:** Percentage of births in urban areas.

**Expected Result:** Typically 70-80% in Colombia.

---

### 3.3 DAX Best Practices

| Do | Do Not |
|----|--------|
| Use DIVIDE() for division | Use / operator directly |
| Format measures clearly | Leave default formatting |
| Use VAR for readability | Nest everything in one line |
| Test in a Card first | Add to complex visual immediately |

---

## 4. Creating Visualizations

### 4.1 Card Visual

**Purpose:** Display a single KPI prominently.

**Steps:**

1. Click blank canvas area
2. Select Card from Visualizations
3. Drag measure to "Fields" area
4. Format:
   - Data label: Font size 40+
   - Category label: On (shows measure name)
   - Background: Optional color

**Expected Outcome:**

```
+-------------------+
|    150,000        |
|   Total Births    |
+-------------------+
```

---

### 4.2 Clustered Bar Chart

**Purpose:** Compare categories (e.g., departments).

**Steps:**

1. Select Clustered Bar Chart
2. Configure:
   - Y-axis: Department
   - X-axis: Total Births (or drag measure)
3. Filter to Top 10:
   - In Filters pane > Add Department
   - Filter type: Top N
   - Show items: Top 10
   - By value: Total Births

**Expected Outcome:**

```
Antioquia      |==================|
Bogota         |================|
Valle          |============|
...
```

---

### 4.3 Line Chart

**Purpose:** Show trends over time.

**Steps:**

1. Select Line Chart
2. Configure:
   - X-axis: Year
   - Y-axis: Total Births (measure)
3. Optional: Add Month for drill-down

**Expected Outcome:**

```
    ^
    |      /\
    |    /    \
    |  /        \
    +--------------->
     2015 2016 2017
```

---

### 4.4 Filled Map

**Purpose:** Geographic visualization.

**Steps:**

1. Select Filled Map
2. Configure:
   - Location: Department
   - Color saturation: Total Births
3. Format:
   - Map style: Grayscale or Road
   - Data colors: Diverging scale

**Note on Colombian Departments:**

If departments are not recognized, try:

1. Go to Data view
2. Select Department column
3. In Column Tools > Data Category > State or Province

**Expected Outcome:** Map of Colombia with departments shaded by birth count.

---

### 4.5 Table Visual

**Purpose:** Show detailed, sortable data.

**Steps:**

1. Select Table
2. Add columns:
   - Department
   - Total Births
   - Avg Birth Weight
   - Low Weight Pct
3. Enable totals:
   - Format > Totals: On

**Expected Outcome:**

```
| Department | Births | Avg Weight | Low % |
|------------|--------|------------|-------|
| Antioquia  | 50,000 | 3,150g     | 7.2%  |
| Bogota     | 45,000 | 3,180g     | 6.8%  |
| ...        | ...    | ...        | ...   |
| TOTAL      | 150,000| 3,120g     | 8.1%  |
```

---

## 5. Adding Interactivity

### 5.1 Creating Slicers

**Slicer for Year:**

1. Select Slicer visualization
2. Drag Year to Values
3. Format:
   - Orientation: Horizontal
   - Selection: Single or Multi
   - Show "Select All": On

**Slicer for Gender:**

1. Add new Slicer
2. Drag Gender to Values
3. Format:
   - Style: Buttons
   - Orientation: Horizontal

**Slicer for Area:**

1. Add new Slicer
2. Drag Area_Type to Values
3. Format:
   - Style: Dropdown

---

### 5.2 Cross-Filtering Behavior

By default, clicking on a visual filters other visuals.

To test:
1. Click on a bar in the bar chart
2. Observe other visuals update

To change behavior:
1. Select a visual
2. Format > Edit interactions
3. Choose: Filter, Highlight, or None

---

### 5.3 Drill-Through Pages (Advanced)

Create a detail page:

1. Add new page (bottom of canvas)
2. Name it "Department Details"
3. Add visuals for detailed analysis
4. Add Department to Drill-through field
5. Test: Right-click department in main page > Drill through

---

## 6. Design Best Practices

### 6.1 Layout Grid

Use alignment guides:

1. View > Gridlines: On
2. View > Snap to Grid: On

**Recommended Layout:**

```
+----------------------------------------------------------+
|  TITLE                                    [Year Slicer]   |
+----------------------------------------------------------+
|  [Card 1]    [Card 2]    [Card 3]    [Gender] [Area]     |
+----------------------------------------------------------+
|                            |                              |
|   BAR CHART                |      LINE CHART              |
|   (60% width)              |      (40% width)             |
|                            |                              |
+----------------------------------------------------------+
|                            |                              |
|   MAP                      |      TABLE                   |
|   (50% width)              |      (50% width)             |
|                            |                              |
+----------------------------------------------------------+
```

---

### 6.2 Color Guidelines

**Primary Colors:**

| Purpose | Hex Code | Use For |
|---------|----------|---------|
| Primary | #667EEA | Headers, titles |
| Male | #4A90D9 | Gender = Male |
| Female | #E84393 | Gender = Female |
| Urban | #636E72 | Area = Urban |
| Rural | #00B894 | Area = Rural |
| Alert | #E17055 | Low birth weight |

**To apply colors:**

1. Select visual
2. Format > Data colors
3. Choose color for each series

---

### 6.3 Typography

- **Titles:** Bold, 14-16pt
- **Data labels:** Regular, 10-12pt
- **Card values:** Bold, 32-40pt
- **Font family:** Segoe UI (default) or DIN

---

### 6.4 Removing Clutter

Remove unnecessary elements:

1. Turn off axis titles if obvious
2. Remove gridlines for cleaner look
3. Reduce decimal places
4. Use abbreviations (K, M) for large numbers

---

## 7. Troubleshooting

### 7.1 Common Errors

#### Error: "Cannot find column"

**Cause:** Column name mismatch in DAX.

**Solution:**
1. Check exact column name in Fields pane
2. DAX is case-sensitive
3. Use format: `'TableName'[ColumnName]`

---

#### Error: "Circular dependency"

**Cause:** Measure references itself.

**Solution:**
1. Check measure names
2. Ensure measure name differs from column names
3. Review referenced measures for loops

---

#### Error: Measure returns BLANK

**Cause:** Filter context eliminates all rows.

**Solution:**
1. Check slicer selections
2. Verify filter conditions match actual data values
3. Test measure without slicers first

---

### 7.2 Performance Tips

1. **Reduce rows in Power Query** before loading
2. **Remove unused columns** to decrease model size
3. **Avoid calculated columns** when measures work
4. **Use variables (VAR)** in complex measures

---

### 7.3 Saving and Sharing

**Save locally:**
- File > Save As
- Choose location
- File type: .pbix

**Publish to web (requires Pro license):**
- Home > Publish
- Select workspace
- Access via powerbi.com

---

## Quick Reference Card

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Copy visual | Ctrl+C |
| Paste visual | Ctrl+V |
| Undo | Ctrl+Z |
| Redo | Ctrl+Y |
| Delete | Delete |
| Select all | Ctrl+A |
| Save | Ctrl+S |

### Essential DAX Functions

| Function | Purpose | Example |
|----------|---------|---------|
| COUNT | Count rows | `COUNT(Table[Column])` |
| AVERAGE | Mean value | `AVERAGE(Table[Column])` |
| SUM | Total | `SUM(Table[Column])` |
| CALCULATE | Filter context | `CALCULATE(SUM(...), Filter)` |
| DIVIDE | Safe division | `DIVIDE(num, den, 0)` |
| IF | Conditional | `IF(condition, true, false)` |

---

## Resources

- [Microsoft Learn - Power BI](https://learn.microsoft.com/en-us/power-bi/)
- [DAX Guide](https://dax.guide/)
- [Power BI Community](https://community.powerbi.com/)
- [SQLBI (Advanced DAX)](https://www.sqlbi.com/)

---

*This guide accompanies Week 10 of the Data Analytics course. For questions, contact your instructor.*
