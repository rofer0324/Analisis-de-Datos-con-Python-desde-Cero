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

print(dataframe.info())
#print(dataframe.describe()) # Data adicional sobre el dataframe