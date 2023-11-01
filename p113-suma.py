# Calcula la suma de una lista de números usando una función

import os ; os.system("cls")

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s

# Programa principal
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista = []
while True:
    n = float(input("Número: "))
    if n == -1 : break
    lista.append(n)

print(lista, len(lista))
res = suma(lista)
print("La suma es", res)