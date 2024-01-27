import matplotlib.pyplot as plt
import numpy as np

# Barras Verticales
"""altura = [5, 10, 15, 20, 30]
x = range(len(altura))

plt.bar(x, altura, width=1)
plt.show()"""

# Barras Horizontales
"""ancho = [5, 10, 15, 20, 30]
y = range(len(ancho))

plt.barh(y, ancho, height=1, color='orange')
plt.show()"""

# Barras Multiples
"""barra_verde = [5, 10, 30, 40]
barra_rojo = [4, 8, 12, 24]
barra_naranja = [28, 7, 12, 18]

x = np.arange(0, 4)

plt.bar(x, barra_verde, color='green', width=0.25)
plt.bar(x + 0.25, barra_rojo, color='red', width=0.25)
plt.bar(x + 0.50, barra_naranja, color='orange', width=0.25)
plt.show()"""

# Barras Apiladas

alturas_a = [5, 10, 15, 20]
alturas_b = [10, 15, 5, 3]

x = range(0 ,4)
plt.bar(x, alturas_a, color='green', width=0.5)
plt.bar(x, alturas_b, color='blue', width=0.5, bottom=alturas_a)
plt.show()


