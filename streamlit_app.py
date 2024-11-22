import streamlit as st
import pandas as pd

st.title('Rainfall Prediction')

st.info('This is a rainfall prediction app')

with st.expander('Data'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/HrishikeshGirsawale/duniya_ka_papa/refs/heads/main/Rainfall.csv')
  df

  st.write('X')
  X = df.drop('rainfall', axis=1)
  X

  st.write('y')
  y = df.rainfall
  y

with st.expander('Data visualization')
  st.scatter_chart(data=df, x='temparature', y='humidity', color='rainfall')
