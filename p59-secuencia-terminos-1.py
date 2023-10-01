# Imprimir la secuencia de términos armónicos el número de renglones que el usuario desee y su suma

import os

while True:
    os.system("cls")

    n = int(input("De cuántos números deseas el factorial? "))

    for i in range (1, n+1):
        print(f"1/{i}! + ", end="")
        f = 1
        suma = 0
        for j in range (1, i+1):
            f = (f * j)
            inverso = 1/f
            suma = inverso + suma
            
    print("\nLa suma de los factoriales inversos es",suma) 

    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N": break

print("\nProceso terminado...")
