import pandas as pd

materias = ["Programacion", "Base de Datos", 
                "Calculo", "Inteligencia Artificial", "Estadistica"]
indices = ["A", "B", "C", "D", "E"]

# Series(data=[], index=[], dtype="str")
#serie = pd.Series(data=materias, index=indices, dtype="str")

#Serie a partir de un Diccionario

Diccionario = {
    "Programacion": 100,
    "Base de Datos": 70,
    "Calculo": 81,
    "Inteligencia Artificial": 100,
    "Estadistica": 80
}

serie = pd.Series(Diccionario)
print(serie,"\n")
print("-"*25)
print("Valor de la Serie:", serie.size)
print("Indices:", serie.index)
print("Tipo de Dato de la Serie:", serie.dtype)
