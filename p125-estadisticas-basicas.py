# Crear una lista y aplicar funciones estadísticas

import os ; os.system("cls")

import statistics

def leer():
    lista = []
    while True:
        n = int(input("Número: "))
        if n == -1 : break
        lista.append(n)
    return lista

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def media(lista):
    media = statistics.mean(lista)
    return media

def varianza(lista):
    varianza = statistics.pvariance(lista)
    return varianza

def desviacion(lista):
    desviacion = statistics.pstdev(lista)
    return desviacion

l = leer()
print("Lista de números :", l, len(l))
may = mayor(l)
print("El mayor de los datos :", may)
men = menor(l)
print("El menor de los datos :", men)
med = media(l)
print(f"La media : {med:.3f}")
var = varianza(l)
print(f"Varianza : {var:.3f}")
desv = desviacion(l)
print(f"Desviación estándar : {desv:.3f}")