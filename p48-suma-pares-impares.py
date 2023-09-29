# Suma de números pares e impares hasta n

import os

while True:
    os.system("cls")

    n = int(input("Hasta dónde deseas (pares e impares): "))
    s = 0

    print("\nImprimir números pares y su suma")
    for par in range(2, n+1, 2):
        print(par, end=" ")
        s = s + par
    print("\nLa suma de los pares es", s)

    s = 0
    print("\nImprimir números impares y su suma")
    for impar in range(1, n+1, 2):
        print(impar, end=" ")
        s = s + impar
    print("\nLa suma de los pares es", s)

    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N" : break

print("\nProceso terminado...") 