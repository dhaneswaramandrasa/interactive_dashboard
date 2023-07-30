import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# Create subplots
fig_dist, axes = plt.subplots(2, 4, figsize=(90, 60))

# Plot density plot of 'recency'
sns.kdeplot(rfmTable['recency'], ax=axes[0, 0], vertical=False)
sns.violinplot(y=rfmTable['recency'], ax=axes[1, 0])
axes[0, 0].set_xlabel('Recency')
axes[0, 0].set_ylabel('Density')
axes[0, 0].set_title('Density Plot of Recency')

# Plot density plot of 'frequency'
sns.kdeplot(rfmTable['frequency'], ax=axes[0, 1], vertical=False)
sns.violinplot(y=rfmTable['frequency'], ax=axes[1, 1])
axes[0, 1].set_xlabel('Frequency')
axes[0, 1].set_ylabel('Density')
axes[0, 1].set_title('Density Plot of Frequency')

# Plot density plot of 'actual_gmv'
sns.kdeplot(rfmTable['actual_gmv'], ax=axes[0, 2], vertical=False)
sns.violinplot(y=rfmTable['actual_gmv'], ax=axes[1, 2])
axes[0, 2].set_xlabel('Actual GMV')
axes[0, 2].set_ylabel('Density')
axes[0, 2].set_title('Density Plot of Actual GMV')

# Plot density plot of 'actual_gmv'
sns.kdeplot(rfmTable['gmv_missing_indicator'], ax=axes[0, 3], vertical=False)
sns.violinplot(y=rfmTable['gmv_missing_indicator'], ax=axes[1, 3])
axes[0, 3].set_xlabel('GMV missing values')
axes[0, 3].set_ylabel('Density')
axes[0, 3].set_title('Density Plot of GMV missing values')


# Show the bar plot using Streamlit
st.pyplot(fig_dist)
