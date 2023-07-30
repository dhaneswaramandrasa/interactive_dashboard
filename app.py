import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns

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
st.title("RFM Dashboard")

# Plot density plot of 'recency' using Plotly
fig_recency = go.Figure()
fig_recency.add_trace(go.Histogram(x=rfmTable['recency'], histnorm='density', marker=dict(color='blue')))
fig_recency.update_layout(title_text='Density Plot of Recency')

# Show the Plotly figure using Streamlit
st.plotly_chart(fig_recency)

# Plot density plot of 'frequency' using Plotly
fig_frequency = go.Figure()
fig_frequency.add_trace(go.Histogram(x=rfmTable['frequency'], histnorm='density', marker=dict(color='green')))
fig_frequency.update_layout(title_text='Density Plot of Frequency')

# Show the Plotly figure using Streamlit
st.plotly_chart(fig_frequency)

# Plot density plot of 'actual_gmv' using Plotly
fig_actual_gmv = go.Figure()
fig_actual_gmv.add_trace(go.Histogram(x=rfmTable['actual_gmv'], histnorm='density', marker=dict(color='orange')))
fig_actual_gmv.update_layout(title_text='Density Plot of Actual GMV')

# Show the Plotly figure using Streamlit
st.plotly_chart(fig_actual_gmv)

# Plot density plot of 'gmv_missing_indicator' using Plotly
fig_gmv_missing = go.Figure()
fig_gmv_missing.add_trace(go.Histogram(x=rfmTable['gmv_missing_indicator'], histnorm='density', marker=dict(color='red')))
fig_gmv_missing.update_layout(title_text='Density Plot of GMV Missing Values')

# Show the Plotly figure using Streamlit
st.plotly_chart(fig_gmv_missing)
