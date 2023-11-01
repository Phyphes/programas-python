# Calcula el mayor y el menor de una lista de números, usando funciones

import os ; os.system("cls")

def leer():
    lista = []
    while True:
        n = float(input("Número: "))
        if n == -1 : break
        lista.append(n)
    return lista

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

# Programa principal
lista = leer()
# lista = [10,30,50,22,66,5,44]
print(lista, len(lista))
men = menor(lista)
may = mayor(lista)
print("El menor es",men)
print("El mayor es",may)