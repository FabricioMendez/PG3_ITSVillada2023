

def busqueda_elemento(lista, elemento):
   
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1
    
list = [8,12,9,45]
elemento_buscado = int(input("Ingrese un número: "))

indice = busqueda_elemento(list, elemento_buscado)
if indice != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el indice {indice} de la lista.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")