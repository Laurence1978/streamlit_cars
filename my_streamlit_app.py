import streamlit as st
import pandas as pd
import requests 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
###### titre de la page

st.title("Cars correlation analysis")
st.image("https://static.vecteezy.com/system/resources/previews/000/524/893/non_2x/vector-car-set.jpg")

# Barre latérale

st.sidebar.image("https://image.slidesharecdn.com/selection-140227104030-phpapp02/95/selection-1-638.jpg?cb=1393497658")
continent = st.sidebar.radio("Select your Continent :", ('All','USA', 'Europe', 'Japan'))
genre = st.sidebar.radio("Select your Category :",df_cars.columns.values)

# 2 tabs
tab1, tab2 = st.tabs(["Data Frame", "Correlation"])
# Je commence par la 1ère tab et j'y insère ce dont je veux afficher et ainsi de suite
with tab1:
    if continent == 'All':
        df_auto = df_cars
        df_auto
    elif continent == 'USA':
        df_auto = df_cars.loc[(df_cars["continent"] == " US.")]
        df_auto
    elif continent == 'Europe':
        df_auto = df_cars.loc[(df_cars['continent'] == " Europe.")]
        df_auto
    elif continent == 'Japan':
        df_auto = df_cars.loc[(df_cars['continent'] == " Japan.")]
        df_auto

with tab2:
    viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
                                								)
    if continent == 'All':
        st.write("Quelquesoit le continent, il y a de de fortes corrélations entre les catégories cylinder, cubicinches, hp et weightlbs.")
    elif continent == 'USA':
        st.write("Aux USA, il y a de de fortes corrélations entre les catégories cylinder, cubicinches, hp et weightlbs.")
    elif continent == 'Europe':
        st.write("EN Europe, il y a de de fortes corrélations entre les catégories cylinder, cubicinches, hp et weightlbs .")
    elif continent == 'Japan':
        st.write("Au Japon, il y a de de fortes corrélations entre les catégories cylinder, cubicinches, hp et weightlbs.")

    st.pyplot(viz_correlation.figure)
    fig = plt.title('Corrélation entre les différentes caractéristiques de voitures', size = 14)
  