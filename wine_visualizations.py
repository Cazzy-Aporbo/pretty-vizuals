import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import load_wine
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.io as pio

# Set Plotly to open graphs in the default web browser
pio.renderers.default = "browser"

# Load the wine dataset
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["target"] = wine.target

# Define rustic matte color palette
rustic_colors = [
    "#6A4C93",  # Medium purple
    "#3E5C76",  # Squash blue
    "#7C9E8F",  # Sage green
    "#FF8C42",  # Tangerine
    "#8B5E3C",  # Rusty brown
    "#4A6C6F",  # Deep teal
]

# 1. Parallel Coordinates Plot
fig1 = px.parallel_coordinates(
    df,
    dimensions=wine.feature_names[:5],  # Use first 5 features for clarity
    color="target",
    color_continuous_scale=rustic_colors,
    labels={col: col for col in wine.feature_names[:5]},
    title="Parallel Coordinates Plot of Wine Features",
)
fig1.update_layout(plot_bgcolor="#F5F5F5", paper_bgcolor="#FFFFFF")
fig1.show()

# 2. 3D Scatter Plot
fig2 = px.scatter_3d(
    df,
    x="alcohol",
    y="malic_acid",
    z="ash",
    color="target",
    color_continuous_scale=rustic_colors,
    title="3D Scatter Plot: Alcohol vs Malic Acid vs Ash",
)
fig2.update_layout(plot_bgcolor="#F5F5F5", paper_bgcolor="#FFFFFF")
fig2.show()

# 3. Heatmap for Feature Correlations
corr = df.corr()
fig3 = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.columns,
    colorscale=rustic_colors,
))
fig3.update_layout(
    title="Feature Correlation Heatmap",
    plot_bgcolor="#F5F5F5",
    paper_bgcolor="#FFFFFF",
    xaxis=dict(tickangle=45),
)
fig3.show()

# 4. Pairplot for Pairwise Relationships
fig4 = px.scatter_matrix(
    df,
    dimensions=wine.feature_names[:5],  # Limit to 5 features for clarity
    color="target",
    color_continuous_scale=rustic_colors,
    title="Pairwise Relationships in Wine Dataset",
)
fig4.update_layout(plot_bgcolor="#F5F5F5", paper_bgcolor="#FFFFFF")
fig4.show()

# 5. Stacked Bar Chart (Mean Features by Wine Class)
df_grouped = df.groupby("target").mean().iloc[:, :5]  # Use first 5 features
df_grouped.plot(kind="bar", stacked=True, color=rustic_colors, figsize=(10, 6))
plt.title("Stacked Bar Chart: Mean Features by Wine Class", fontsize=14)
plt.xlabel("Wine Class", fontsize=12)
plt.ylabel("Mean Feature Value", fontsize=12)
plt.legend(title="Features", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()