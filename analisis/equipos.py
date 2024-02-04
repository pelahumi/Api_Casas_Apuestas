import pandas as pd
import matplotlib.pyplot as plt

#Añadimos nombre de las columnas para mayor claridad
columns = ['nombre', 'escudo', 'pais', 'puntuacion']

#Leemos el csv
equipos = pd.read_csv('docs/equipo.csv', names=columns)

#Eliminamos la columna escudo que no nos interesa
equipos = equipos.drop('escudo', axis=1)

#Calculamos los datos descriptivos
desc = equipos.describe()

#Vemos si hay valores nulos
nulos = equipos.isnull().sum()
print(nulos)

"""#Outliers
equipos.boxplot(column='puntuacion')
plt.title('Boxplot de puntuacion')
plt.show()

#Hcemos un scatter plot para ver si hay alguna relacion entre nombre y puntuacion
equipos.plot.scatter(x='nombre', y='puntuacion')
plt.title('Scatter plot entre nombre y puntuacion')
plt.show()

#Hacemos scatter plot para ver si hay alguna relacion entre pais y puntuacion
equipos.plot.scatter(x='pais', y='puntuacion')
plt.title('Scatter plot entre pais y puntuacion')
plt.show()

#Vemos la distribucion de la puntuacion
equipos['puntuacion'].plot(kind='hist')
plt.title('Distribucion de la puntuacion')
plt.show()

#Vemos la distribucion de la puntuacion por pais
equipos['puntuacion'].hist(by=equipos['pais'])
plt.title('Distribucion de la puntuacion por pais')
plt.show()

"""

#Vemos cuanto equipos hay por pais
equipos['pais'].value_counts().plot(kind='bar')
plt.title('Equipos por pais')
plt.show()

#Vemos la puntuacion media por pais
equipos.groupby('pais')["puntuacion"].mean().plot(kind='bar')
plt.title('Puntuacion media por pais')
plt.show()

#Vemos la puntuacion maxima por pais
equipos.groupby('pais')["puntuacion"].max().plot(kind='bar')
plt.title('Puntuacion maxima por pais')
plt.show()



