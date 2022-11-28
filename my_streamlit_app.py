import streamlit as st
import pandas as pd
import requests 
import seaborn as sns
import matplotlib.pyplot as plt


###### titre de la page

st.title("Cars Analysis")
st.image("https://static.vecteezy.com/system/resources/previews/000/524/893/non_2x/vector-car-set.jpg",  width=100)

###### selection par continent

continent = st.sidebar.selectbox(
	    'Quel continent ?',
	    ('US.', 'Europe', 'Japan'))

col1, col2 = st.columns([2, 1])

with col1:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df_cars[continent])
st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax = sns.boxplot(df_cars[continent])


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)



