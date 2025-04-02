import mysql.connector


mydb  = mysql.connector.connect(
    host="localhost", #el que uses
    user="root", #el que tengas, este es por defecto
    password="pleXusBD", #la que uses, esta es inventada
    database="mydatabase"
)


mycursor = mydb.cursor()


sql = "DROP TABLE customers"

mycursor.execute(sql)