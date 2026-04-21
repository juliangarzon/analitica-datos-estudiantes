from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "calidad_aire_risaralda.csv"


st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="🌫️",
    layout="wide",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df = df.rename(
        columns={
            "Municipio": "municipio",
            "Estacion": "estacion",
            "Fecha": "fecha",
            "Diametro aerodinamico": "diametro",
            "Medicion": "medicion",
        }
    )
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["municipio"] = df["municipio"].astype(str).str.strip()
    df["estacion"] = df["estacion"].astype(str).str.strip()
    df["diametro"] = df["diametro"].astype(str).str.strip()
    df["medicion"] = pd.to_numeric(df["medicion"], errors="coerce")
    return df.dropna(subset=["fecha", "medicion"]).sort_values("fecha")


df = load_data()


st.title("Air Quality Dashboard")
st.write(
    "Complete this template to explore particulate matter measurements in Risaralda."
)


with st.sidebar:
    st.header("Filters")

    # TODO: Replace the placeholders with real default values.
    selected_municipios = st.multiselect(
        "Municipios",
        options=sorted(df["municipio"].unique()),
        default=___,
    )

    selected_particles = st.multiselect(
        "Particle type",
        options=sorted(df["diametro"].unique()),
        default=___,
    )

    min_date = df["fecha"].min().date()
    max_date = df["fecha"].max().date()

    date_range = st.slider(
        "Date range",
        min_value=min_date,
        max_value=max_date,
        value=___,
    )

    show_table = st.checkbox("Show filtered data", value=False)


# TODO: Stop execution if one of the multiselect filters is empty.

filtered_df = df[
    df["municipio"].isin(selected_municipios)
    & df["diametro"].isin(selected_particles)
    & df["fecha"].dt.date.between(date_range[0], date_range[1])
].copy()


# TODO: Create three KPI columns with st.columns(3).
metric_col1, metric_col2, metric_col3 = ___

average_measurement = filtered_df["medicion"].mean()
peak_measurement = filtered_df["medicion"].max()
total_records = len(filtered_df)

with metric_col1:
    st.metric("Average measurement", ___)

with metric_col2:
    st.metric("Peak measurement", ___)

with metric_col3:
    st.metric("Records", ___)


chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Trend over time")

    trend_df = (
        filtered_df.groupby(["fecha", "diametro"], as_index=False)["medicion"]
        .mean()
        .sort_values("fecha")
    )

    fig_trend = px.line(
        trend_df,
        x="fecha",
        y="medicion",
        color="diametro",
        markers=True,
        title="Average measurement by day",
    )
    fig_trend.update_layout(xaxis_title="", yaxis_title="Measurement")
    st.plotly_chart(___, use_container_width=True)

with chart_col2:
    st.subheader("Average by municipality")

    municipality_df = (
        filtered_df.groupby("municipio", as_index=False)["medicion"]
        .mean()
        .sort_values("medicion", ascending=False)
    )

    fig_bar = px.bar(
        municipality_df,
        x="municipio",
        y="medicion",
        color="municipio",
        title="Average particulate matter by municipality",
    )
    fig_bar.update_layout(showlegend=False, xaxis_title="", yaxis_title="Measurement")
    st.plotly_chart(___, use_container_width=True)


st.subheader("Distribution by station")

station_df = filtered_df.copy()
fig_box = px.box(
    station_df,
    x="estacion",
    y="medicion",
    color="diametro",
    title="Measurement variability by station",
)
fig_box.update_layout(xaxis_title="", yaxis_title="Measurement")
st.plotly_chart(___, use_container_width=True)


if show_table:
    st.subheader("Filtered data")
    st.dataframe(filtered_df, use_container_width=True)
