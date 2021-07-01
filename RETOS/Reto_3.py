# Usted debe realizar un programa que valide la contraseña ingresada y verifique si hay palabras seguidas que se repitan. El programa debe mostrar la cantidad de palabras iguales contiguas.
cadena = input().split(" ")

for i in range(0, len(cadena)-1):
    if cadena[i] != cadena[i+1]:
        print(cadena[i], end=" ")
print(cadena[i+1], "\t")

contar = 1
for y in range(0, len(cadena)-1):
    if cadena[y] == cadena[y+1]:
        contar += 1
    if cadena[y] != cadena[y+1]:
        print(contar, end=" ")
        contar = 1
print(contar)
