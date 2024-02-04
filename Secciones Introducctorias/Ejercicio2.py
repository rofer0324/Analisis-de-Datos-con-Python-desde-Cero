# Escribe un programa que le pida al usuario un numero de horas de trabajo diarias y una tarifa por hora para
# calcular el salario. Imprimir el salario.

num_horas = int(input("Ingrese el numero de horas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

salario = num_horas * tarifa

print("El salario es: ", salario)