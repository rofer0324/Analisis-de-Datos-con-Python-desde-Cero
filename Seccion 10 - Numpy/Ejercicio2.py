"""
2. Crea una matriz unidimencional con 20 numeros aleatorios que se encuentren
en un rango del 0 al 5 y que sean enteros.

- Imprimir todos los indices que contengan un numero diferente a 0.
"""

import numpy as np

matriz_unidimencional = np.random.randint(0, 5, 20)
print(matriz_unidimencional)
print("-"*25)
print(np.argwhere(matriz_unidimencional))