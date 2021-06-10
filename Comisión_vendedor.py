def comision_empleado(cat, ventas):
    if cat == 1:
        comi = ventas * 0.1
    elif cat == 2:
        comi = ventas * 0.2
    elif cat == 3:
        comi = ventas * 0.35
    elif cat == 4:
        comi = ventas * 0.45
    elif cat == 5:
        comi = ventas * 0.5
    else:
        comi = ventas * 0.6
    print("Su comisión es de: $" + str(comi) + ", ya que su categoría es:",
          cat, "y sus ventas son de: $" + str(ventas))


CATEGORIA = int(input("Ingrese su categoria: "))
VENTAS = int(input("INGRESE SUS VENTAS: "))

comision_empleado(CATEGORIA, VENTAS)
