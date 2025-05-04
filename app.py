import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Car Advertisement Data Dashboard")

df = pd.read_csv("/Users/sunheng/Documents/GitHub/software_development_tools_project/vehicles_us.csv")

if st.checkbox("Show raw data"):
    st.write(df)

st.subheader("Odometer Histogram")
fig1 = px.histogram(df, x="odometer")
st.plotly_chart(fig1)

st.subheader("Price vs Odometer")
fig2 = px.scatter(df, x="odometer", y="price")
st.plotly_chart(fig2)