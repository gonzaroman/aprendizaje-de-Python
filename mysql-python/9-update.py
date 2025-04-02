import mysql.connector


mydb  = mysql.connector.connect(
    host="localhost", #el que uses
    user="root", #el que tengas, este es por defecto
    password="pleXusBD", #la que uses, esta es inventada
    database="mydatabase"
)


mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")