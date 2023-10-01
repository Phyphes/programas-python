# Imprimir los números de 1 a n de 10 en 10

import os

while True:
    os.system("cls")

    n = int(input("Hasta dónde imprimir los números: "))

    for i in range(1, n+1, 10):
        print(i, end=" ")

    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N": break

print("\nProceso terminado...")