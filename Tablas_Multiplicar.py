# Tablas de multiplicar del 1 al 9
def tablas(n):
    for i in range(1, 11):
        Resultado = n*i
        print(n, "X", i, "=", Resultado)


for j in range(1, 10):
    tablas(j)
    print()
