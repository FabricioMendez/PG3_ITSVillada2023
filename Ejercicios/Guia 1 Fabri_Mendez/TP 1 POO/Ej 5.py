

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

f = input("Ingrese una palabra: ")
print(es_palindromo(f))

