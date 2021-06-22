# Determina si en una lista no existen elementos repetidos

def comparar(lista):

    lista.sort()  # se ordena la lista
    print(lista)
    for i in range(0, len(lista)-1):
        if lista[i] == lista[i+1]:
            return "Existen elementos repetidos"

    return("No existen elementos repetido")


l1 = [10, 12, 10, 12, 13, 23, 2, 3, 4]
l2 = [1, 4, 5, 6, 10]
print(comparar(l1))
print(comparar(l2))
