"""data_processing.py
Reusable functions to load, clean, and save geospatial datasets.
"""
from pathlib import Path
import geopandas as gpd
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)




def load_shapefile(path: str) -> gpd.GeoDataFrame:
"""Load vector data and ensure a consistent CRS (EPSG:4326)."""
gdf = gpd.read_file(path)
if gdf.crs is None:
logging.warning("Input shapefile has no CRS — assuming EPSG:4326")
gdf = gdf.set_crs(epsg=4326)
else:
gdf = gdf.to_crs(epsg=4326)
return gdf




def clean_geodata(gdf: gpd.GeoDataFrame, keep_cols: list = None) -> gpd.GeoDataFrame:
"""Basic cleaning: drop null geometries, select columns, and standardize column names."""
# drop null geometries
gdf = gdf[~gdf.geometry.isnull()].copy()


# standardize column names
gdf.columns = [c.strip().lower().replace(" ", "_") for c in gdf.columns]


if keep_cols:
available = [c for c in keep_cols if c in gdf.columns]
gdf = gdf[available + [gdf.geometry.name]]


# ensure geometry is valid
gdf['geometry'] = gdf['geometry'].buffer(0)


return gdf




def save_geojson(gdf: gpd.GeoDataFrame, filename: str):
out = PROCESSED_DIR / filename
gdf.to_file(out, driver="GeoJSON")
logging.info(f"Saved processed file: {out}")




if __name__ == "__main__":
# quick CLI for local testing
shp = RAW_DIR / "example.shp"
if shp.exists():
g = load_shapefile(str(shp))
g = clean_geodata(g)
save_geojson(g, "example_processed.geojson")
