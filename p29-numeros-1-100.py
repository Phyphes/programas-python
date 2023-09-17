# Imprimir los números del 1 al 100 de 1 en 1

import os ; os.system("cls")

n = int(input("Hasta donde quieres llegar: "))
p = int(input("De cuánto en cuánto: "))

c = 1
while c <= n :
    print(c, end= " ")
    c = c + p