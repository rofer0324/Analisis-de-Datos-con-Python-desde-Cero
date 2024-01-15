"""
1. Crea una Matriz de dos dimensiones de cualquier tamaño que 
contenga 'unos' en todos los bordes y en el interior 'ceros'.
"""

import numpy as np

matriz = np.ones((4,4))
#print(matriz)

#Desde el indice 1 hasta el penultimo indice
matriz[1:-1, 1:-1] = 0
print(matriz)