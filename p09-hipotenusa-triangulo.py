# Calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados

import math

print("Calculando la hipotenusa de un triángulo rectángulo\n")
long_lado1 = float(input("Dame la longitud del primer lado: "))
long_lado2 = float(input("Dame la longitud del segundo lado: "))

hipotenusa = math.sqrt(long_lado1 * long_lado1 + long_lado2 * long_lado2)

print(f"La hipotenusa es: {hipotenusa}\n")

print(f"\nUn triángulo rectángulo con longitud de lado 1: {long_lado1} y longitud de lado 2: {long_lado2}, su hipotenusa es {hipotenusa:.2f}")
