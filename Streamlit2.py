import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt




region = st.sidebar.selectbox("Sélectionner la région: ", ('Europe', 'Japon', 'USA')) 
  
if (region == 'Europe'): 
    continent = ' Europe.'
elif(region == 'Japon'):  
    continent = ' Japan.'
else :
    continent = ' US.'
    
st.sidebar.write("La sélection s'applique uniquement sur le dernier graphique (courbe).")
    
st.title('Evolution des voitures au fil des ans au Japon, aux USA et en Europe.')

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)

#affichage du pairplot
st.write("**Corrélation entre les différentes variables**")
st.write(' ')
st.write("Le graphique ci dessous montre les corrélations entre les différentes caractéristiques des voitures, tout pays confondus. Bien qu'il nous permettent de déceler différents liens, il est plus facile d'utiliser la heatmap en dessous de ce premier graphique.")
fig3 = sns.pairplot(df_voiture)
st.pyplot(fig3)

#fig1=px.scatter_matrix(data_frame = df_voiture,dimensions=["mpg", "cylinders", "cubicinches", "weightlbs", "time-to-60", "year", "continent"])
#barplot_chart = st.write(fig1)

#Affichage de la heatmap
st.write(' ')
st.write(' ')
st.write(' ')
st.write("**Heatmap**")
st.write(' ')
st.write("Le graphique ci dessous fait clairement apparaitre des liens forts entre le nombre de cylindres, la cylindrée, la puissance et le poids. Chacune de cette variable croit simultanément. A l'inverse, la variable 'mpg' est corrélé négativement à ces variables. Ce qui signifie malgré tout que plus les variables cités précédement sont élevées plus la consomation de carburant est importante. ")

fig2, ax = plt.subplots()
upp_mat = np.triu(df_voiture.corr())
sns.heatmap(df_voiture.corr(), vmin = -1, vmax = +1,  cmap = 'coolwarm', mask = upp_mat)
st.write(fig2)

st.write(' ')
st.write(' ')
st.write(' ')
#Distribution du poids des voitures selon la région
st.write("**Poids des voitures selon la région**")
st.write(' ')
st.write(' ')

st.write("Le poids des voitures est plus important au USA qu'en Europe et au Japon. Même si les valeurs minimales sont sensiblement les mêmes, les valeurs médianes et maximales sont elles très différentes.")
fig4 = px.box(df_voiture, x="continent", y = "weightlbs")
st.write(fig4)

#Calcul de la moyenne des variables par année
df_annee = df_voiture.groupby(['year','continent']).mean().reset_index()


df_annee2 = df_annee[df_annee['continent'] == continent]

#st.title = 'Europe'
st.write(' ')
st.write(' ')
st.write(' ')
st.write("**Evolution de la puissance des voitures en fonction des années**")
st.write(' ')
st.write(' ')

st.write("Le graphique ci dessous montre, pour la région sélectionnée, l'évolution de la puissance au fil des ans. La courbe est différente en fonction des régions. Néanmoins la tendance est à la baiise dès le début des années 80 pour chacunes d'entres elles." )
st.write('')
st.write("**Région sélectionnée : **" )
st.write(region)
fig5 = px.line(df_annee2, x="year", y="hp")
st.write(fig5)

