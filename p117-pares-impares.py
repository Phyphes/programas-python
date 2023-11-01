# Regresa pares e impares de una lista de números, usando una función

import os ; os.system("cls")

def leer():
    lista = []
    while True:
        n = float(input("Número: "))
        if n == -1 : break
        lista.append(n)
    return lista

def paresimpares(lista):
    p = []
    i = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
        else:
            i.append(n)
    return p, i

# Programa principal
# lista = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]
lista = leer()
print(lista, len(lista))
p, i = paresimpares(lista)
print("Los pares son", p, len(p))
print("Los impares son", i, len(i))