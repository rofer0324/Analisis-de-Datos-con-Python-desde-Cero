import matplotlib.pyplot as plt
import numpy as np

# Rango de edades de 18 a 32 años
# 50 edades

elementos = np.random.randint(18, 33, (50, ))

plt.hist(elementos, bins=range(18, 33))
plt.show()

# Contar cuantas personas tienen 18 años
for persona in elementos:
    if persona == 18:
        print(persona)
        