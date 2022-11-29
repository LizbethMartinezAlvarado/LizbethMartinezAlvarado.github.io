import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Walmart USA Dashboard')
st.write("This dashboard intends to show KPI's in USA Walmart branches.")

walmart = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

Segment = list(walmart['Segment'].unique())
Segment
Sales = list(walmart.groupby("Segment")["Sales"].sum())
Sales
fig1 = px.bar(x = Segment, y = Sales, color = Segment, 
                labels={
                     "x": "Segment",
                     "y": "Total sales",
                     "color": "Segments"
                 },
                title="Total sales by segment")
st.plotly_chart(fig1)

fig2 = px.pie(walmart, values='Quantity', names='Category', title = 'Quatity sold by Cateogry')
st.plotly_chart(fig2)

fig3 = px.histogram(walmart, x = "Profit", nbins=50)
st.plotly_chart(fig3)