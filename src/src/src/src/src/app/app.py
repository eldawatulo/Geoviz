import streamlit as st
import geopandas as gpd
import pandas as pd
from src.viz import plot_choropleth


st.set_page_config(page_title="GeoViz Demo", layout="wide")
st.title("GeoViz Project — Interactive Demo")


@st.cache_data
def load_processed():
return gpd.read_file("data/processed/example_processed.geojson")


gdf = load_processed()


cols = [c for c in gdf.columns if gdf[c].dtype != 'geometry']
metric = st.selectbox("Metric", cols)


fig, ax = plot_choropleth(gdf, column=metric)
st.pyplot(fig)


st.write("Top regions")
st.dataframe(gdf.sort_values(metric, ascending=False).head(10))
