

class Familia:
    def __init__(self, nombrepadre, nombremadre, nombrehijo):
        self.padre = nombrepadre
        self.madre = nombremadre
        self.hijos = nombrehijo
    
    def __str__(self):
        return f"""
        Padre:{self.padre} 

        Madre: {self.madre}

        Hijos: {" ".join(self.hijos)}
        """

nombrepadre = input("Ingrese el nombre del padre: ")
nombremadre = input("Ingrese el nombre de la madre: ")
hijos = []

for _ in range (3):
    hijos.append(input("Ingrese hijo: "))

familia = Familia(nombrepadre, nombremadre, hijos)
print(familia)




