import matplotlib.pyplot as plt
import numpy as np
import math

#x = range (0, 50)
#y = [valores ** 2 for valores in x]

"""
# Senoidal creada con libreria math
x = [16*val / 100 for val in range(100)]
#print(x)
y = [math.sin(val) for val in x]
#print(y)
"""

# Senoidal creada con libreria matplotlib
x = np.linspace(0, 16, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()