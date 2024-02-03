import pandas as pd

materias = ["Programacion", "Base de Datos", 
                "Calculo", "Inteligencia Artificial", "Estadistica"]
indices = ["A", "B", "C", "D", "E"]

# Series(data=[], index=[], dtype="str")
#serie = pd.Series(data=materias, index=indices, dtype="str")

#Serie a partir de un Diccionario

diccionario = {
    "Programacion": 100,
    "Base de Datos": 70,
    "Calculo": 81,
    "Inteligencia Artificial": 100,
    "Estadistica": 80
}

serie = pd.Series(diccionario)
print(serie,"\n")
print("-"*25)
print("Valor de la Serie:", serie.size)
print("Indices:", serie.index)
print("Tipo de Dato de la Serie:", serie.dtype)
print("-"*25)

#Accesar a los elementos de la Serie
print("\n",serie[0]) #Valor que contiene ese indice

print("-"*25)
print("Accesar a los elementos desde Programacion hasta Calculo \n")
print(serie[0:3])

#Accesar por clave = valor de la clave
print("-"*25)
print(serie["Programacion"])

#Accesar por clave en una lista
print("-"*25)
print(serie[["Programacion", "Calculo"]])

# Metodos que proporciona las Series
print("\n", "-"*25, "\n")
print(serie.count()) # Devuelve 5 elementos ya que ninguno es null
print(serie.sum()) # Suma los valores de la Serie
print("\n")
print(serie.cumsum()) # Valores acumulados de la serie

print("\n")
print(serie.value_counts()) # Valores unicos y cuantas veces se repiten

print("\n")
print(serie.min()) # Valor minimo de la Serie
print("\n")
print(serie.max()) # Valor maximo de la Serie
print("\n")
print(serie.mean()) # Valor media de la Serie

print("\n")
print(serie.std()) # Valor de desviacion tipica

print("\n", "-"*25, "\n")
print(serie.describe()) # Resumen de la Serie

