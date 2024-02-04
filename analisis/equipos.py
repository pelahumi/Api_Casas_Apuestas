import pandas as pd
import matplotlib.pyplot as plt

#Añadimos nombre de las columnas
columns = ['nombre', 'escudo', 'pais', 'puntuacion']

#Leemos el csv
equipos = pd.read_csv('docs/equipo.csv', names=columns)

#Mostramos los primeros 5 registros
print(equipos.head())

#Eliminamos la columna escudo que no nos interesa
equipos = equipos.drop('escudo', axis=1)

#Mostramos gráfica de barras
equipos.plot(kind='bar', x='nombre', y='puntuacion')
plt.show()

#Mostramos gráfica de pastel
equipos.plot(kind='pie', y='puntuacion', labels=equipos['nombre'])
plt.show()

#Hacemos una relación de los equipos por país
equipos_por_pais = equipos['pais'].value_counts()
print(equipos_por_pais)
