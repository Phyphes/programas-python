# Crear un programa que permita procesar una lista de n números enteros

import os ; os.system("cls")

n = int(input("¿De cuántos números deseas la lista? "))
lista = []
suma = 0

# Agregar número a la lista
for c in range ( 1, n + 1 ):
    num = int(input(f"Número {c}: "))
    lista.append(num)
print(lista)

# Iterar lista para sacar suma y promedio
for num in lista:
    suma = suma + num
print("La suma es:",suma)
print("El promedio es:",suma/n)

