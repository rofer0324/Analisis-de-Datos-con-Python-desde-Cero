import pandas as pd
import math
import numpy as np

diccionario = {
    "Programacion": 100,
    "Base de Datos": 70,
    "Calculo": 81,
    "Inteligencia Artificial": 100,
    "Estadistica": 80,
    "Ingles": np.NAN, # Para valor desconocido
    "Mecanica": None  # Null
    
}

serie2 = pd.Series(["amigo", "b", "c", "d"])

serie = pd.Series(diccionario)
#print(serie,"\n")

# Se puede sumar, restar, multiplicar, dividir 
# y modulo a los valores de la serie

print(serie + 2)


print("\n", serie2 * 5)

# Funciones Trigonometricas a las series
print("\n", "-"*25)
print(serie.apply(math.sin))

# Aplicar que las iniciales de cada palabra
# comiencen con mayusculas
print("\n", "-"*25)
print(serie2.apply(str.capitalize))

# Aplicar un condicional a las series
print("\n", "-"*25)
print(serie[serie > 80])

# Ordenar serie ascendente o descendente
print("\n", "-"*25)
print(serie.sort_values(ascending=True)) # Para Valores
#print(serie.sort_index(ascending=True)) # Para Indices

# Para eliminar valores nulos
print("\n", "-"*25)
print(serie.dropna())