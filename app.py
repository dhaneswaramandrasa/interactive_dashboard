import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
st.title("Visualizations in Streamlit")

# Create a 3D scatter plot with Plotly
fig_3d = go.Figure(data=go.Scatter3d(
    x=np.log10(rfmTable['recency']),
    y=np.log10(rfmTable['frequency']),
    z=np.log10(rfmTable['actual_gmv']),
    mode='markers',
    marker=dict(size=8, color=rfmTable['class_label_num'], colorscale='Viridis'),
    text=rfmTable['class_label']
))

# Set labels for the axes
fig_3d.update_layout(scene=dict(
    xaxis_title='recency',
    yaxis_title='frequency',
    zaxis_title='actual_gmv'
))

# Show the 3D scatter plot using Streamlit
st.plotly_chart(fig_3d)

# Create a bar plot using Matplotlib
fig_bar = plt.figure(figsize=(10, 6))
plt.bar(rfmTable['class_label'], rfmTable['frequency'])
plt.xlabel('Class Label')
plt.ylabel('Frequency')

# Show the bar plot using Streamlit
st.pyplot(fig_bar)
