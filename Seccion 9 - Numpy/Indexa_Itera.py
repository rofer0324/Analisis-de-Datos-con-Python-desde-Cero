import numpy as np #cap 70.

matriz = np.arange(10)
print(matriz)

print(matriz[5]) #elemento en el indice 5

print(matriz[2:5]) #obtiene los elementos entre el indice 2 al 5

matriz[0:6:2] = 100 #cambia valores del 0 al 6 en pasos de 2
print(matriz)
print("-"*25)

matriz_seleccion = np.arange(16).reshape(4,4)
print(matriz_seleccion)
print("")
#Formas de seleccion para los elementos de las matrices
print(matriz_seleccion[ : ,0])
print("")
print(matriz_seleccion[0:2, : ])

####---- Iteraciones ----####
print("-"*25)
print("")
for fila in matriz_seleccion:
    print(fila, "FILA")

print("-"*25)
print("")
for fila in matriz_seleccion:
    for elemento in fila:
        print(elemento)

print("-"*25)
print("")

for elemento in matriz_seleccion.flat:
    print(elemento)