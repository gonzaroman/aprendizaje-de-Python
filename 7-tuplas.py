#las tuplas a diferencia de las listas no se pueden modificar
#son mas rapidas 

x=(1,2,3)

print(x)

meses=('enero','febrero','marzo')

#constructor

y=tuple((1,2,3))

print(y)

print(dir(y))

print(x[1])

del x #eliminamos la tupla x

print(x)


location = {
    (33.453322, 34,343434) : "tokyo",
    (45.432323, 45,676767) : "Madrid"
}