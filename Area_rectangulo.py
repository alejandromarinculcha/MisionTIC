# OPCIÓN 1
"""
def area_rectangulo(l, a):
    area = l*a
    return area


largo = float(input("Ingrese el valor del largo: "))
ancho = float(input("Ingrese el valor del ancho: "))

a = area_rectangulo(largo, ancho)
print(a)
"""

# OPCIÓN 2


def area_rectangulo(L, a):
    area = L*a
    print("El área del rectangulo es:", area)


largo = float(input("Ingrese el valor del largo: "))
ancho = float(input("Ingrese el valor del ancho: "))

area_rectangulo(largo, ancho)
