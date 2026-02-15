# Week 10 Workshop: Birth Records Dashboard in Power BI

## Power BI Essentials - Complete Dashboard Project

**Duration:** 2 hours (homework or in-class workshop)

**Dataset:** Nacidos Vivos (Birth Records) from datos.gov.co

**Source:** [https://www.datos.gov.co/en/Salud-y-Protecci-n-Social/nacimientos/26g4-ekt3](https://www.datos.gov.co/en/Salud-y-Protecci-n-Social/nacimientos/26g4-ekt3)

---

## Objectives

By completing this workshop, you will:

1. Import and clean data using Power Query
2. Create 5 different visualization types
3. Write 3 DAX measures for key metrics
4. Add interactive slicers for filtering
5. Design a clean, professional dashboard layout

---

## Workshop Overview

```
+----------------------------------------------------------+
|  BIRTH RECORDS DASHBOARD                                  |
|  Colombia - Nacidos Vivos Analysis                        |
+----------------------------------------------------------+
|                                                           |
|  [Year Slicer]  [Gender Slicer]  [Area Slicer]           |
|                                                           |
|  +-------------+  +-------------+  +-------------+        |
|  | CARD        |  | CARD        |  | CARD        |        |
|  | Total Births|  | Avg Weight  |  | Low Weight %|        |
|  +-------------+  +-------------+  +-------------+        |
|                                                           |
|  +---------------------------+  +---------------------+   |
|  | BAR CHART                 |  | LINE CHART          |   |
|  | Births by Department      |  | Births Over Time    |   |
|  +---------------------------+  +---------------------+   |
|                                                           |
|  +---------------------------+  +---------------------+   |
|  | MAP                       |  | TABLE               |   |
|  | Geographic Distribution   |  | Detailed Records    |   |
|  +---------------------------+  +---------------------+   |
|                                                           |
+----------------------------------------------------------+
```

---

## Part 1: Data Import and Cleaning (30 minutes)

### Task 1.1: Download the Dataset

1. Go to [datos.gov.co](https://www.datos.gov.co/)
2. Search for "nacidos vivos" or "nacimientos"
3. Download the dataset as CSV
4. Note the file location

Alternative: Use the direct link provided by your instructor.

---

### Task 1.2: Import Data into Power BI

1. Open **Power BI Desktop**
2. Click **Home** > **Get Data** > **Text/CSV**
3. Select your downloaded file
4. In the preview window, verify:
   - Column headers are detected correctly
   - Data types look reasonable
5. Click **Transform Data** (not Load) to open Power Query

---

### Task 1.3: Clean Data in Power Query

Perform these cleaning operations:

#### 1. Rename Columns for Clarity

Right-click column headers and rename:

| Original | New Name |
|----------|----------|
| PESO | Birth_Weight_Grams |
| SEXO | Gender |
| ANO | Year |
| MES | Month |
| DEPARTAMENTO | Department |
| MUNICIPIO | Municipality |
| AREA | Area_Type |

#### 2. Transform Gender Values

1. Select the Gender column
2. Go to **Transform** > **Replace Values**
3. Replace:
   - `1` with `Male`
   - `2` with `Female`

#### 3. Transform Area Values

1. Select the Area_Type column
2. Replace:
   - `1` with `Urban`
   - `2` with `Rural`
   - `3` with `Unknown`

#### 4. Remove Invalid Records

1. Filter out rows where Birth_Weight_Grams = 0 or is null
2. Filter out rows where Gender is null
3. Click on column header > **Remove Empty**

#### 5. Check Data Types

Ensure:
- Birth_Weight_Grams = Whole Number
- Year = Whole Number
- Month = Whole Number
- Text columns = Text

#### 6. Close and Apply

Click **Home** > **Close & Apply**

---

## Part 2: Create 5 Visualizations (45 minutes)

### Visualization 1: Card - Total Births

1. Click blank area on canvas
2. Select **Card** from Visualizations pane
3. Drag `Birth_Weight_Grams` to Values
4. Change aggregation: Click dropdown > **Count**
5. Format the card:
   - Display units: Auto
   - Add title: "Total Births"
   - Increase font size

**Expected:** A single number showing total birth count.

---

### Visualization 2: Clustered Bar Chart - Births by Department

1. Click blank area
2. Select **Clustered Bar Chart**
3. Configure:
   - **Y-axis:** Department
   - **X-axis:** Birth_Weight_Grams (Count)
4. Sort: Click chart > More options (...) > Sort descending
5. Show only Top 10:
   - In Filters pane, add Department
   - Select "Top N" filter type
   - Show Top 10 by Count of Birth_Weight_Grams

**Expected:** Horizontal bars showing top 10 departments by birth count.

---

### Visualization 3: Line Chart - Births Over Time

1. Click blank area
2. Select **Line Chart**
3. Configure:
   - **X-axis:** Year
   - **Y-axis:** Birth_Weight_Grams (Count)
4. Optional: Add Month for monthly detail
   - Drill down hierarchy: Year > Month

**Expected:** Line showing trend of births over years.

---

### Visualization 4: Filled Map - Geographic Distribution

1. Click blank area
2. Select **Filled Map**
3. Configure:
   - **Location:** Department
   - **Legend:** Leave empty
   - **Tooltips:** Count of Birth_Weight_Grams
4. In Format pane:
   - Set map style to Grayscale
   - Adjust colors for data values

**Note:** If map does not recognize Colombian departments, you may need to:
- Add "Colombia" to department names
- Or use a custom TopoJSON file

**Alternative:** Use **Shape Map** if Filled Map does not work.

**Expected:** Map of Colombia colored by birth density.

---

### Visualization 5: Table - Detailed Records

1. Click blank area
2. Select **Table**
3. Add columns:
   - Department
   - Gender
   - Area_Type
   - Count of records
   - Average Birth_Weight_Grams
4. Enable totals row:
   - Format > Totals > On

**Expected:** A sortable table with aggregated data.

---

## Part 3: Create 3 DAX Measures (20 minutes)

### Measure 1: Average Birth Weight

1. Right-click table in Fields pane
2. Select **New Measure**
3. Enter:

```dax
Avg Birth Weight =
AVERAGE('nacidos_vivos'[Birth_Weight_Grams])
```

4. Format: Whole Number with "g" suffix

---

### Measure 2: Low Birth Weight Percentage

Low birth weight is defined as less than 2500 grams.

```dax
Low Weight Percentage =
VAR TotalBirths = COUNT('nacidos_vivos'[Birth_Weight_Grams])
VAR LowWeightBirths =
    CALCULATE(
        COUNT('nacidos_vivos'[Birth_Weight_Grams]),
        'nacidos_vivos'[Birth_Weight_Grams] < 2500
    )
RETURN
    DIVIDE(LowWeightBirths, TotalBirths, 0) * 100
```

Format: Number with 1 decimal, add "%" suffix

---

### Measure 3: Year-over-Year Change

```dax
YoY Birth Change =
VAR CurrentYear = SUM('nacidos_vivos'[Year])
VAR CurrentBirths = COUNT('nacidos_vivos'[Birth_Weight_Grams])
VAR PreviousYearBirths =
    CALCULATE(
        COUNT('nacidos_vivos'[Birth_Weight_Grams]),
        PREVIOUSYEAR('nacidos_vivos'[Date])
    )
RETURN
    DIVIDE(CurrentBirths - PreviousYearBirths, PreviousYearBirths, 0) * 100
```

**Note:** This measure requires a Date column. If your data only has Year/Month:

Alternative simpler version:
```dax
Births This Year =
CALCULATE(
    COUNT('nacidos_vivos'[Birth_Weight_Grams]),
    'nacidos_vivos'[Year] = MAX('nacidos_vivos'[Year])
)
```

---

### Add Measures to Dashboard

1. Create 3 Card visuals
2. Add one measure to each card
3. Position them at the top of the dashboard

---

## Part 4: Add Slicers (15 minutes)

### Slicer 1: Year

1. Click blank area
2. Select **Slicer** visualization
3. Drag `Year` to the slicer
4. Format options:
   - Style: Dropdown or List
   - Single select or Multi-select

---

### Slicer 2: Gender

1. Add another Slicer
2. Drag `Gender` to the slicer
3. Format:
   - Style: Buttons (horizontal)
   - Add "All" option

---

### Slicer 3: Area Type

1. Add another Slicer
2. Drag `Area_Type` to the slicer
3. Format:
   - Style: Dropdown
   - Allow multiple selections

---

### Sync Slicers (Optional but Recommended)

1. Go to **View** > **Sync Slicers**
2. Ensure all slicers affect all visuals on the page

---

## Part 5: Dashboard Design (10 minutes)

### Layout Guidelines

1. **Align visuals:** Use gridlines (View > Gridlines)
2. **Consistent sizing:** Group similar visuals together
3. **Visual hierarchy:**
   - KPIs (cards) at top
   - Main charts in middle
   - Details (table) at bottom

### Color Scheme

Use a consistent color palette:

| Element | Color Suggestion |
|---------|------------------|
| Male | Blue (#4A90D9) |
| Female | Pink (#E84393) |
| Urban | Gray (#636E72) |
| Rural | Green (#00B894) |
| Accent | Purple (#6C5CE7) |

### Add Title

1. Insert > Text Box
2. Add dashboard title: "Colombia Birth Records Analysis"
3. Add subtitle with data source and date range

---

## Deliverables

Your completed workshop should include:

### Power BI File (.pbix)

1. **Data Model:**
   - Cleaned and transformed data
   - Proper column names and data types

2. **Measures (3 total):**
   - Avg Birth Weight
   - Low Weight Percentage
   - Births count or YoY metric

3. **Visualizations (5 total):**
   - Card (Total Births)
   - Clustered Bar Chart (by Department)
   - Line Chart (over time)
   - Map (geographic)
   - Table (detailed)

4. **Slicers (3 total):**
   - Year
   - Gender
   - Area Type

5. **Professional Layout:**
   - Aligned visuals
   - Consistent colors
   - Clear titles

---

## Grading Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| Data Cleaning | 15 | Proper transformations in Power Query |
| Visualizations | 30 | All 5 charts created correctly |
| DAX Measures | 25 | All 3 measures work correctly |
| Slicers | 15 | Interactive filtering works |
| Design | 15 | Professional appearance and layout |
| **Total** | **100** | |

---

## Tips for Success

### Power Query Tips

- Use **Applied Steps** to track your transformations
- You can always go back and modify steps
- Name your steps descriptively

### DAX Tips

- Test measures in a Card visual first
- Use **DAX Formatter** (daxformatter.com) to format complex formulas
- Start simple, then add complexity

### Design Tips

- Less is more - do not overcrowd the dashboard
- Every visual should answer a specific question
- Test interactivity - click on charts to see cross-filtering

---

## Common Issues and Solutions

### Issue: Map Shows Wrong Location

**Solution:** Add country context
- Rename "Bogota" to "Bogota, Colombia"
- Or use Data Categories: Set column to State/Province

### Issue: Slicers Do Not Filter Charts

**Solution:** Check relationships
- Go to Model View
- Ensure tables are related
- Check if filters are set to "All Pages"

### Issue: DAX Returns Blank

**Solution:** Check for nulls
- Use `DIVIDE()` instead of `/` to handle division by zero
- Wrap calculations in `IF(ISBLANK(...), 0, ...)`

---

## Extension Challenges

If you finish early, try these:

1. **Add a Gauge:** Show % of births meeting healthy weight threshold
2. **Create a Drill-through:** Click on department to see municipality details
3. **Add Bookmarks:** Create different views (Overview, Regional, Trends)
4. **Mobile Layout:** Design a phone-friendly version

---

## Submission

Submit your completed .pbix file via the course platform.

Name your file: `Week9_Workshop_[YourName].pbix`

Include a screenshot of your final dashboard as backup.

---

## Resources

- [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
- [DAX Guide](https://dax.guide/)
- [Power Query Documentation](https://docs.microsoft.com/en-us/power-query/)
- [datos.gov.co](https://www.datos.gov.co/)

---

*Power BI transforms data into insights. Your dashboard tells the story of thousands of Colombian births.*
