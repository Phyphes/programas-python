# Determina el mayor de tres números

import os ; os.system("cls")

def mayor(n1, n2, n3):
    may = 0
    if n1 > n2 and n1 > n3:
        may = n1
    elif n2 > n1 and n2 > n3:
        may = n2
    else:
        may = n3
    return may

# Programa principal
print("Dame tres números : ")
n1,n2,n3 = float(input()), float(input()), float(input())
may = mayor(n1,n2,n3)
print(f"El mayor de los tres números es {may}")