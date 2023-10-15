# Crear un diccionario de llave numérica días

import os ; os.system("cls")

dias = {
    1 : 'Lunes',
    2 : 'Martes',
    3 : 'Miércoles',
    4 : 'Jueves',
    5 : 'Viernes',
    6 : 'Sábado',
    7 : 'Domingo' 
}

print(f"\nDiccionario: \n{dias}",len(dias))
print(f"\nPrimer elemento : {dias[1]}")     # usando []
print(f"Último elemento : {dias[7]}")       # usando []
print(f"Quinto elemento : {dias.get(5)}")   # usando get
print(f"Séptimo elemento: {dias.get(7)}")   # usando get
print(f"\nDiccionario: \n{dias}",len(dias))
