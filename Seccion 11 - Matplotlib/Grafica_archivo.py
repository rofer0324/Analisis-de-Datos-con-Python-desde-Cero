import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

try:
    with open("Seccion 11 - Matplotlib\Files\Data", "r") as file:
        for line in file:
            datos = line.split()
            datos_completo = [float(dato) for dato in datos]
            
            x.append(datos_completo[0])
            y.append(datos_completo[1])
except:
    pass

print(x)
print(y)

plt.plot(x, y)
plt.show()