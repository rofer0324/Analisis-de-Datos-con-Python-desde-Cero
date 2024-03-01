import mysql.connector
import pandas as pd
import requests

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user = "root",
    password = "password",
    host = "localhost",
    database = "scraping"  
)

# Cargar los datos del archivo: planetas.csv a la tabla planetas de la base de datos scraping
dataframe = pd.read_csv("Seccion 14 - Web Scraping\planetas.csv")
print(dataframe)

sql = "INSERT INTO planetas (satelite, planeta, diametro, periodo_orbital, imagen) VALUES (%s, %s, %s, %s, %s)"
cursor = conexion.cursor()

for planeta in dataframe.values:
    planeta = list(planeta) # Debe ser una lista
    print(f"Guardando datos de: {planeta[0]}")
    print(planeta[4])
    planeta[4] = requests.get(planeta[4]).content # Guarda en la DBA el contenido en ese indice que son las imagenes
    cursor.execute(sql, planeta)
    
conexion.commit()
cursor.close()
conexion.close()