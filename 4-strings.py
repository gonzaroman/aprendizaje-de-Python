miNombre = "Gonza"

print ("me llamo " + miNombre)
print (f"me llamo  {miNombre}")

print ("me llamo {0}".format(miNombre))


mystr = "hola mundo para hacer pruebas con el texto"



print(dir(mystr)) #obtener metodos y propiedades que podemos utilizar con mystr

#imprime esto:
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print(mystr.upper())

print(mystr.lower())

print(mystr.swapcase())

print(mystr.capitalize())

print(mystr.replace('hola','texto remplazado'))



print(mystr.count('mundo')) #cuenta las veces que aparece la palabra mundo
print(mystr.count('a')) #cuenta las veces que aparece la letra a


print(mystr.startswith('hola')) #devuelve true si el string empieza por hola

print(mystr.endswith('text')) #devuelve true si el string termina con 'texto'

print(mystr.split()) #hace una lista separando las palabras

print(mystr.split( 'a ')) #hace una lista separando por la letra a


print(mystr.find('m')) #devuelve  la posicion de la letra m, empieza en 0,1,2...

print(len(mystr) ) #devuelve el tamaño de la cadena mystr

print(mystr.index('e')) #devuelve el indice de la letra e

print(mystr.isnumeric() )

print(mystr[4])
print(mystr[-3])