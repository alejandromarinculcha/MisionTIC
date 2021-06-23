def cuadrados_matriz(X):
    Y = []
    for i in range(len(X)):
        fila = []
    for j in range(len(X[i])):
        fila.append(X[i][j]*X[i][j])
    Y.append(fila)
    return Y


print(cuadrados_matriz([[1, -3, 2], [4, 11, -1]]))
