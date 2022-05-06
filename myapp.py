import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

@st.cache      # IMPORTANT: Cache the conversion to prevent computation on every rerun
def gen_df():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    return chart_data

image = Image.open('KDT-JU.png')
st.title("My first web app")
st.image(image)

df = gen_df()
st.dataframe(df)
sel = st.selectbox('Select column',['a', 'b', 'c'])
st.bar_chart(df[sel])

# Download dataframe
csv_c = df.to_csv().encode('utf-8')
st.download_button(
     label="Download dataframe as CSV",
     data=csv_c,
     file_name=f'df.csv',
     mime='text/csv',
 )
