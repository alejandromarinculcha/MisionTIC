def pago_final(n, precio):
    if n <= 5:
        valor = n * precio
    elif n <= 10:
        valor = n * precio * 0.95
    elif n <= 20:
        valor = n * precio * 0.90
    else:
        valor = n * precio * 0.80
    return valor


n = int(input("Ingrese número de productos: "))
precio = int(input("Ingrese el precio del producto: "))

print("El pago final es: ", pago_final(n, precio))
