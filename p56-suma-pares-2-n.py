# Se desea imprimir los pares de 2 a n y su suma

import os

while True:
    os.system("cls")

    n = int(input("Hasta dónde imprimir los números: "))
    suma = 0 

    for i in range (2, n+1, 2):
        print(i, end=" ")
        suma = i + suma
        
    print(f"\nLa suma total es:",suma)

    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N": break

print("\nProceso terminado...")
    
