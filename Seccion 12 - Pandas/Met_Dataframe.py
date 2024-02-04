import pandas as pd

dataframe = pd.read_csv("Seccion 12 - Pandas\Alumnos.csv", sep=",", decimal=".")

# Obtener informacion del Dataframe
print(dataframe.info())

# Obtener Tuplas y numero de filas de Dataframe
print("\n", "*"*25)
print(dataframe.shape)

# Numero de elementos que contiene el Dataframe
print("\n", "*"*25)
print(dataframe.size)

# Nombres de todas las columnas del Dataframe
print("\n", "*"*25)
print(dataframe.columns)

# Nombre de todas las filas del Dataframe
print("\n", "*"*25)
print(dataframe.index)

# Tipos de datos de las columnas del Dataframe
print("\n", "*"*25)
print(dataframe.dtypes)

# Obtener un filtro de X indice del Dataframe
print("\n", "*"*25)
print(dataframe.iloc[3])