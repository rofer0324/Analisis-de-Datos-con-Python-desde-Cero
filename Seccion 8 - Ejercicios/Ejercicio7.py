"""
1. Imprime las siguientes variables en una sola linea:
    x = 10, y = 50, z = 70
2. Ahora modifica el comando anterior para que el resultado se muestre separado por comas
    10, 50, 70
3. Ahora modifica el comando anterior para que el resultado se muestre separado por el signo de suma
    10 + 50 + 70
4. Por ultimo modifica el comando para que se añada el signo de igual al final
"""

x = 10
y = 50
z = 70

print(x, y, z)
print(x, y, z, sep = ", ")
print(x, y, z, sep = " + ")
print(x, y, z, sep = " + ", end = " =")