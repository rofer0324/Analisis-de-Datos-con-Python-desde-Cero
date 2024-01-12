"""
1. Muestra la pregunta ¿Cual es tu nombre? al usuario y almacena el valor en la variable nombre
2. Guarda la primera letra del contenido de la variable "nombre" dentro de la variable inicial
3. Dada la variable "nombre_completo" = 'Gregory Martinez Aguilar' copia solo el apellido "Martinez" en
    en una variable de diferente nombre
"""

nombre = input("Cual es tu nombre: ")
nombre = nombre[0]
print(nombre)
nombre_completo = 'Gregory Martinez Aguilar'
apellido = nombre_completo[8:16]
print(apellido)