import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Sample data for demonstration
data = {
    'gmv_missing_indicator': np.random.rand(100),
    'frequency': np.random.rand(100),
    'actual_gmv': np.random.rand(100),
    'class_kmeans_5': np.random.choice([1, 2, 3, 4, 5], size=100)
}
rfm_targeted = pd.DataFrame(data)

# Set the title of the app
st.title("Plotly 3D Scatter Plot in Streamlit")

# Create a 3D scatter plot with Plotly
fig = go.Figure(data=go.Scatter3d(
    x=np.log10(rfm_targeted['gmv_missing_indicator']),
    y=np.log10(rfm_targeted['frequency']),
    z=np.log10(rfm_targeted['actual_gmv']),
    mode='markers',
    marker=dict(size=8, color=rfm_targeted['class_kmeans_5'], colorscale='Viridis'),
    text=rfm_targeted['class_kmeans_5']
))

# Set labels for the axes
fig.update_layout(scene=dict(
    xaxis_title='gmv_missing_indicator',
    yaxis_title='frequency',
    zaxis_title='actual_gmv'
))

# Show the plot using Streamlit
st.plotly_chart(fig)
