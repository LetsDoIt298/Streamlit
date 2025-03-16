import streamlit as st
import pandas as pd
import numpy as np


# Totle of Application
st.title('Hello Duniya!!')

# Displaying a simple text
st.write('This is a simple text')

# Displaying df
df = pd.DataFrame({'A':[1,2,3,4,5],
                   'B':[9,8,7,6,5]})
st.write(df)

# Create a line chart
st.line_chart(df)