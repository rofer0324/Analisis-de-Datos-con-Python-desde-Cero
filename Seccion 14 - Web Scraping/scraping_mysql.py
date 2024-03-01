import mysql.connector
import pandas as pd

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

sql = "INSERT INTO planetas (satelite, planeta, diametro, periodo_orbital) VALUES (%s, %s, %s, %s)"
cursor = conexion.cursor()

for planeta in dataframe.values:
    planeta = list(planeta) # Debe ser una lista
    cursor.execute(sql, planeta)
    
conexion.commit()
cursor.close()
conexion.close()