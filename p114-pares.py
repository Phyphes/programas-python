# Formar una lista por medio de los pares de otra lista

import os ; os.system("cls")

def pares(lista):
    p = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
    return p

def leer():
    lista = []
    while True:
        n = float(input("Número: "))
        if n == -1 : break
        lista.append(n)
    return lista

# Programa principal
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = leer()
print(lista, len(lista))
res = pares(lista)
print("La lista con los pares es ", res, len(res))