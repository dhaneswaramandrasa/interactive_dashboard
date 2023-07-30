import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Sample data for demonstration
rfmTable = pd.read_parquet('rfmTable.parquet')
rfmTable['class_label'] = np.where(rfmTable['class_kmeans_5'] == 3, 'High Potential', (np.where(rfmTable['class_kmeans_5'] == 0, 'Medium Potential', 'Low Potential')))

# Create a mapping for the categorical label to numerical value
label_mapping = {
    'High Potential': 1,
    'Medium Potential': 2,
    'Low Potential': 3
}

# Convert the categorical label to numerical value
rfmTable['class_label_num'] = rfmTable['class_label'].map(label_mapping)

# Set the title of the app
st.title("Plotly 3D Scatter Plot in Streamlit")

# Create a 3D scatter plot with Plotly
fig = go.Figure(data=go.Scatter3d(
    x=np.log10(rfmTable['recency']),
    y=np.log10(rfmTable['frequency']),
    z=np.log10(rfmTable['actual_gmv']),
    mode='markers',
    marker=dict(size=8, color=rfmTable['class_label_num'], colorscale='Viridis'),
    text=rfmTable['class_label']
))

# Set labels for the axes
fig.update_layout(scene=dict(
    xaxis_title='recency',
    yaxis_title='frequency',
    zaxis_title='actual_gmv'
))

# Show the plot using Streamlit
st.plotly_chart(fig)
