# Pedir un número entre 1-10 y muestre su equivalente en número romano, si el número no está en el rango mandar mensaje de error

import os ; os.system("cls")

print("[1]  es  I")
print("[2]  es  II")
print("[3]  es  III")
print("[4]  es  IV")
print("[5]  es  V")
print("[6]  es  VI")
print("[7]  es  VII")
print("[8]  es  VIII")
print("[9]  es  IX")
print("[10] es  X")

numero = int(input("\nDame un número entre 1-7: "))

if numero == 1:
    print("\nI")
elif numero == 2:
    print("\nII")
elif numero == 3:
    print("\nIII")
elif numero == 4:
    print("\nIV")
elif numero == 5:
    print("\nV")
elif numero == 6:
    print("\nVI")
elif numero == 7:
    print("\nVII")
elif numero == 8:
    print("\nVIII")
elif numero == 9:
    print("\nIX")
elif numero == 10:
    print("\nX")
else:
    print("\nERROR número fuera de rango")
