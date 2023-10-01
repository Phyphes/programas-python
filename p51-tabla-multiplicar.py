# Imprimir la tabla de multiplicar que el usuario pida usando ciclo for

import os

while(True):
    os.system("cls")

    t = int(input("Qué tabla deseas? "))
    n = int(input("Hasta dónde? "))

    for i in range (1, n+1):
        print(f"{t} x {i} = {t*i}")
    
    res = input("\nDeseas continuar? (S/N) ").upper()
    if res == "N" : break