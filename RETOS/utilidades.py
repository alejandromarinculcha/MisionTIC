def clases(cadena):
    lista = []
    for i in range(0, len(cadena)-1):
        if (cadena[i] in cadena) and (cadena[i] not in lista):
            lista.append(cadena[i])
    return lista


def faltan(lista1, lista2, clase):
    posicion = []
    for i in range(0, len(lista2)):
        if clase == lista2[i]:
            posicion.append(i)
    final = []
    for y in range(0, len(lista1)):
        if lista1[y] in posicion:
            final.append(lista1[y])
    return final


def notengo(mayorista, calidad):
    lista = []
    for i in range(0, len(mayorista)):
        if mayorista[i] not in calidad:
            lista.append(mayorista[i])
    return lista


def intercambiar(mayorista, calidad):
    lista1 = []
    for i in range(0, len(mayorista)):
        if mayorista[i] not in calidad:
            lista1.append(mayorista[i])
    lista2 = []
    for i in range(0, len(calidad)):
        if calidad[i] not in mayorista:
            lista2.append(calidad[i])
    if len(lista1) > len(lista2):
        return len(lista2)
    else:
        return len(lista1)
