"""utils.py
Helper utilities: logging, assertions, CRS checks.
"""
import logging
import geopandas as gpd




def assert_no_null_geoms(gdf: gpd.GeoDataFrame):
nulls = gdf.geometry.isnull().sum()
assert nulls == 0, f"Found {nulls} null geometries"




def ensure_crs(gdf: gpd.GeoDataFrame, epsg: int = 4326) -> gpd.GeoDataFrame:
if gdf.crs is None:
gdf = gdf.set_crs(epsg=epsg)
else:
gdf = gdf.to_crs(epsg=epsg)
return gdf
