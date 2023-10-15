# Crear un diccionario de llave de cadena ventas

import os ; os.system("cls")

ventas = {
    'Juan' : 1550,
    'José' : 2600,
    'María' : 2220,
}

print(f"\nDiccionario original: \n{ventas}",len(ventas))
ventas['Rocío'] = 2500              # agregar elemento usando []
ventas['Mateo'] = 1567              # agregar elemento usando []
ventas.update({'Andrea' : 9567})    # agregar elemento usando update
ventas.update({'Miguel' : 1234})    # agregar elemento usando update
print(f"\nDiccionario modificado: \n{ventas}",len(ventas))