import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# Sample data for demonstration
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [5, 2, 7, 4, 8]
}
df = pd.DataFrame(data)

# Set the title of the app
st.title("Seaborn Plot in Streamlit")

# Display the DataFrame
st.subheader("Sample Data:")
st.dataframe(df)

# Add a Seaborn plot using Matplotlib
st.subheader("Seaborn Plot:")
sns_plot = sns.barplot(x='x', y='y', data=df)
plt.tight_layout()
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Save the Seaborn plot as an image
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)

# Display the image using Streamlit
st.image(buffer)
