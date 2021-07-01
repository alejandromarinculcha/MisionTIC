# Realizar un programa que reciba un diccionario (en el formato JSON) con los nombres de los productos del supermercado y sus precios, y también reciba la lista de los productos que quiere comprar Juanito.
# El programa debe mostrar los nombres de los productos que Juanito finalmente puede comprar en el supermercado y el valor total que pagará en la compra.
import json

# Para recibir un diccionario (en el formato JSON).
# ---------> producto1 = json.loads(input())

# Para crear un diccionario con dos claves
producto1 = {input(): int(input()), input(): int(input())}
Lista = input().split(" ")


suma = 0
lista = ""
for i in range(0, len(Lista)):
    if Lista[i] in producto1:
        valor = producto1.get(Lista[i])
        suma = valor + suma
        lista += f"{Lista[i]} "

print(suma)


print(lista)
