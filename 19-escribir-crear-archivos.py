f = open("archivo2.txt", "a")
f.write("añadimos esta  linea al contenido")
f.write("añadimos otra linea al contenido")
f.close()

f = open("archivo2.txt", "r")
print(f.read())
f.close()

f = open("archivo2.txt", "w")
f.write("Hemos borrado el contenido")
f.close()

f = open("archivo2.txt", "r")
print(f.read())
f.close()

import os
os.remove("archivo2.txt")

#comprobamos si el archivo existe para borrarlo, en caso contrario muestra mensaje:
if os.path.exists("archivo2.txt"):
  os.remove("archivo2.txt")
else:
  print("el archivo no existe")

#crea una carpeta si no existe, si existe la borra:
if os.path.exists("carpetaCreada"):
    os.rmdir("carpetaCreada")
else:
    os.mkdir("carpetaCreada")