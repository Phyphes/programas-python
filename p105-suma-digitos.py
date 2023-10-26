# Suma los dígitos de un número entero 1971 = 18

import os ; os.system("cls")

def sumadigitos(n):
    suma = 0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n // 10
    return suma

# Programa principal
año = int(input("Dame tu año y te diré tu número de la suerte: "))
suerte = sumadigitos(año)
print(f"Tu año de nacimiento es {año} por lo tanto tu número de la suerte es {suerte}")