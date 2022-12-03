import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Walmart USA Dashboard')
st.sidebar.caption('Click the sliders to control the graphs')
st.write('This dashboard intends to show the quantity sold by subcategory in USA Walmart branches.')


walmart = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

selected_ship = st.sidebar.radio('Select ship mode', walmart['Ship Mode'].unique())

selected_category = st.sidebar.selectbox('Select the category', walmart['Category'].unique())

optionals = st.sidebar.expander('Optional configurations',True)
selected_discount=optionals.slider('Select the discount percentage',
min_value = float(walmart['Discount'].min()),
max_value = float(walmart['Discount'].max()))

walmart_selected = walmart.loc[(walmart['Discount'] == selected_discount) & 
(walmart['Ship Mode'] == selected_ship) & 
(walmart['Category'] == selected_category), 
['Sub-Category','Quantity']]

fig = px.pie(walmart_selected, values='Quantity', names='Sub-Category')

st.plotly_chart(fig)