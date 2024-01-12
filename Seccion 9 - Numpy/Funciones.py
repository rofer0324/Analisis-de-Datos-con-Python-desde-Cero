import numpy as np

x = 100
raiz = np.sqrt(x)
seno = np.sin(x)
coseno = np.cos(x)

arcsen = np.arcsin(1)
arctan = np.arctan(1)

print("Raiz: ", raiz)
print("seno: ", seno)
print("coseno: ", coseno)
print("arcsen: ", arcsen)
print("arctan: ", arctan)
print("-"*25)

matriz = np.arange(0,5)
print(matriz, matriz.dtype)
print("-"*25)

matriz_b = np.sqrt(matriz) #Obtener raiz de una matriz
print(matriz_b, matriz_b.dtype)
print("-"*25)

matriz_c = np.array([90, 180, 270, 360])
print(matriz_c)
matriz_d = np.deg2rad(matriz_c) #Convertir a radianes
print(matriz_d)


