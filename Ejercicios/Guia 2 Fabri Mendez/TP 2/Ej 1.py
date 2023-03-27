

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Te llamas: ", self.nombre)

Persona1 = Persona(input("Ingrese su nombre: "))
Persona1.mostrar()


