import pandas as pd

dataframe = pd.read_csv("Seccion 12 - Pandas\Alumnos.csv")

#data = ["Roberto", 25, 1.85, 7.5, 8.4, 9.0, 10.0]
#dataframe.loc[9] =  data
#print(dataframe)

# Forma alternativa para agregar una fila al Data Frame
dataframe_aux = [
    {"Nombres": "Humberto"},
    {"Nombres": "Daniel", "Edad": 22, "Estatura": 1.69, "Programacion": 8.5, "Base de Datos": 9.0, "Calculo": 9.5, "Valores": 10.0},
    {}
]

dataframe = pd.concat([dataframe, pd.DataFrame(dataframe_aux)], ignore_index=True)
print(dataframe)

# Eliminar Filas de un Dataframe
print("\n", "*"*25)
dataframe = dataframe.drop([5])
print(dataframe)

# Eliminar Filas de un Dataframe con datos Null
print("\n", "*"*25)
print(dataframe.dropna(subset=["Nombres"])) # Elimina datos nulos con ese parametro "Nombres"

# Para eliminar en general las filas que tienen datos nulos
#print(dataframe.dropna())

# Filtrar filas por Condiciones
print("\n", "*"*25)
print( dataframe[ (dataframe["Edad"] >= 22) & (dataframe["Calculo"] >= 6) ] )