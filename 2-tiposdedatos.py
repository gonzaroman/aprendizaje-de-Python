#cadena string
print("hola mundo")
print('hola mundo con comilla simple')
print("""hola mundo con comillas triples""")
#imprimir el tipo de dato
print(type("hola mundo"))



#concatenar +
print("hola"+" mundo"+" amigos")

#numeros int
print(34)

print(type(34))

#decimal float
print(34.5)

print(type(34.5))

#boolean

print(True)
print(False)

print(type(True))


#listas pueden almacenar un solo tipo o varios

[10, 20, 55, 89]
['hola','hello','saludo']
[10, 'helo', True, 20.1]
[]#vacia


print([10, 'helo', True, 20.1])
print(type([10, 'helo', True, 20.1]))



#Tuplas, son como las listas pero con parentesis, pero los datos no se pueden cambiar despues
#son inmutables
(10, 20, 67, 101)

print((10, 20, 67, 101))

print(type((10, 20, 67, 101)))


#diccionarios clave valor: Key Value
{
    "nombre": "Jose",
    "apellido": "Garcia",
    "edad" : 89
}
print(
    type(
        {
        "nombre": "Jose",
        "apellido": "Garcia",
        "edad" : 89
        }
    )
)

#tipo nontype

print(type(None))