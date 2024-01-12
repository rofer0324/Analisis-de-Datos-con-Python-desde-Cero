import numpy as np
import sys

matriz_nula = np.zeros((2,3))
#print(matriz_nula)

matriz_unos = np.ones((3,2,4))
# 3 matrices de unos 2x4
#print(matriz_unos)

matriz_vacia = np.empty((2,3))
# Al estar vacia contiene basura
#print(matriz_vacia)

matriz_rango = np.arange(0,10,2)
# inicie desde 0, finaliza en 10 y que vaya en pasos de 2
#print(matriz_rango)

a = np.linspace(0,10,5)
# a es una matriz, que contiene un rango de numeros de
# 0 a 10. el tercer argumento es la cantidad de elementos.
print(a)

#Impresion de matrices extensas
np.set_printoptions(threshold=sys.maxsize)
matriz = np.arange(2500).reshape(50,50)
print(matriz)

print("\n")
print("-"*20)
print("\n")
#Matrices Random

num_aleatorios = np.random.default_rng()

m1 = num_aleatorios.random((5,5))
print(m1)
print("-"*20)
m2 = np.random.random((5,5))
print(m2)
print("-"*20)

print(m2*10)
print("-"*20)

m3 = np.random.randint(10, 100, (4,4))
print(m3)



####---- Formas de la matriz ----####
matriz1 = np.arange(15).reshape(3,5)
print(matriz1, matriz1.shape)
print("-"*25)

#matriz transpuesta
matriz1 = matriz1.T
print(matriz1, matriz1.shape)
print("-"*25)

matriz2 = np.arange(16).reshape(4,4)
print(matriz2, "\n")
#Obtener una matriz unidimencional
print(matriz2.ravel())
print("-"*25)