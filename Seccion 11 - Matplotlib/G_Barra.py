import matplotlib.pyplot as plt

alturas = [10, 20, 30, 40, 50]
x =  range(len(alturas))

plt.bar(x, alturas, width=0.5, color='green')
plt.title('Gráfico de barras')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# Para agregar codigo Latex es:
# plt.title(r"$\\frac{1}{4}$")