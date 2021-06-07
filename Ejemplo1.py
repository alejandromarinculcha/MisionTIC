nombre_producto = str(input("Ingrese nombre del producto: "))
Costo_unitario = int(input("Ingrese costo Unitario: "))
Precio_venta = int(input("Ingrese precio de venta al público: "))
Cantidad_unidades_disponibles = int(
    input("Ingrese la cantidad de unidades disponibles: "))

Ganancia = (Precio_venta-Costo_unitario)*Cantidad_unidades_disponibles

print("Producto:", nombre_producto)
print("CU:", "$", Costo_unitario)
print("PV:", "$", Precio_venta)
print("Unidades Disponibles", Cantidad_unidades_disponibles)
print("Ganancia:",  "$", Ganancia)
print("Gracias por comprar en Alemarc Store")
