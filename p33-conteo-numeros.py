# Cuenta números, los suma, cuenta positivos, negativos y ceros, se detiene al introducir 999

import os ; os.system("cls")

cuenta = suma = cp = cn = cc = 0

while (True):
    numero = int(input("Número: "))
    if numero != 999:
        cuenta = cuenta + 1
        suma = suma + numero
        if numero > 0:
            cp = cp + 1
        elif numero < 0:
            cn = cn + 1
        else:
            cc = cc + 1
    else:
        break

print(f"Se introdujeron {cuenta} números")
print(f"La suma de los números es {suma}")
print("Los positivos son ", cp)
print("Los negativos son ", cn)
print("Los ceros son "    , cc)