# Imprime los números del 1 al 200 hasta alcanzar la suma de 100

import os ; os.system("cls")

c = 0       # ?
suma = 0    # 100

while c <=200:
    c = c + 1
    suma = suma + c
    print(c, end=" ")
    if suma >= 1500:
        print()
        break

print(f"Hemos alcanzado la cantidad límite {suma}, sumando {c} números")