import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')
st.write("Please find some great correlation analysis!")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

import seaborn as sns
viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

continents = df_cars['continent']
continents_choice = st.sidebar.selectbox('Select your continent:', continents)
