"""
def area(r):
    return 3.1416*r**2


r = int(input("Ingrese radio del círculo: "))
print(area(r))
"""

import math


def area(r):
    return math.pi*r**2


# El programa empieza desde aquí ya que es lo principal y ...
# apenas ve una función va y la busca arriba.
radio = float(input("Ingrese radio del círculo: "))
print(area(radio))
