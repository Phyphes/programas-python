# Crear una lista y aplicar funciones estadísticas

import os ; os.system("cls")
from math import sqrt

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
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def varianza(lista):
    media = 0
    for n in lista:
        media += n
    media =  media / len(lista)
    suma = 0
    for n in lista:
        suma += (n - media)**2
    var = (suma * 1 / len(lista))
    return var

def desviacion(lista):
    media = 0
    for n in lista:
        media += n
    media =  media / len(lista)
    suma = 0
    for n in lista:
        suma += (n - media)**2
    varianza = (suma * 1 / len(lista))
    desviacion = sqrt(varianza)
    return desviacion

lista = leer()
print("Lista de números :", lista, len(lista))
may = mayor(lista)
print("El mayor de los datos :", may)
men = menor(lista)
print("El menor de los datos :", men)
med = media(lista)
print(f"La media : {med:.3f}")
var = varianza(lista)
print(f"Varianza : {var:.3f}")
desv = desviacion(lista)
print(f"Desviación estándar : {desv:.3f}")