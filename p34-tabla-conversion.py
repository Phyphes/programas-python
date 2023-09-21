# Imprimir una tabla de conversión de Peso a Dolar

import os

tc = 19.13 ; tcl = 21.22

while(True):
    os.system("cls")
    while(True):
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final  : "))
        if pi < pf: break

    c = pi
    print("\nPesos\tDolar\tLibra")
    print("-"*25)
    while c <= pf:
        print(f"{c}\t{c/tc:.4f}\t{c/tcl:.4f}")
        c = c + 1
    print("-"*25)
    res = input("Deseas continuar? (S/N): ").upper()
    if res == "N": break

print("\nProceso terminado.")