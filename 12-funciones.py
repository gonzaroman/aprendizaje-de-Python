def hello():
    print("hola desde una funcion")

hello()


def helloParametros(nombre="nombre por defecto"):
    print("hola "+nombre)

helloParametros("Gonza")
helloParametros()

def suma(x,y):
    return x+y

print(suma(10,20))

#funciones lambda:
#estas funciones se escriben en una linea y tienen return por defecto
sumaLambda = lambda numero1,numero2: numero1+numero2

print(sumaLambda(3,4))