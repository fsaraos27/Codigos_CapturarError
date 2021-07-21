# Error en colores
print("")
try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    print(colores['blanco'])
except KeyError:
    print("No existe en la lista")
print("")
