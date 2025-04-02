import mysql.connector

print("Inicio del script")
mydb  = mysql.connector.connect(
    host="localhost", #el que uses
    user="root", #el que tengas, este es por defecto
    password="pleXusBD" #la que uses, esta es inventada
)
print("Conexión establecida")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

print("bd creada")


mydb.close()