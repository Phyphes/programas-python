# Imprime una pirámide de un caracter determinado usando dos ciclos for aninados

import os
os.system("cls")

n = int(input("Cuántos renglones? "))
c = input("Caracter? ")

for i in range (1, n+1):
    print()
    for i in range (1, i+1):
        print(c, end="")
    