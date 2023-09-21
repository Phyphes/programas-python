# Calcula e imprime los números de la conjetura collatz

import os

while True:

    os.system("cls")

    while True:
        num = int(input("Dame un número entero positivo: "))
        if num > 0: break

    while (num != 1):
        print(num, end=" ")
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num,end=" ")

    res = input("\nDeseas continuar? (S/N): ").upper()
    if res == "N": break

print("\nProceso terminado.")