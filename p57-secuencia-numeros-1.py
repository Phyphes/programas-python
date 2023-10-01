# Imprimir la secuencia de números mostrando el número de renglones que el usuario desee

import os

while True:
    os.system("cls")
    n = int(input("Hasta dónde imprimir la secuencia: "))

    for i in range (1, n+1):
        print()
        for j in range (1, i+1):
            print(i, end=" ")
    
    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N": break

print("\nProceso terminado...")
    