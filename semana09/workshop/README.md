# Week 9 Workshop: Visualization Principles

## Creating Publication-Ready Figures with Budget Execution Data

**Duration:** 2 hours (homework or in-class workshop)

**Dataset:** Budget Execution Data (EJECUCION_PRESUPUESTAL) from datos.gov.co

**Local file in this repository:** `../data/EJECUCION_PRESUPUESTAL.csv`

---

## Objectives

By completing this workshop, you will:

1. Create 5 different chart types with real budget data
2. Answer 5 concrete analytical questions using code
3. Apply a consistent, professional color palette
4. Add proper titles, labels, and annotations
5. Export publication-ready figures in multiple formats

---

## Workshop Tasks

### Part 1: Data Preparation and Color Palette (15 minutes)

**Task 1.1: Load and Explore the Data**

1. Load the budget execution dataset
2. Identify numeric and categorical columns
3. Create summary statistics

**Task 1.2: Define a Professional Color Palette**

Create a consistent color palette that you will use throughout:
- Primary color (main data)
- Secondary color (comparison/secondary data)
- Accent color (highlighting important values)
- Warning color (below-target or negative values)
- Neutral color (reference lines, background elements)

Recommended palettes:
- Corporate blue: `['#2C3E50', '#3498DB', '#1ABC9C', '#E74C3C', '#95A5A6']`
- Muted earth: `['#5D4E37', '#8B7355', '#CD853F', '#B22222', '#A9A9A9']`
- Modern minimal: `['#1A1A2E', '#16213E', '#0F3460', '#E94560', '#EAEAEA']`

---

### Part 2: Create 5 Chart Types (75 minutes)

Each chart must answer a real analytical question from the dataset.

**Chart 1: Horizontal Bar Chart - Which sectors concentrate the most budget? (15 minutes)**

Use the real dataset to aggregate `Apropiación Vigente` by `Nombre Sector`:
- Focus on the top 10 sectors
- Sort values from largest to smallest
- Use a single professional color
- Add value labels at the end of each bar
- Include a title that states the takeaway

**Chart 2: Grouped Bar Chart - Where is the largest gap between appropriation and commitments? (15 minutes)**

Use the real dataset to compare `Apropiación Vigente` vs `Compromisos` by sector:
- Focus on the top 8 sectors by appropriation
- Use two distinct colors
- Add a legend
- Show the execution percentage above each pair
- Help the reader see where the gap is widest

**Chart 3: Scatter Plot - Which entities combine large budgets with low execution? (15 minutes)**

Build a scatter plot with real aggregated data:
- X axis: `Apropiación Vigente`
- Y axis: execution percentage
- Highlight at least 2 interesting outliers
- Add a 90% reference line
- Use point size or color intentionally

**Chart 4: Stacked Bar Chart - How does budget composition differ across sectors? (15 minutes)**

Use `Nombre Nivel Uno Rubro` to compare composition across top sectors:
- Use a sequential color palette
- Add percentage labels when readable
- Include a legend
- Keep the chart readable even if some sectors have similar mixes

**Chart 5: Small Multiples - Which sectors are below the 90% execution target? (15 minutes)**

Create small multiples with one subplot per sector:
- Use the top 8 sectors by appropriation
- Show execution percentage in each subplot
- Add a 90% reference line
- Use warning color only for sectors below target
- Keep scales consistent across subplots

---

### Part 3: Publication-Ready Formatting (20 minutes)

**Task 3.1: Apply Consistent Styling**

For each of your 5 charts, ensure:

- [ ] Title is descriptive and left-aligned
- [ ] Axis labels are clear and have units if applicable
- [ ] Font sizes are consistent across all charts
- [ ] Colors follow your defined palette
- [ ] Legends are positioned appropriately
- [ ] No unnecessary gridlines or borders

**Task 3.2: Add Source Attribution**

Add a footnote to each chart with:
- Data source: "Source: datos.gov.co - Budget Execution Data"
- Date of data (if available)

**Task 3.3: Export Figures**

Export each chart in two formats:
1. PNG at 300 DPI for reports
2. SVG for presentations (vector format)

Use consistent naming:
- `chart1_budget_by_category.png`
- `chart2_approved_vs_executed.png`
- etc.

---

### Part 4: Critical Analysis (10 minutes)

Answer the following questions in your notebook:

1. **Which chart type was most effective** for communicating the most important pattern in the dataset? Why?

2. **What insight would be missed** if you only showed the sectors with the largest budgets?

3. **If you could only show one chart** to a decision-maker, which would you choose and what question would it answer best?

4. **What additional data** or time dimension would make these visualizations more impactful?

---

## Deliverables

Your completed workshop should include:

1. **Completed Jupyter Notebook** with:
   - All code cells executed
   - Clear markdown explanations for each chart
   - Answers to critical analysis questions

2. **Exported Figures** (10 files total):
   - 5 PNG files at 300 DPI
   - 5 SVG files

3. **Color Palette Documentation**:
   - Hex codes for your chosen palette
   - Brief rationale for color choices

---

## Grading Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| Data-Ink Ratio | 20 | Charts are clean, no chartjunk |
| Chart Type Selection | 20 | Appropriate chart for each data type |
| Color Usage | 15 | Purposeful, consistent palette |
| Labels & Titles | 15 | Clear, informative, professional |
| Export Quality | 15 | High-resolution, properly named files |
| Critical Analysis | 15 | Thoughtful answers to questions |
| **Total** | **100** | |

---

## Tips for Success

### Matplotlib Style Tips

```python
# Set a clean style
plt.style.use('seaborn-v0_8-whitegrid')

# Or create custom style
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
```

### Color Best Practices

| Do | Do Not |
|-----|---------|
| Use color to highlight key data | Use rainbow colors |
| Keep palette to 5-7 colors max | Use different color for each bar |
| Use sequential colors for ordered data | Use red-green (colorblind issues) |
| Gray out less important data | Make everything equally prominent |

### Exporting Tips

```python
# High-resolution PNG
plt.savefig('chart.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

# Vector format for editing
plt.savefig('chart.svg', format='svg', bbox_inches='tight')

# PDF for printing
plt.savefig('chart.pdf', format='pdf', bbox_inches='tight')
```

### Annotation Best Practices

- Annotate only the most important values
- Use consistent formatting for numbers
- Position annotations to avoid overlap
- Use subtle colors for annotations (gray or dark version of main color)

---

## Files Provided

- `workshop_starter.ipynb` - Starter notebook with structure and hints
- `workshop_solution.ipynb` - Complete instructor solution (not for student submission)

---

## Submission

Submit your completed notebook and exported figures via the course platform by [deadline].

Create a folder named: `Week9_Workshop_[YourName]/`

Include:
- `workshop_completed.ipynb`
- `figures/` folder with all exported charts

---

## Additional Resources

- [Edward Tufte - The Visual Display of Quantitative Information](https://www.edwardtufte.com/tufte/books_vdqi)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [ColorBrewer - Color Advice for Maps](https://colorbrewer2.org/)

---

*Remember: Good visualization is about communication, not decoration. Every element should serve the data.*
