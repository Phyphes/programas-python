# Imprimir los números de 1 a n o de n a 1, según el usuario lo decida

import os

while True:
    os.system("cls")

    print("[1] Imprimir los números de 1 a n")
    print("[2] Imprimir los números de n a 1")
    op = int(input("Elije: "))

    if op == 1:
        print("\nImprimiendo de 1 hasta n\n")
        n = int(input("Dame el valor de n: "))
        for z in range(1, n+1, 1):
            print(z, end=" ")
    elif op == 2:
        print("\nImprimiendo desde n hasta 1\n")
        n = int(input("Dame el valor de n: "))
        for w in range(n, 0 , -1):
            print(w, end=" ")
    else:
        print("\Opción Inválida")

    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N" : break

print("\nProceso terminado...")