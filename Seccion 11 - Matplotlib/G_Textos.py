import matplotlib.pyplot as plt
import numpy as np

x = np.full(5, 5, dtype=int)
y = np.linspace(2, 10, 5)

plt.scatter(x, y)
plt.title("Ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Diccionario para la configuracion del cuadro
cuadro = {
    "facecolor": '0.50',
    "edgecolor": 'red',
    "boxstyle": 'round'
}

#Texto en la coordenada (5, 4)
plt.text(5, 4, "Segundo punto", horizontalalignment='center', bbox=cuadro)

#Exportar esta grafica a PNG.
plt.savefig("Grafico.png")
plt.show()