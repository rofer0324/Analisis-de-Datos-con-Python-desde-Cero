import pandas as pd
import numpy as np

datos = pd.read_csv("Seccion 12 - Pandas\Alumnos_index.csv")

print( datos.groupby(["Sexo", "Edad"]).groups )

# DataFrame de Datos agrupados de Hombres
print("\n", "*"*25)
df_hombres = datos.groupby(["Sexo"]).get_group("M")
print(df_hombres)

# DataFrame de Datos agrupados de Hombres
print("\n", "*"*25)
df_mujeres = datos.groupby(["Sexo"]).get_group("F")
print(df_mujeres)

# Valores minimos de cada columna
print("\n", "*"*25)
valores_min = datos.groupby(["Sexo"]).agg(np.min) 
print(valores_min)