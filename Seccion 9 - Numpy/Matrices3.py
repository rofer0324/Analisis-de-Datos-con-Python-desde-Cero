# Guardar y cargar matrices

import numpy as np

# Se comentaron estas lineas para hacer pruebas con las matrices b y c
"""# 16 elementos, 4x4
matriz = np.arange(16).reshape(4,4)

# Ruta/nombre de la matriz , variable de la matriz
np.save("Seccion 9 - Numpy/Matriz4x4", matriz)"""

# Cargar matriz
matrizb = np.load("Seccion 9 - Numpy/Matriz4x4.npy")
print(matrizb)
print("-"*15)

# Se modifica los valores de matrizb sin afectar la matriz original que fue cargada (matriz)

matrizc = np.load("Seccion 9 - Numpy/Matriz4x4.npy")
matrizc[0,0] = 1000
print(matrizc)
