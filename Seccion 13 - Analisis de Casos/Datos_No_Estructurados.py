import pandas as pd
import matplotlib.pyplot as plt
import requests

# Caso de Analisis de Datos no estructurados de las Peliculas mas Taquilleras del 2023.
# source: https://en.wikipedia.org/wiki/List_of_2023_box_office_number-one_films_in_the_United_States

url = "https://en.wikipedia.org/wiki/List_of_2023_box_office_number-one_films_in_the_United_States"

# Instancia del url
peticion = requests.get(url)
data = pd.read_html(peticion.text)
dataframe = data[0]

###--- Manipulacion de Datos ---###

# Elimino las columnas que no necesito
dataframe = dataframe.drop(['.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}#','Notes', 'Ref.'], axis=1)

# Elimino las Peliculas repetidas y me quedo con la ultima que ocupo el primer puesto hasta el fin de semana del año 2023.
dataframe = dataframe.drop_duplicates(subset='Film', keep='last')

# Eliminar caracteres innecesarios
dataframe["Gross"] = dataframe["Gross"].str.replace("\$", "").str.replace(",", "").astype("int64")

# Crear nueva columna para fecha
# Es transformado de esta manera ya que de la manera en la que se obtiene de la web, no se puede transformar directamente al formato.
dataframe["Weekend end date"] = pd.to_datetime(dataframe["Weekend end date"])

# Crear columna solamente para el numero de mes
dataframe["Month"] = pd.DatetimeIndex(dataframe["Weekend end date"]).month

print("\n", dataframe.head(5))
print("\n", dataframe.info())

print("\n", "*"*65)
df_1 = dataframe[ ["Film", "Gross"] ].sort_values(ascending=False, by="Gross")
print(df_1)

# Grafico 1 - Barra
print("\n", "*"*65)
plt.figure(figsize=(10, 5))
plt.bar(df_1["Film"].head(5), df_1["Gross"].head(5), color=['b', 'g', 'r', 'c', 'm', 'y'])
plt.title("Top 5 Peliculas por ingresos")
plt.xlabel("Peliculas")
plt.ylabel("Ingresos")
plt.xticks(rotation=10)
plt.show()

# Grafico 2 - Pastel
print("\n", "*"*65)
plt.figure(figsize=(10, 5))
plt.title("Top 10 Peliculas por ingresos")
plt.pie(df_1["Gross"].head(10), labels=df_1["Film"].head(10), autopct="%1.1f%%")
plt.show()

# Grafico 3
print("\n", "*"*65)
dt_2 = dataframe.groupby("Month")["Gross"].mean() # Se agrupa por mes y se obtiene la media de los ingresos
print(dt_2)
plt.figure(figsize=(10, 5))
plt.plot(dt_2)
plt.xlabel("Meses")
plt.ylabel("Media de Ingresos")
plt.show()


