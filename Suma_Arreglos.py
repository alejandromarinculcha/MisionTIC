# Suma de dos arreglos

def suma_arreglo(A, B):
    if (len(A) == len(B)):
        c = []
        for x in range(0, len(A)):
            c.append(A[x]+B[x])
        return c
    else:
        return "No es posible ya que los vectores son de diferente tamaño."


print(suma_arreglo([1, 3, 6], [3, 2, 1]))

print(suma_arreglo([1, 3, 6], [3, 2, 1, 4]))
