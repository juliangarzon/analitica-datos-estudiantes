# Week 8 Workshop: Visualization Principles

## Creating Publication-Ready Figures with Budget Execution Data

**Duration:** 2 hours (homework or in-class workshop)

**Dataset:** Budget Execution Data (EJECUCION_PRESUPUESTAL) from datos.gov.co

---

## Objectives

By completing this workshop, you will:

1. Create 5 different chart types with real budget data
2. Apply a consistent, professional color palette
3. Add proper titles, labels, and annotations
4. Export publication-ready figures in multiple formats

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

**Chart 1: Horizontal Bar Chart - Budget by Category (15 minutes)**

Create a horizontal bar chart showing budget allocation by category:
- Sort values from largest to smallest
- Use a single professional color
- Add value labels at the end of each bar
- Include a clean title with context
- Remove unnecessary gridlines and spines

**Chart 2: Grouped Bar Chart - Approved vs Executed (15 minutes)**

Create a grouped bar chart comparing approved budget vs executed budget:
- Use two distinct colors (one for approved, one for executed)
- Add a legend
- Show the gap between approved and executed
- Include percentage execution rate in annotations

**Chart 3: Line Chart - Monthly Execution Trend (15 minutes)**

Create a line chart showing monthly budget execution rate:
- Include a target line for reference
- Use color to differentiate actual vs target
- Highlight months where execution was below target
- Add annotations for key data points (start, end, any notable changes)

**Chart 4: Stacked Bar Chart - Budget Composition (15 minutes)**

Create a stacked bar chart showing how the budget is composed:
- Use a sequential color palette (light to dark)
- Add percentage labels within each segment
- Include a legend
- Consider horizontal orientation for readability

**Chart 5: Small Multiples - Department Comparison (15 minutes)**

Create a small multiples visualization comparing execution across departments:
- Use consistent scales across all subplots
- Highlight the department with lowest execution
- Add reference lines at 90% target
- Use minimal styling for each subplot

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

1. **Which chart type was most effective** for communicating the budget story? Why?

2. **What insight would be missed** if you only used one chart type?

3. **If you could only show one chart** to a decision-maker, which would you choose and why?

4. **What additional data** would make these visualizations more impactful?

---

## Deliverables

Your completed workshop should include:

1. **Jupyter Notebook** (`workshop_solution.ipynb`) with:
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
- `workshop_solution.ipynb` - Complete solution (for reference after completion)

---

## Submission

Submit your completed notebook and exported figures via the course platform by [deadline].

Create a folder named: `Week7_Workshop_[YourName]/`

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
