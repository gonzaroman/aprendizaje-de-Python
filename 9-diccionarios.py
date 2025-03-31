#clave valor key value
producto = {
    "nombre": "libro",
    "cantidad": 3,
    "precio": 4.99
}

persona = {
    "nombre":"juan",
    "apellido": "garcia",
    "edad": 59
}

print(type(producto))

#metodos
print(dir(persona))


print(persona.keys())

print(persona.items())

persona.clear()

print(persona)


del persona


listaProductos = [
    {"name":"libro", "precio":4.66},
    {"name":"PC", "precio":1200},

]

print(listaProductos)