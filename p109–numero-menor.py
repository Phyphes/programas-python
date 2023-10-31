# Diseñar un programa con una función que pida tres números enteros y devuelva el menor de ellos

import os ; os.system("cls")

def menor(n1, n2, n3):
    menor = 0
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3
    return menor

# Programa principal
print("Dame tres números : ")
n1,n2,n3 = float(input()), float(input()), float(input())
menor = menor(n1,n2,n3)
print(f"El menor de los tres números es {menor}")