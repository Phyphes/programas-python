#  Calcular el factorial de cada número de una lista

import os ; os.system("cls")

def leer():
    lista = []
    while True:
        n = int(input("Número: "))
        if n == -1 : break
        lista.append(n)
    return lista

def factoriales(lista):
    sd = []
    for n in lista:
        f = 1
        for n in range(1, n+1):
            f = f * n
        sd.append(f)
    return sd

lista = leer()
lista_factoriales = factoriales(lista)
print("Lista original            : ", lista, len(lista))
print("Lista con los factoriales : ", lista_factoriales, len(lista_factoriales))