# Error de lista
print("")
try:
    lista = [1, 2, 3, 4, 5]
    print(lista[10])
except IndexError:
    print("Valor fuera de rango")
print("")