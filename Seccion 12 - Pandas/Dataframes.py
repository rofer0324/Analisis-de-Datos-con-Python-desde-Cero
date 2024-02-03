import pandas as pd

# Estructura para el Data Frame
# pd.DataFrame(data, index, columns, dtype)

diccionario = {
    "Nombre": ["Juan", "Ana", "Jose", "Arturo"],
    "Edad": [25, 18, 23, 27],
    "Estatura": [1.75, 1.60, 1.82, 1.70]
    
}

dframe = pd.DataFrame(diccionario)
print(dframe)

# Data frame a partir de Lista de Lista
print("\n","-"*25)
lista_persona = [["Jose", 23, 1.82], ["Ana", 18, 1.60], ["Arturo", 27, 1.70], ["Juan", 25, 1.75], ["Maria", 35], []]
data_frame2 = pd.DataFrame(lista_persona, columns=["Nombre", "Edad", "Estatura"])
print(data_frame2)

# Lista de Diccionarios
print("\n","-"*25)
diccionario_persona = [
    {"Nombre": "Jose", "Edad": 23, "Estatura": 1.82},
    {"Nombre": "Ana", "Edad": 18, "Estatura": 1.60},
    {"Nombre": "Arturo", "Edad": 27, "Estatura": 1.70},
    {"Nombre": "Juan", "Edad": 25, "Estatura": 1.75},
    {"Nombre": "Maria", "Edad": 35, "Estatura": 1.65},
    {"Nombre": "Alberto", "Estatura": 1.70}
]

data_frame3 = pd.DataFrame(diccionario_persona)
print(data_frame3)