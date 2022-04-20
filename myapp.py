import pandas as pd
import numpy as np
import streamlit as st

st.title('This is my first web app')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.table(chart_data.iloc[0:])

option = st.selectbox('Select a column', chart_data.columns.tolist())
st.bar_chart(option)
