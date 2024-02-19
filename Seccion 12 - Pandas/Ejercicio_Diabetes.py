import pandas as pd

# Creando dataframe a partir de el archivo diavetes.csv
dataframe = pd.read_csv("Seccion 12 - Pandas\diabetes.csv")
print(len(dataframe)) # Elementos del Dataframe

print("\n", "*"*25)

# Definir columnas del Dataframe a una variable
print("Columnas del DataFrame:")
columnas = dataframe.columns
print(columnas)

# Valores de Glucosa
print("\n", "*"*25)
print("Valores de Glucosa:", dataframe.Glucosa)

# Obtener cuantas personas tienen diabetes
print("\n", "*"*25)
print("Personas con Diabetes:")
print(dataframe.Resultado.value_counts())
print("\n", "*"*25)

# 10 personas con mayor IMC
print("\n", "*"*25)
print("Personas con mayor Indice de Masa Corporal:")
print(dataframe.BMI.sort_values(ascending=False).head(10))

# Cantidad de Todas las edades que tienen Diabetes
print("\n", "*"*25)
print("Edades que tienen Diabetes:")
cant_personas = dataframe["Edad"].where(dataframe["Resultado"] == 1).dropna().value_counts()

# Para pbtener las personas sin Diabetes hay que cambiar el valor de 1 a 0 en ["Resultado"]
# cant_personas = dataframe["Edad"].where(dataframe["Resultado"] == 0).dropna().value_counts()

print(cant_personas)

# Crear Dataframe
cant_personas_df = pd.DataFrame({
    "Edades": cant_personas.index,
    "Cantidad": cant_personas.values
})

print("\n", "*"*25)
print(cant_personas_df)
