# Calcula el factorial de un número entero

import os ; os.system("cls")

def factorial(n):
    f = 1
    for n in range(1, n+1):
        f = f * n
    return f

# Programa principal
n = int(input("Número: "))
print(f"El factorial de {n} es {factorial(n)}")