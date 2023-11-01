# Se generan dos listas de números aleatorios y se suman

import os ; os.system("cls")

import random

MAX = 15

def genera_aleatorios():
    l = []
    for n in range(MAX):
        l.append(random.randint(1,100))
    return l

def suma_listas(l1, l2):
    s = []
    for n in range(MAX):
        s.append(l1[n]+l2[n])
    return s

# Programa principal
l1 = genera_aleatorios()
print("Lista 1", l1, len(l1))
l2 = genera_aleatorios()
print("Lista 2", l2, len(l2))
s = suma_listas(l1, l2)
print("La suma de las listas es", s, len(s))