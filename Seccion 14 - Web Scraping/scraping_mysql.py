import mysql.connector
import pandas as pd

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user = "root",
    password = "password",
    host = "localhost",
    database = "scraping"   
)

# Cargar los datos del archivo: planetas.csv