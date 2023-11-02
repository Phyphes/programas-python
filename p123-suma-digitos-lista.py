# Sumar los dígitos de cada número de una lista

import os ; os.system("cls")

def leer():
    lista = []
    while True:
        n = int(input("Número: "))
        if n == -1 : break
        lista.append(n)
    return lista

def suma_digitos(lista):
    sd = []
    for n in lista:
        suma = 0
        while n!=0:
            dig = n % 10
            suma = suma + dig
            n = n // 10
        sd.append(suma)
    return sd

l = leer()
l_suma = suma_digitos(l)
print("Lista original               : ", l, len(l))
print("Lista con la suma de dígitos : ", l_suma, len(l_suma))