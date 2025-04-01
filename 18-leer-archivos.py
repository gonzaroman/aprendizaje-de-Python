# Hay cuatro métodos (modos) diferentes para abrir un archivo:
# "r" - Lectura: valor predeterminado. Abre un archivo archivo para lectura, error si el archivo no existe
# "a" - Anexar: abre un archivo para anexando, crea el archivo si no existe
# "w" - Escribir - Abre un archivo para escribir, Crea el archivo si no existe
# "x" - Crear: crea el archivo especificado, devuelve Un error si el archivo existe

# Además, puede especificar si el archivo debe manejarse en modo binario o de texto
# "t" - Texto: valor predeterminado. Modo de texto
# "b" - Binario - Modo binario (p. ej. imágenes)

#f = open("demofile.txt", "rt")

f = open("archivo.txt", "r")
print(f.read())

print("leemos una linea del  archivo")
f = open("archivo.txt", "r")
print(f.readline())

print("leemos la siguiente")
print(f.readline())
f.close()
print("leemos linea por linea")
f = open("archivo.txt", "r")
for x in f:
  print(x)
f.close()