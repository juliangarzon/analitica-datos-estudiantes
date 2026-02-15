"""
Week 9 Workshop: Budget Execution Dashboard
Streamlit App - STARTER TEMPLATE

Instructions:
1. Complete the TODO sections
2. Run with: streamlit run streamlit_app_starter.py
3. Test your filters and charts

Requirements:
- Title and description
- 3 filter widgets (multiselect, slider, checkbox)
- 3 key metrics
- 4 interactive charts
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title='Budget Dashboard',
    page_icon='📊',
    layout='wide'
)

# =============================================================================
# DATA LOADING
# =============================================================================

@st.cache_data
def load_data():
    """
    Create sample Budget Execution dataset.
    In production, this would load from a CSV or database.
    """
    np.random.seed(42)

    departments = ['Education', 'Health', 'Infrastructure', 'Security', 'Social Services', 'Environment']
    years = [2021, 2022, 2023, 2024]
    categories = ['Personnel', 'Operations', 'Investment', 'Transfers']

    data = []
    for dept in departments:
        for year in years:
            for cat in categories:
                approved = np.random.randint(100000, 5000000)
                execution_rate = np.random.uniform(0.6, 1.0)
                executed = int(approved * execution_rate)

                data.append({
                    'department': dept,
                    'year': year,
                    'category': cat,
                    'budget_approved': approved,
                    'budget_executed': executed,
                    'execution_rate': round(execution_rate * 100, 1),
                    'project_count': np.random.randint(5, 50)
                })

    return pd.DataFrame(data)

# Load data
df = load_data()

# =============================================================================
# SIDEBAR - FILTERS
# =============================================================================

with st.sidebar:
    st.title('Filters')
    st.markdown('---')

    # TODO: FILTER 1 - Department Multiselect
    # Create a multiselect widget for departments
    # Hint: st.multiselect('Label', options, default)

    selected_departments = st.multiselect(
        'Select Departments',
        options=___,  # df['department'].unique()
        default=___   # df['department'].unique() to select all by default
    )

    # TODO: FILTER 2 - Year Slider
    # Create a slider for year range
    # Hint: st.slider('Label', min, max, (default_min, default_max))

    year_range = st.slider(
        'Select Year Range',
        min_value=___,  # int(df['year'].min())
        max_value=___,  # int(df['year'].max())
        value=___       # (min_year, max_year) as tuple
    )

    # TODO: FILTER 3 - Show Raw Data Checkbox
    # Create a checkbox to toggle data table visibility
    # Hint: st.checkbox('Label')

    show_data = st.checkbox(___)  # 'Show Raw Data'

    st.markdown('---')
    st.caption('Data source: Budget Execution Dataset')

# =============================================================================
# APPLY FILTERS
# =============================================================================

# TODO: Check if departments are selected
# If no departments selected, show warning and stop
# Hint: if len(selected_departments) == 0: st.warning(...); st.stop()

if len(selected_departments) == 0:
    st.warning(___)  # 'Please select at least one department'
    st.stop()

# TODO: Create filter mask
# Filter by selected departments AND year range
# Hint: df['column'].isin(list) & df['column'].between(min, max)

mask = (
    df['department'].isin(___) &  # selected_departments
    df['year'].between(___)       # year_range[0], year_range[1]
)

filtered_df = df[mask]

# =============================================================================
# HEADER
# =============================================================================

st.title('Budget Execution Dashboard')
st.markdown('Interactive visualization of budget allocation and execution across departments.')

st.markdown('---')

# =============================================================================
# KEY METRICS
# =============================================================================

# TODO: Create 3 columns for metrics
# Hint: col1, col2, col3 = st.columns(3)

col1, col2, col3 = st.columns(___)  # 3

# TODO: Calculate metrics
total_approved = filtered_df['budget_approved'].sum()
total_executed = filtered_df['budget_executed'].sum()
avg_execution_rate = ___  # (total_executed / total_approved * 100)

# TODO: Display metrics
# Hint: col1.metric('Label', value, delta=None)

with col1:
    st.metric(
        label='Total Approved Budget',
        value=f'${total_approved:,.0f}'
    )

with col2:
    st.metric(
        label=___,  # 'Total Executed Budget'
        value=___   # f'${total_executed:,.0f}'
    )

with col3:
    st.metric(
        label=___,  # 'Execution Rate'
        value=___   # f'{avg_execution_rate:.1f}%'
    )

st.markdown('---')

# =============================================================================
# CHARTS
# =============================================================================

# Create 2 columns for charts
chart_col1, chart_col2 = st.columns(2)

# ----- CHART 1: Bar Chart - Department Comparison -----
with chart_col1:
    st.subheader('Budget by Department')

    # TODO: Aggregate data by department
    dept_data = filtered_df.groupby('department').agg({
        'budget_approved': 'sum',
        'budget_executed': 'sum'
    }).reset_index()

    # Reshape for grouped bar chart
    dept_melted = dept_data.melt(
        id_vars=['department'],
        value_vars=['budget_approved', 'budget_executed'],
        var_name='type',
        value_name='amount'
    )
    dept_melted['type'] = dept_melted['type'].replace({
        'budget_approved': 'Approved',
        'budget_executed': 'Executed'
    })

    # TODO: Create grouped bar chart
    # Hint: px.bar(data, x=..., y=..., color=..., barmode='group')

    fig1 = px.bar(
        dept_melted,
        x=___,  # 'department'
        y=___,  # 'amount'
        color=___,  # 'type'
        barmode='group',
        color_discrete_map={'Approved': '#636EFA', 'Executed': '#00CC96'}
    )

    fig1.update_layout(
        xaxis_title='',
        yaxis_title='Budget ($)',
        legend_title='',
        xaxis_tickangle=45,
        height=400
    )

    # TODO: Display chart
    # Hint: st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(___, use_container_width=True)

# ----- CHART 2: Line Chart - Year Trend -----
with chart_col2:
    st.subheader('Budget Trend Over Time')

    # Aggregate by year
    year_data = filtered_df.groupby('year').agg({
        'budget_approved': 'sum',
        'budget_executed': 'sum'
    }).reset_index()

    year_melted = year_data.melt(
        id_vars=['year'],
        value_vars=['budget_approved', 'budget_executed'],
        var_name='type',
        value_name='amount'
    )
    year_melted['type'] = year_melted['type'].replace({
        'budget_approved': 'Approved',
        'budget_executed': 'Executed'
    })

    # TODO: Create line chart
    # Hint: px.line(data, x=..., y=..., color=..., markers=True)

    fig2 = px.line(
        year_melted,
        x=___,  # 'year'
        y=___,  # 'amount'
        color=___,  # 'type'
        markers=True
    )

    fig2.update_layout(
        xaxis_title='Year',
        yaxis_title='Budget ($)',
        legend_title='',
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)

# Second row of charts
chart_col3, chart_col4 = st.columns(2)

# ----- CHART 3: Pie Chart - Category Distribution -----
with chart_col3:
    st.subheader('Distribution by Category')

    # Aggregate by category
    cat_data = filtered_df.groupby('category')['budget_executed'].sum().reset_index()

    # TODO: Create pie chart
    # Hint: px.pie(data, values=..., names=..., hole=0.3)

    fig3 = px.pie(
        cat_data,
        values=___,  # 'budget_executed'
        names=___,   # 'category'
        hole=0.3
    )

    fig3.update_traces(textposition='inside', textinfo='percent+label')
    fig3.update_layout(height=400)

    st.plotly_chart(fig3, use_container_width=True)

# ----- CHART 4: Scatter Plot - Execution Analysis -----
with chart_col4:
    st.subheader('Execution Analysis')

    # TODO: Create scatter plot
    # Hint: px.scatter(data, x=..., y=..., color=..., size=...)

    fig4 = px.scatter(
        filtered_df,
        x=___,  # 'budget_approved'
        y=___,  # 'budget_executed'
        color=___,  # 'department'
        size=___,   # 'execution_rate'
        hover_name='category',
        hover_data=['year', 'project_count'],
        opacity=0.7
    )

    # Add reference line (y = x)
    max_val = max(filtered_df['budget_approved'].max(), filtered_df['budget_executed'].max())
    fig4.add_trace(
        go.Scatter(
            x=[0, max_val],
            y=[0, max_val],
            mode='lines',
            name='Perfect Execution',
            line=dict(dash='dash', color='gray')
        )
    )

    fig4.update_layout(
        xaxis_title='Approved ($)',
        yaxis_title='Executed ($)',
        height=400
    )

    st.plotly_chart(fig4, use_container_width=True)

# =============================================================================
# RAW DATA (Conditional)
# =============================================================================

# TODO: Show data table if checkbox is checked
# Hint: if show_data: st.dataframe(...)

if show_data:
    st.markdown('---')
    st.subheader('Raw Data')
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # Show data summary
    st.caption(f'Showing {len(filtered_df)} records')

# =============================================================================
# FOOTER
# =============================================================================

st.markdown('---')
st.caption('Week 9 Workshop - Data Analytics Course | Built with Streamlit and Plotly')
