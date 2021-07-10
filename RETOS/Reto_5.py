import utilidades as ut

print(ut.clases(["carnes", "carnes", "lacteos", "verduras", "frutas",
                 "lacteos", "carnes", "verduras", "verduras", "carnes"]))

print(ut.faltan([1, 2, 6, 8], ["carnes", "carnes", "lacteos", "verduras",
      "frutas", "lacteos", "carnes", "verduras", "verduras", "carnes"], "carnes"))

print(ut.notengo([3, 5, 7, 10, 15, 16], [4, 10, 5, 8]))

print(ut.intercambiar([3, 5, 7, 10, 15, 16], [4, 10, 5, 8]))
