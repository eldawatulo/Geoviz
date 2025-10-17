

"""viz.py
Visualization utilities for geospatial plotting (static + interactive).
"""
import geopandas as gpd
import matplotlib.pyplot as plt




def plot_choropleth(gdf: gpd.GeoDataFrame, column: str, cmap: str = "OrRd", figsize=(12,8)):
fig, ax = plt.subplots(1, 1, figsize=figsize)
gdf.plot(column=column, cmap=cmap, legend=True, ax=ax, edgecolor='0.8')
ax.set_axis_off()
ax.set_title(f"Choropleth: {column}")
return fig, ax




def top_n_bar(gdf: gpd.GeoDataFrame, column: str, n: int = 10):
df = gdf.nlargest(n, column).set_index('name' if 'name' in gdf.columns else gdf.index)
ax = df[column].plot.barh(figsize=(6, n/2))
ax.invert_yaxis()
ax.set_title(f"Top {n} by {column}")
return ax
