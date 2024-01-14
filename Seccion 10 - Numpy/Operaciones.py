import numpy as np

a = np.array([40, 50, 60, 70])
b = np.arange(4)

print(a, "Matriz A\n")
print(b, "Matriz B\n")

print("-"*20)
print(a+b, "SUMA")
print("-"*20)
print(a-b, "RESTA")
print("-"*20)
print(a*b, "MULTIPLICACION")
print("-"*20)

print(a > 35)

#producto de 2 matrices
print(a.dot(b))

########################################
print()
print("-"*20)
m1 = np.random.randint(0, 10, (3,3))
print(m1)

print(m1.sum(), "<- Suma de todos los elementos de la matriz")
print(m1.min(), "<- Valor minimo de la matriz")
print(m1.max(), "<- Valor maximo de la matriz")

print("-"*20)
print()
print(m1.cumsum(axis=0), "<- Suma acumulada por eje")
