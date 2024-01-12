#  3x + 5y      = 1
#  2x + 4y + 6z = 3
#  1x +    + 5z = 6

import numpy as np

incongnitas = np.array( [ [3, 5, 0], [2, 4, 6], [1, 0, 5] ] )
constantes = np.array( [1, 3, 6] )

resultados = np.linalg.solve(incongnitas, constantes)

Lista_incognitas = ["x", "y", "z"]

for letra in range(len(resultados)):
    print(f"{Lista_incognitas[letra]}: {resultados[letra]}")