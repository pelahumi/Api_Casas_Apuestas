# Análisis
Pincha [aquí](https://github.com/pelahumi/Api_Casas_Apuestas) para acceder a mi repositorio.

## Equipos.csv
En este csv tenemos datos de la puntuación, nacionalidad y escudo de 32 equipos de fútbol diferentes. Para empezar el análisis, primero leemos el csv, además añadimos nombre a cada columna para una mayor comprensión:

```
columns = ['nombre', 'escudo', 'pais', 'puntuacion']
equipos = pd.read_csv('docs/equipo.csv', names=columns)
```

Una vez leído el csv ya podemos visualizar los datos en forma de tabla. Si nos fijamos, vemos que la columna de escudos almacena fotos de escudos de los equipos, por lo que es una columna de la que podemos prescindir ya que no nos proporciona ningún tipo de información útil.

```
equipos = equipos.drop('escudo', axis=1)
```

Ahora es importante ver si tenemos algún valor nulo en alguna de las columnas, para ello ejecutamos:

```
nulos = equipos.isnull().sum()
```

Vemos que no hay ningún valor nulo en ninguna de las columnas. 

También vemos si hay algún valor "outlier" visualizando gráficamente el diagrama de cajas:

![bigotes](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/df2cc0d8-0e21-463a-8791-4fd742461431)


Calculamos los datos descriptivos:

```
desc = equipos.describe()
```

<img width="154" alt="desc" src="https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/04557159-6fd2-46b9-988a-8a53515564b4">

Y graficamos los datos:

![bar1](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/9d7ecfad-beb9-469a-addd-0a23297ec4b9)

![bar2](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/721fc2ae-6ae7-48dd-b0f1-8d8dcccb87ab)

![bar3](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/369203f4-429f-471c-9128-28cf96eab862)

Vemos las distribuciones de la puntuación:

![distribucion1](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/1a9879f5-8c34-45ab-be65-572df01232a7)

![distribucion2](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/15473304-2daa-416a-9aa0-36fa06c16a70)

Por último, para ver si merece la pena hacer una regresión lineal veremos los scatter plots y ver así las relaciones entre las variables dependientes y la dependiente, que en este caso es la puntuación de cada equipo.

![scatter1](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/7551b522-b8bd-4481-b739-9253b8937215)

![scatter2](https://github.com/pelahumi/Api_Casas_Apuestas/assets/91721764/52cfb38e-70c0-413c-af6b-742166ad5319)

Como vemos, no hay ningún patrón en los scatter plots que nos indique que debemos hacer una regresión lineal.

