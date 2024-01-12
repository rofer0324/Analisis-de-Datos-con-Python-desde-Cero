#Matriz 4x5 
import numpy as np

matriz = np.arange(20).reshape(4,5) #Fila x Columna
print(matriz)

print("\nNumero de ejes: ", matriz.ndim)
print("Forma de la matriz: ", matriz.shape)
print("Elementos de la matriz: ", matriz.size)
print("Tipo de elementos de la matriz: ", matriz.dtype)
print("Tamaño en bytes de la matriz: ", matriz.itemsize)

print("\n\n\n")
#Creacion de matrices.
a = np.array([1,2,3,4])
print(a,"Tipo:", a.dtype)
print()
b = np.array([1.1, 2.2, 3.3, 4.4])
print(b,"Tipo:", b.dtype)
print()
c = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #.array acepta como argumento (la lista de matriz, tipo de dato)
print(c, "Tipo:", c.dtype)

print()
#ejemplo
d = np.array([[1,2,3,4,5],[6,7,8,9,10]], dtype=complex) 
print(d, "Tipo:", d.dtype)
print()
print("-"*25)
print()

#### ---- Copiar matrices ---- ####
matriz_1 = np.arange(16).reshape(2, 8)
matriz_2 = matriz_1.copy()

print(matriz_1, "Matriz A")
print("-"*25)
print(matriz_2, "Matriz B")
print()
print(matriz_1 is matriz_2)
print()
matriz_2[0,1] = 3500
print(matriz_2)
print("-"*25)
print()

#Solo es copiado a la matriz 2, los elementos de la primera fila de la matriz 1
matriz_2 = matriz_1[0, : ].copy()
print(matriz_2)
