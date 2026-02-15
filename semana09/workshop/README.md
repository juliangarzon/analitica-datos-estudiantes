# Week 9 Workshop: Build a Budget Execution Dashboard

## Overview

| Item | Details |
|------|---------|
| **Duration** | 90 minutes |
| **Dataset** | Budget Execution (Ejecucion Presupuestal) |
| **Deliverable** | Working Streamlit dashboard |
| **Tools** | Python, Plotly, Streamlit |

---

## Learning Objectives

By completing this workshop, you will be able to:

1. Build a complete Streamlit web application
2. Implement filter widgets (selectbox, multiselect, slider)
3. Display key metrics using `st.metric()`
4. Create and display 4 interactive Plotly charts
5. Organize dashboard layout with columns and sidebar

---

## Prerequisites

### Install Required Packages

```bash
pip install streamlit plotly pandas
```

### Verify Installation

```bash
streamlit --version
```

---

## Dashboard Requirements

Your dashboard must include:

### 1. Title and Description
- Application title
- Brief description of what the dashboard shows
- Data source information

### 2. Three Filter Widgets (in sidebar)

| Widget | Type | Purpose |
|--------|------|---------|
| Department | `multiselect` | Filter by one or more departments |
| Year | `slider` | Filter by year range |
| Show Raw Data | `checkbox` | Toggle data table visibility |

### 3. Four Charts

| Chart # | Type | Purpose |
|---------|------|---------|
| 1 | Bar Chart | Budget by department (approved vs executed) |
| 2 | Line Chart | Budget trend over years |
| 3 | Pie Chart | Budget distribution by category |
| 4 | Scatter Plot | Approved vs Executed with size = execution rate |

### 4. Key Metrics Row

Display these 3 metrics at the top:

| Metric | Calculation |
|--------|-------------|
| Total Approved Budget | Sum of approved budget |
| Total Executed Budget | Sum of executed budget |
| Average Execution Rate | Executed / Approved * 100 |

---

## Workshop Structure

### Part 1: Plotly Exercises (30 minutes)
Complete `workshop_starter.ipynb` to practice Plotly charts.

### Part 2: Streamlit Dashboard (60 minutes)
Build the complete dashboard using `streamlit_app_starter.py`.

---

## Files in This Workshop

| File | Purpose |
|------|---------|
| `workshop_starter.ipynb` | Plotly practice exercises |
| `workshop_solution.ipynb` | Plotly solutions |
| `streamlit_app_starter.py` | Dashboard starter template |
| `streamlit_app_solution.py` | Complete dashboard solution |

---

## Running the Streamlit App

### Step 1: Navigate to workshop directory
```bash
cd /path/to/semana08/workshop
```

### Step 2: Run the app
```bash
streamlit run streamlit_app_starter.py
```

### Step 3: View in browser
The app will open automatically at `http://localhost:8501`

### Step 4: Make changes and refresh
- Edit the Python file
- Save your changes
- Click "Rerun" in the browser (or enable "Always rerun")

---

## Streamlit Quick Reference

### Text and Titles
```python
st.title('Main Title')
st.header('Section Header')
st.subheader('Subsection')
st.write('Regular text')
st.markdown('**Bold** and *italic*')
```

### Widgets
```python
# Selectbox (single choice)
selected = st.selectbox('Label', options=['A', 'B', 'C'])

# Multiselect (multiple choices)
selected_list = st.multiselect('Label', options=['A', 'B', 'C'], default=['A'])

# Slider (numeric range)
year = st.slider('Year', min_value=2020, max_value=2024, value=(2020, 2024))

# Checkbox (boolean)
show_data = st.checkbox('Show raw data')
```

### Layout
```python
# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Label', value, delta)

# Sidebar
with st.sidebar:
    st.title('Filters')
    # widgets go here

# Tabs
tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
with tab1:
    # content for tab 1
```

### Display
```python
# Metrics
st.metric(label='Total', value=1000, delta='+10%')

# DataFrames
st.dataframe(df)  # Interactive
st.table(df)      # Static

# Plotly charts
st.plotly_chart(fig, use_container_width=True)
```

### Control Flow
```python
# Stop execution if condition not met
if len(selected) == 0:
    st.warning('Please select at least one option')
    st.stop()
```

---

## Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Install streamlit: `pip install streamlit`

### Issue: "fig.show() opens in browser, not in app"
**Solution:** Use `st.plotly_chart(fig)` instead of `fig.show()`

### Issue: "Multiselect returns empty list and breaks filter"
**Solution:** Check for empty selection before filtering:
```python
if len(selected_depts) == 0:
    st.warning('Please select at least one department')
    st.stop()
```

### Issue: "Chart is too narrow"
**Solution:** Add `use_container_width=True`:
```python
st.plotly_chart(fig, use_container_width=True)
```

### Issue: "TypeError: cannot use == with list"
**Solution:** Use `.isin()` for multiselect filtering:
```python
# Wrong
filtered = df[df['dept'] == selected_depts]

# Right
filtered = df[df['dept'].isin(selected_depts)]
```

---

## Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| Title & Description | 10 | App has clear title and description |
| Filter Widgets | 20 | 3 working filters (multiselect, slider, checkbox) |
| Key Metrics | 15 | 3 metrics displayed correctly |
| Bar Chart | 15 | Department comparison chart |
| Line Chart | 10 | Year trend chart |
| Pie Chart | 10 | Category distribution chart |
| Scatter Plot | 10 | Approved vs Executed with size |
| Layout | 10 | Clean organization with sidebar and columns |
| **Total** | **100** | |

---

## Bonus Challenges

If you finish early, try these enhancements:

1. **Add a download button** for filtered data
   ```python
   st.download_button('Download CSV', filtered.to_csv(), 'data.csv')
   ```

2. **Add a category filter** (fourth filter widget)

3. **Add delta values** to metrics showing change from previous year

4. **Add color to metrics** based on performance (green for good, red for bad)

5. **Create a two-tab layout** separating Overview and Details

---

## Submission

Submit the following:
1. Your completed `streamlit_app.py` file
2. A screenshot of your running dashboard

---

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [Streamlit Gallery](https://streamlit.io/gallery)

---

*Last updated: January 2026*
