# Imprime las tablas desde la tabla del 1 hasta la tabla n, desde 1 hasta m

import os

while True:

    os.system("cls")
    n = int(input("Hasta qué tabla? "))
    m = int(input("Hasta dónde? "))
    t = 1

    while t <= n :
        print(f"\nTabla del {t}\n")
        c = 1
        while c <= m :
            print(f"{t} x {c} = {t*c}")
            c = c + 1
        t = t + 1
    res = input("Deseas continuar? (S/N) ").upper()
    if res == "N" : break

print("\nProceso terminado.")