

class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def mostrar(self):
        if self.calificacion >= 6:
            print (f"El alumno {self.nombre} esta aprobado con", self.nota)
        else:
            print (f"El alumno {self.nombre} esta desaprobado con", self.nota)


nombre1 = (input("Ingrese el nombre del alumno: "))
calificacion1 = float(input("Ingrese la calificacion del alumno: "))
alumno1 = Alumno(nombre1, calificacion1)
alumno1.mostrar()

