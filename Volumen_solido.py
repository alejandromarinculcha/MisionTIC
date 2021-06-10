"""
Modelo matematico:
volSolido: RxRxR->R
(r1, r2,h)<->(4/3* pi*r1^3)+ (pi* r^2*h)/3

Variables: r1, r2 y h

"""
# MÉTODO 1
import math
"""
def volsolido(r1, r2, h):
    volumen = (4/3*math.pi*r1**3)+(math.pi*r2**2*h)/3
    return volumen


radio1 = float(input("Ingrese el radio 1: "))
radio2 = float(input("Ingrese el radio 2: "))
altura = float(input("Ingrese la altura: "))

print("El volumen del sólido es:", volsolido(radio1, radio2, altura))
"""

# MÉTODO 2


def volEsfera(r1):
    volumen = 4/3*math.pi*r1**3
    return volumen


def volCono(r1, h):
    volumen = (math.pi*r1**2*h)/3
    return volumen


def VolSolido(r1, r2, h):
    volumen = volEsfera(r1) + volCono(r2, h)
    return volumen


re = float(input("Ingrese el radio de la esfera: "))
rc = float(input("Ingrese el radio del cono: "))
hc = float(input("Ingrese la altura del cono: "))

print(VolSolido(re, rc, hc))
