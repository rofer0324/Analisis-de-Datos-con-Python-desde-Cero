import pandas as pd
import numpy as np

columnas = ["Alimentos", "Cantidad", "Minutos"]

# Numeros Random del 1 al 3 y que sean 5000 elementos
alimentos = np.random.randint(1, 4, (5000, ))

cantidad = np.random.randint(1, 11, (5000, ))

minutos = np.ones((5000, ))

dataframe = pd.DataFrame((alimentos, cantidad, minutos))
dataframe = dataframe.T # Transponer el Dataframe para que sean 5mil filas y 3 columnas
#print(dataframe)

# Aplicando Columnas al Dataframe
dataframe.columns = columnas
print(dataframe)

####--- Creando tiempos de preparacion ---####

# este código está multiplicando los valores en la columna "Minutos" por tres, pero solo para las filas donde el valor en la columna "Alimentos" es igual a 1.
dataframe["Minutos"] = dataframe["Minutos"].where(dataframe.loc[ : , "Alimentos"] == 1) * (dataframe["Cantidad"] * 3)

# reemplazando los valores nulos en la columna "Minutos" por cuatro veces el valor correspondiente en la columna "Cantidad", pero solo 
# para las filas donde el valor en la columna "Alimentos" es igual a 2.
dataframe["Minutos"][ (dataframe["Minutos"].isnull()) & (dataframe["Alimentos"] == 2)] = \
    dataframe["Cantidad"][dataframe["Alimentos"] == 2] * 4

# reemplazando los valores nulos en la columna "Minutos" por seis veces el valor correspondiente en la columna "Cantidad", pero solo 
# para las filas donde el valor en la columna "Alimentos" es igual a 3.
dataframe["Minutos"][ (dataframe["Minutos"].isnull()) & (dataframe["Alimentos"] == 3)] = \
    dataframe["Cantidad"][dataframe["Alimentos"] == 3] * 6


# Crear el archivo csv sin indices
dataframe.to_csv("DataSet_custom.csv", index=False)