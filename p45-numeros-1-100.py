# Imprime los números del 1 al x en y 

import os
os.system("cls")

x = int(input("Hasta dónde: "))
y = int(input("De cuánto en cuánto: "))

for n in range(1, x+1, y):
    print(n, end=" ")