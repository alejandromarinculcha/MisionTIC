# Determinar si un elemento de una lista es una cadena palíndrome
def palindrome(cadena):
    j = len(cadena)-1

    for i in range(0, len(cadena)):
        if (cadena[i] != cadena[j]):
            return False
        j = j-1

    return True


def listaconPalindrome(lista):
    for palabra in lista:
        if (palindrome(palabra)) == True:
            return "Si existe"

    return "No existe"


l1 = ["al sur de Colombia", "amor a roma", "amo a mi ciudad"]
l2 = ["al sur de Colombia", "la tele letal", "amo a mi ciudad"]
print(listaconPalindrome(l1))
print(listaconPalindrome(l2))


# ___________________________________________________________________
# Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'

# Función que valida si hay una vocal en una cadena


def comparar(cadena):

    cantidad = 0
    cadena2 = 'aeiou'

    for i in range(0, 5):  # recorre la cadena de vocales
        # cuenta cada vocal cuantas veces aparece en otra cadena
        cantidad = cadena.count(cadena2[i], 0, len(cadena))+cantidad

    if cantidad >= 2:  # si la cantidade de vocales es mayor o igual que 2
        return True
    else:
        return False


# función que dada una lista de palabras, revisa si hay palabras que contienen mas de dos vocales
def listaconVocal(lista):
    mensaje = "No existe"
    for i in range(0, len(lista)):
        if (comparar(lista[i])) == True:
            print(lista[i])
            mensaje = "Si existe"
    print(mensaje)


l1 = ["rr", "casa", "KJLR", "ttt"]
l2 = ["casa", "perro"]
l3 = ["rr", "cs", "KJLR", "ttt"]
print(listaconVocal(l1))
print(listaconVocal(l2))
print(listaconVocal(l3))
