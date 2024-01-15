import matplotlib.pyplot as plt
import numpy as np

# Matriz Unidimencional de 0 a 15 con 200 elementos
x = np.linspace(0, 15, 200)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1) # Grafica la primera curva
plt.plot(x, y2) # Grafica la segunda curva
plt.show()