import numpy as np
import matplotlib.pyplot as plt

# 500 filas x 2 columnas
pts = np.random.rand(500, 2)

x = pts[:, 0]
y = pts[:, 1]

plt.scatter(x, y)
plt.show()
