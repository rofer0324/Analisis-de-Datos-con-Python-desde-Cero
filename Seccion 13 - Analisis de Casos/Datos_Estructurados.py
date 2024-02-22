import pandas as pd
import matplotlib.pyplot as plt

# Caso de Analisis de Datos estructurados del numero reportado de casos de COVID-19 en el mundo.
# source: https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

url = "https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide"

pd.set_option('display.max_columns', None)

dataframe = pd.read_csv("Seccion 13 - Analisis de Casos\data.csv")


###--- Manipulacion de Datos ---###

# Cambiar tipo de dato de la fecha
dataframe["dateRep"] = pd.to_datetime(dataframe["dateRep"], format="%d/%m/%Y")

# Cambiar el nombre de las columnas a Español
columnas = ["Fecha", "Dia", "Mes", "Año", "Casos", "Muertes", "Pais", "Codigo_pais_dos_letras", "Codigo_pais", "Poblacion", "Continente", "Acumulativo"]
dataframe.columns = columnas

# Eliminando columnas innecesarias
dataframe = dataframe.drop(["Codigo_pais_dos_letras", "Acumulativo"], axis=1)

# Comprobar si existen valores null en el dataframe
print(dataframe.isna().sum().sum())
dataframe.dropna(inplace=True) # Se eliminan los valores null

# Agrupar por pais y obtener el total de casos y muertes
print("\n", "*"*65)
df_pais = dataframe.groupby("Pais")[["Casos", "Muertes"]].sum()
df_pais["Relacion_Mortalidad"] = (df_pais["Muertes"] / df_pais["Casos"]) * 100
print(df_pais)

#print(dataframe.info())
#print(dataframe.describe()) # Data adicional sobre el dataframe

###--- Visualizacion de la Data ---###

# Grafico 1 - Barra
print("\n", "*"*65)
data = df_pais["Relacion_Mortalidad"].sort_values(ascending=False).head(15)
plt.figure(figsize=(10, 5))
plt.bar(data.index, data)
plt.title("Top 15 Paises con mas casos de COVID-19")
plt.xlabel("Paises")
plt.ylabel("Tasa de Mortalidad")
plt.xticks(rotation=70)
plt.show()

# Grafico 2 - Pastel
print("\n", "*"*65)
data = df_pais["Casos"].sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.title("Top 10 Paises con mas casos de COVID-19")
plt.pie(data, labels=data.index, autopct="%1.1f%%")
plt.show()

# Grafico 3 - 10 paises con mas perdidas humanas
print("\n", "*"*65)
data = df_pais["Muertes"].sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.title("Top 10 Paises con mas muertes por COVID-19")
plt.bar(data.index, data)
plt.xlabel("Paises")
plt.ylabel("Muertes")
plt.xticks(rotation=70)
plt.show()

# Grafico 4

# Agrupando Datos por mes
print("\n", "*"*65)
df_mes = dataframe.groupby("Mes")[["Casos", "Muertes"]].sum()
print(df_mes)
figura = plt.figure(figsize=(10, 10))
g1 = figura.add_subplot(1, 2, 1)
g2 = figura.add_subplot(1, 2, 2)

g1.plot(df_mes["Casos"], marker="o", color="r")
g1.set_title("Total de Casos por Mes en 2020")
g1.set_xlabel("Mes")
g1.set_ylabel("Casos")

g2.plot(df_mes["Muertes"], marker="o", color="b")
g2.set_title("Total de Muertes por Mes en 2020")
g2.set_xlabel("Mes")
g2.set_ylabel("Muertes")
plt.show()

# Grafico 5

# Panamá
print("\n", "*"*65)
df_panama = dataframe[dataframe["Pais"] == "Panama"]

df_panama = df_panama.groupby("Mes")["Casos"].sum() # Agrupar por mes y sumar los casos
df_panama = df_panama.reset_index() # Se convierte la serie en un dataframe
print(df_panama)

# Alemania
print("\n", "*"*65)
df_alemania = dataframe[dataframe["Pais"] == "Germany"]

df_alemania = df_alemania.groupby("Mes")["Casos"].sum() # Agrupar por mes y sumar los casos
df_alemania = df_alemania.reset_index() # Se convierte la serie en un dataframe
print(df_alemania)

figura = plt.figure(figsize=(12, 12))
g1 = figura.add_subplot(1, 2, 1)
g2 = figura.add_subplot(1, 2, 2)

g1.plot(df_panama["Mes"], df_panama["Casos"], marker="o", color="r")
g1.set_title("Total de Casos por Mes en Panamá")

g2.plot(df_alemania["Mes"], df_alemania["Casos"], marker="o", color="b")
g2.set_title("Total de Casos por Mes en Alemania")
plt.show()

"""
Observaciones:
- La tasa de mortalidad en los paises con mas casos de COVID-19 es muy variable.
- Mayor tasa de mortalidad: Yemen, Mexico, Sudan, Syria, Egypt, etc.
- Mayor cantidad de casos: USA, India, Brazil, Russia, France, etc.
- Mayor cantidad de muertes: USA, Brazil, India, Mexico, UK, etc.
- En el mes de Julio se observa un pico en la cantidad de casos y muertes.

- En Panamá, la cantidad de casos ha ido en aumento desde el mes de Marzo.
- En Alemania, la cantidad de casos ha ido en aumento desde el mes de Marzo.

    En Panamá y Alemania, como paises de muestra para el analisis, se observo que al implementar los cierres, 
    la cantidad de casos disminuyo Panamá[Julio] y Alemania[Marzo], pero al relajar las medidas, la cantidad de casos volvio a aumentar.
"""

