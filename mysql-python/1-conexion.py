import mysql.connector

print("Inicio del script")
mydb  = mysql.connector.connect(
    host="localhost", #el que uses
    user="root", #el que tengas, este es por defecto
    password="pleXusBD" #la que uses, esta es inventada
)
print("Conexión establecida")
print(mydb)
#mydb.close()
print("Fin del script")