import pandas as pd

archivo = "Seccion 12 - Pandas\Alumnos.csv"
dataframe = pd.read_csv(archivo, sep=",", decimal=".")
print(dataframe)
print("\n", "*"*25)
print("Cabecera del dataframe") # 5 Primeros registros
print("\n", dataframe.head())

# Para exportar el dataframe a un archivo csv
dataframe.to_csv("Seccion 12 - Pandas\Alumnos2.csv", index=True, sep=",", decimal=",")


# Crear Dataframe a partir de un archivo Excel
print("\n", "*"*25)
archivo_excel = "Seccion 12 - Pandas\Alumnos.xlsx"
dataframe2 = pd.read_excel(archivo_excel, decimal=".")
print(dataframe2)

# Para exportar dataframe a un archivo Excel
dataframe2.to_excel("Seccion 12 - Pandas\Alumnos2.xlsx", index=True)

