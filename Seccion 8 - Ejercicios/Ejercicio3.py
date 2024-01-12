"""
1. Escribe la palabra dinosaurio dentro de una variable llamada "animal"
2. Escribe la palabra verde dentro de una variable llamada "color"
3. Crea una variable llamada "combinado" donde se almacenen las dos variables anteriores: "animal" y "color"
    dando como resultado el valor dinosaurioverde.
4. En la variable "combinado" intercala un espacion en blanco para separar las dos palabras.
"""

animal = "dinosaurio"
color = "verde"

combinado = animal + color
print(combinado)

#combinado = animal + " " + color
print(f"{combinado} {color}")