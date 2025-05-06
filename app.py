import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(page_title="Car Advertisement Dashboard", layout="wide")
st.header("Car Advertisement Data Dashboard")
# Load the dataset
df = pd.read_csv("vehicles_us.csv")
# Filter chekbox for expensive cars
expensive = st.checkbox("Show only expensive cars")
if expensive:
    df = df[df['price'] > 50000]
# Filter checkbox for electric cars
electric = st.checkbox("Show only electric cars")
if electric:
    df = df[df['fuel'] == 'electric']
#show raw data
if st.checkbox("Show raw data"):
    st.write(df)

#odometer histogram
st.subheader("Histogram: Vehicle Odometer")
#remove outliers
df = df[df['odometer'] < df['odometer'].quantile(0.95)]
fig1 = px.histogram(df, x='odometer', nbins=50, title='Distribution of Odometer')
st.plotly_chart(fig1, use_container_width=True)


#scatter plot of price vs odometer
st.subheader("Scatter Plot: Price vs Odometer")
fig2 = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig2, use_container_width=True)


#Histogram of vehicle prices
st.subheader("Histogram: Vehicle Prices")
fig3, ax = plt.subplots()
ax.hist(df['price'], bins=50, edgecolor='black')
ax.set_title('Distribution of Vehicle Prices')
ax.set_xlabel('Price')
ax.set_ylabel('# of Vehicles')
st.pyplot(fig3)

#show filtered dataframe
if st.checkbox("Show filtered data frame"):
    st.dataframe(df)
    