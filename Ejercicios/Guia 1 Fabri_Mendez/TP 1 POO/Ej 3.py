


alto = int(input("Ingrese el alto del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))
caracter = input("Ingrese el caracter que quiera del dibujo: ")

for i in range(alto):
    for a in range(ancho):
        print(caracter, end="")
    print()