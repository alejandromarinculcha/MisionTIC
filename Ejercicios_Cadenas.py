# Determinar si la primera cadena está en la cadena 2
def comparar(cadena1, cadena2):

    for i in range(0, len(cadena1)):
        if cadena1[i] not in cadena2:
            return "No esta"
    return "Si esta"


cadena1 = input("Ingrese la primer cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
print(comparar(cadena1, cadena2))


# Determinar si una cadena es palíndrome
def palindrome(cadena):
    j = len(cadena)-1

    for i in range(0, len(cadena)):
        if (cadena[i] != cadena[j]):
            return "No es palindrome"
        j = j-1

    return "Si es palindrome"


palabra = input("Ingrese la o las cadena(S) a evaluar: ")
print(palindrome(palabra))
