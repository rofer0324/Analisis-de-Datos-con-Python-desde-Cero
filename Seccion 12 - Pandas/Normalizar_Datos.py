import pandas as pd

dataframe = pd.read_csv("Seccion 12 - Pandas\Alumnos_index.csv")

df_normalizado = dataframe.melt( ["Id", "Nombres", "Sexo"],
                                ["Programacion", "BaseDatos", "Calculo", "Valores", "Ingles"],
                                "Materias",
                                "Calificacion")

print(df_normalizado)

# Tabla Pivote
print("\n", "*"*25)
df_pivote = df_normalizado.pivot("Id", "Materias", "Calificacion")
print(df_pivote)