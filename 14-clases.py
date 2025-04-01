class MiClase:
    x=5

c1 = MiClase()
print(c1.x)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre}({self.edad})"
    
    #metodos:
    def miMetodo(self):
        print("mi nombre es "+self.nombre )

p1 = Persona("gonza", 99)

print(p1.nombre)
print(p1.edad)

p2 = Persona("juan",89)

print(p1)

#metodos:
p3 = Persona("Antonio",59)
p3.miMetodo()

p3.nombre = "Pedro"
p3.miMetodo()

#herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, year, titulacion):
        super().__init__(nombre, edad)
        self.curso = year
        self.titulacion = titulacion
    def bienvenido(self):
        print("bienvenido", self.nombre, "a la clase de", self.titulacion)

marcelo = Estudiante("Marcelo",29,2025,"DAM")

marcelo.bienvenido()