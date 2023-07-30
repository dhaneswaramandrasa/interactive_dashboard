import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns
from streamlit_extras.add_vertical_space import add_vertical_space

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

st.write("")
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)

with row3_1:
    # Plot violin plot of 'recency' using Plotly
    fig_recency = go.Figure()
    fig_recency.add_trace(go.Violin(y=rfmTable['recency'], box_visible=True, meanline_visible=True, fillcolor='blue', line_color='blue'))
    fig_recency.update_layout(title_text='Violin Plot of Recency')
    
    # Show the Plotly figure using Streamlit
    st.plotly_chart(fig_recency)
    st.markdown(
    "The distribution of recency across the customer base appears to be quite uniform, suggesting a well-balanced mix of both loyal or new users and long-standing customers."
    )

with row3_2:
    # Plot violin plot of 'frequency' using Plotly
    fig_frequency = go.Figure()
    fig_frequency.add_trace(go.Violin(y=rfmTable['frequency'], box_visible=True, meanline_visible=True, fillcolor='green', line_color='green'))
    fig_frequency.update_layout(title_text='Violin Plot of Frequency')
    
    # Show the Plotly figure using Streamlit
    st.plotly_chart(fig_frequency)
    st.markdown(
    "The frequency distribution across the customer base seems to be heavily concentrated towards the lower end, indicating that a majority of users make only a few orders during the observed period."
    )
    
add_vertical_space()

# Plot violin plot of 'actual_gmv' using Plotly
fig_actual_gmv = go.Figure()
fig_actual_gmv.add_trace(go.Violin(y=rfmTable['actual_gmv'], box_visible=True, meanline_visible=True, fillcolor='orange', line_color='orange'))
fig_actual_gmv.update_layout(title_text='Violin Plot of Actual GMV')

# Show the Plotly figure using Streamlit
st.plotly_chart(fig_actual_gmv)

# Plot violin plot of 'gmv_missing_indicator' using Plotly
fig_gmv_missing = go.Figure()
fig_gmv_missing.add_trace(go.Violin(y=rfmTable['gmv_missing_indicator'], box_visible=True, meanline_visible=True, fillcolor='red', line_color='red'))
fig_gmv_missing.update_layout(title_text='Violin Plot of GMV Missing Values')

# Show the Plotly figure using Streamlit
st.plotly_chart(fig_gmv_missing)
