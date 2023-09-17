# Imprimir los números del 100 al 1, en decrementos de 1

import os ; os.system("cls")

n = int(input("Desde dónde: "))
c = n

while c >= 1:
    print(c, end=" ")
    c = c - 1

print("\nFuera del ciclo")