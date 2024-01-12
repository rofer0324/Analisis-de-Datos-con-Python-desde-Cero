"""
1. Crea una lista de colores rojo, verde y azul y almacenalo en una lista llamada "colores"
2. Muestra los colores en la salida estandar
3. Modifica el codigo para que ahora solo muestre el segundo elemento de la lista (verde) que has creado.
4. Cambia el primer color rojo por el color rosa en la lista
5. Elimina la tercera entrada de la lista
6. Ahora añade el color morado al final de la lista
7. Por ultimo, añade el color amarillo en la primera posicion (indice 0)
"""

colores = ["rojo", "verde", "azul"]
print(colores)
print(colores[1])

colores[0] = "rosa"

del colores[2]

colores.append("morado")
colores.insert(0, "amarillo")

print(colores)
