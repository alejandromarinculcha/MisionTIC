# IMPRIMIR NÚMEROS DEL 1 AL 100 Y SU CUADRADO
for x in range(1, 101):
    print(x, x**2)


    
# NÚMEROS IMPARES DESDE 1 HASTA 99 Y OTRO LISTADO DE NÚMEROS PARES DESDE 2 HASTA 1000
for x in range(1, 999+1, 2):
    print(x)  # Imprime números impares
for y in range(2, 1000+1, 2):
    print(y)  # Imprime números pares

    

# NÚMEROS PARES DESDE 1000 HASTA 2
x = int(input("Ingrese un número par de inicio: "))
for n in range(x, 3, -2):
    print(n)

    

# Imprimir desde 1 hasta n, con su respectivo factorial
def factorial(n):
    fact = 1
    for a in range(1, n+1):
        fact = fact*a
    return(fact)

x = int(input("Ingrese número: "))

for b in range(1, x+1):
    print("Númpero:", b)
    print("Factorial:", factorial(b))

    

# Calcular el valor de n elevado a la potencia m
base = int(input("Ingrese número base: "))

def potencia_dada(n):
    potencia = 1
    for i in range(1, n+1):
        potencia = potencia*base
    return potencia

m = int(input("Ingrese la potencia: "))
print("El resultado es:", potencia_dada(m))
