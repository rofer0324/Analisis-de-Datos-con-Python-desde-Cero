import pandas as pd
import math

dataframe = pd.read_csv("Seccion 12 - Pandas\Alumnos.csv", sep=",", decimal=".")
#print(dataframe)

lista = [100,69,31,46,57,68,74,89,90]
dataframe["Peso"] = lista

# Tambien se puede agregar esta columna a travez de una serie.
#serie = ([100,69,31,46,57,68,74,89,90])
"""
En el caso de que haga falta un valor, la serie agregara el valor faltante como 
"""
#dataframe["Peso"] = serie

dataframe["Estatura"]  = dataframe["Estatura"] * 100 # Para que salga la estatura en cm.
print(dataframe)

# Aplicar funciones a las columnas
print("\n", "*"*25)
print(dataframe["Valores"].apply(math.cos))

# Eliminar Columnas de un Dataframe
print("\n", "*"*25)
del dataframe["Nombres"]
print(dataframe)

# Se puede eliminar una columna y almacenar esos valores en una variable[Lista]
print("\n", "*"*25)
valores = dataframe.pop("Valores")
print(valores)