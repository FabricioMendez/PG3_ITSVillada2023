

class Persona:
    def __init__(self ,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Empleado(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    def sueldo(self, sueldo):
        self.sueldo = sueldo
        if self.sueldo >= 3000:
            print("Tiene que pagar impuestos")
        else:
            print("No tiene que pagar impuestos")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
sueldo = int(input("Ingrese su sueldo: "))

em =Empleado(nombre, apellido)
em.sueldo(sueldo)


