import matplotlib.pyplot as plt
import numpy as np

# Se obtiene 5 numeros aleatorios para hacer la grafica.
data = np.random.rand(5)

plt.pie(data)
plt.show()