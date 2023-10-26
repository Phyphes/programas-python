# Regrese la suma de números en el rango de números especificados

import os ; os.system("cls")

def suma_rango(ini, fin):
    s = 0
    for i in range(ini, fin + 1):
        s += i
    return s

ini = int(input("Desde dónde la suma: "))
fin = int(input("Hasta dónde la suma: "))
print(f'La suma en el rango de {ini} y {fin} es {suma_rango(ini,fin)}')