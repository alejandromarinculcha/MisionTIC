# Producto escalar o punto
def productoPunto(v, w):

    s = 0
    for i in range(0, len(v)):
        s = s+(v[i]*w[i])
    return s


A = [1, -3, 4, 11, 67]
B = [1, 5, 2, 1, 6]
print(productoPunto(A, B))


# _____________________________________
# Invertir un arreglo
def invertir(A):

    Ainv = []

    for i in range(len(A)-1, -1, -1):
        Ainv.append(A[i])
    return(Ainv)


A = [1, -3, 4, 11, 67]
print(invertir(A))


# _____________________________________
# Mediana de un arreglo
def mediana(A):

    A.sort()  # ordena el arreglo

    if (len(A) % 2 == 0):  # es par
        return(A[(len(A)//2)-1])
    else:
        return(A[(len(A)//2)])


A = [1, 11, 4, -3, 67]
B = [2, 4, -6, 1]

print(mediana(A))
print(mediana(B))
