from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "violencia_intrafamiliar_demo.csv"
)


st.set_page_config(
    page_title="Violencia Intrafamiliar Dashboard",
    page_icon="📉",
    layout="wide",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, low_memory=False)
    df = df.rename(
        columns={
            "Año del hecho": "year",
            "Sexo de la victima": "victim_sex",
            "Ciclo Vital": "life_stage",
            "Contexto del Hecho": "context",
            "Departamento del hecho DANE": "department",
            "Municipio del hecho DANE": "municipality",
            "Presunto Agresor Detallado": "aggressor",
            "Factor Desencadenante de la Agresión": "trigger",
        }
    )
    df["year"] = pd.to_numeric(df["year"], errors="coerce")

    for column in [
        "victim_sex",
        "life_stage",
        "context",
        "department",
        "municipality",
        "aggressor",
        "trigger",
    ]:
        if column in df.columns:
            df[column] = df[column].fillna("Sin información").astype(str).str.strip()

    return df.dropna(subset=["year"])


df = load_data()

available_departments = (
    sorted(df["department"].unique()) if "department" in df.columns else []
)
available_contexts = sorted(df["context"].unique()) if "context" in df.columns else []
available_sexes = sorted(df["victim_sex"].unique())


st.title("Violencia intrafamiliar en Colombia")
st.caption(
    "Demo de dashboard para mostrar estructura, filtros y lectura de insights con un dataset nacional."
)


with st.sidebar:
    st.header("Filters")

    year_min = int(df["year"].min())
    year_max = int(df["year"].max())
    selected_years = st.slider(
        "Year range",
        min_value=year_min,
        max_value=year_max,
        value=(year_min, year_max),
    )

    selected_sexes = st.multiselect(
        "Victim sex",
        options=available_sexes,
        default=available_sexes,
    )

    selected_contexts = st.multiselect(
        "Context",
        options=available_contexts,
        default=available_contexts[:3] if len(available_contexts) >= 3 else available_contexts,
    )

    selected_departments = st.multiselect(
        "Department",
        options=available_departments,
        default=available_departments[:8] if len(available_departments) >= 8 else available_departments,
    )


filtered_df = df[df["year"].between(selected_years[0], selected_years[1])]
filtered_df = filtered_df[filtered_df["victim_sex"].isin(selected_sexes)]

if "context" in filtered_df.columns and selected_contexts:
    filtered_df = filtered_df[filtered_df["context"].isin(selected_contexts)]

if "department" in filtered_df.columns and selected_departments:
    filtered_df = filtered_df[filtered_df["department"].isin(selected_departments)]

if filtered_df.empty:
    st.error("No rows match the current selection.")
    st.stop()


metric_col1, metric_col2, metric_col3 = st.columns(3)

total_cases = len(filtered_df)
female_share = (
    (filtered_df["victim_sex"].eq("Mujer").mean() * 100)
    if "Mujer" in filtered_df["victim_sex"].values
    else 0
)
top_stage = (
    filtered_df["life_stage"].value_counts().idxmax()
    if "life_stage" in filtered_df.columns
    else "N/A"
)

with metric_col1:
    st.metric("Cases", f"{total_cases:,}")

with metric_col2:
    st.metric("Women share", f"{female_share:.1f}%")

with metric_col3:
    st.metric("Most frequent life stage", top_stage)


top_col1, top_col2 = st.columns(2)

with top_col1:
    annual_df = filtered_df.groupby("year", as_index=False).size()
    fig_annual = px.line(
        annual_df,
        x="year",
        y="size",
        markers=True,
        title="Cases by year",
    )
    fig_annual.update_layout(xaxis_title="", yaxis_title="Cases")
    st.plotly_chart(fig_annual, use_container_width=True)

with top_col2:
    life_stage_df = (
        filtered_df.groupby("life_stage", as_index=False)
        .size()
        .sort_values("size", ascending=False)
        .head(8)
    )
    fig_life_stage = px.bar(
        life_stage_df,
        x="life_stage",
        y="size",
        color="life_stage",
        title="Top life stages",
    )
    fig_life_stage.update_layout(showlegend=False, xaxis_title="", yaxis_title="Cases")
    st.plotly_chart(fig_life_stage, use_container_width=True)


bottom_col1, bottom_col2 = st.columns(2)

with bottom_col1:
    if "department" in filtered_df.columns:
        department_df = (
            filtered_df.groupby("department", as_index=False)
            .size()
            .sort_values("size", ascending=False)
            .head(10)
        )
        fig_department = px.bar(
            department_df,
            x="department",
            y="size",
            color="department",
            title="Departments with more reported cases",
        )
        fig_department.update_layout(showlegend=False, xaxis_title="", yaxis_title="Cases")
        st.plotly_chart(fig_department, use_container_width=True)

with bottom_col2:
    if "aggressor" in filtered_df.columns:
        aggressor_df = (
            filtered_df.groupby("aggressor", as_index=False)
            .size()
            .sort_values("size", ascending=False)
            .head(10)
        )
        fig_aggressor = px.bar(
            aggressor_df,
            x="aggressor",
            y="size",
            color="aggressor",
            title="Most common aggressor categories",
        )
        fig_aggressor.update_layout(showlegend=False, xaxis_title="", yaxis_title="Cases")
        st.plotly_chart(fig_aggressor, use_container_width=True)


st.subheader("What this demo should teach")
st.markdown(
    """
- A useful dashboard starts with a clear question, not with charts.
- Filters should reduce noise and help comparison.
- Metrics summarize, charts explain, and tables support verification.
- The same structural pattern can be reused with another public dataset.
"""
)
