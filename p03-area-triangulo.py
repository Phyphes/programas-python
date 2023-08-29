# Calcula el area de un triangulo dada la base y la altura

import math

print("Calculando el área de un triángulo \n")
print("Dame la base y la altura separados por un enter: ")
base, altura = int(input()), int(input())

area = ( base * altura ) / 2

print(f"\nEl triángulo de base {base} y altura {altura} tiene un área de {area:.2f}")
