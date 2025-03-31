demoLista = [1, 'hola', 1.34, True, [1,2,3]]

colores = ['rojo', 'verde','azul']

#constructor de lista

listaNumeros = list((1,2,3,4))

print(listaNumeros)

print(type(listaNumeros))

listaGenerada = list(range(1,10))
print(listaGenerada)

print(dir(colores)) #mostramos metodos aplicables a la lista colores

print(len(colores))
print(colores[1]) #devuelve verde

print(colores[-2]) #devuelve desde la ultima

print('verde' in colores) #True si está en la  lista colores

print('amarillo' in colores) #false

print("***********")
print(colores)
colores[1]='amarillo'
print(colores)

#insertamos
colores.append('granate')

print(colores)

colores.extend(['violeta', 'negro']) #agregar varios valores

print(colores)

colores.insert(2,'gris') #agrega en la posicion 2

print(colores)

colores.insert(-1, 'verdoso') #agrega en la posicion 1 desde el final

print(colores)

colores.insert(len(colores), "verde agua")

print(colores)

colores.pop() #elimina  el ultimo  elemento

print(colores)

colores.remove('granate') #elimina el color granate

print(colores)

colores.pop(3) #elimina el elemento 3

print(colores)

colores.sort() #ordear orden alfabetico

print(colores)

colores.sort(reverse=True) #ordear orden alfabetico a la  inversa

print(colores)

print(colores.index('verdoso')) #obtenemos el indice, posicion

colores.append('rojo')

print(colores.count('rojo')) #cuenta las veces que aparece el rojo

colores.clear() #vacia la lista

print(colores)