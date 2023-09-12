# Dado un número entero entre 1-7, se muestra con letra el día de la semana
# 1 es domingo, 2 es lunes y así correspondientemente, número fuera de rango se muestra error

import os ; os.system("cls")

print("[1] es Domingo")
print("[2] es Lunes")
print("[3] es Martes")
print("[4] es Miércoles")
print("[5] es Jueves")
print("[6] es Sábado")
print("[7] es Domingo")

numero = int(input("\nDame un número entre 1-7: "))

if numero == 1:
    print("\nDomingo")
elif numero == 2:
    print("\nLunes")
elif numero == 3:
    print("\nMartes")
elif numero == 4:
    print("\nMiércoles")
elif numero == 5:
    print("\nJueves")
elif numero == 6:
    print("\nViernes")
elif numero == 7:
    print("\nSábado")
else:
    print("\nERROR número fuera de rango")

