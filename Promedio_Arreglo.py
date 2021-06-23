# sumar los elementos del arreglo
def suma_arreglo(A):
    s = 0
    for x in A:
        s = s+x
    return s


# calcula el promedio
def promedio(A):
    prom = suma_arreglo(A)/len(A)
    return prom


print(promedio([2, 4, 5]))
