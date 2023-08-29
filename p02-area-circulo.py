# Calcula el area de un circulo dado el radio

import math # importamos la libreria de funciones y constantes matematicas

print("Calculando el área de un círculo \n")

radio = float(input("Dame el radio: "))

# area = 3.1416 * radio * radio
area = math.pi * math.pow(radio,2) # a la potencia, al cuadrado

print(f"\nPara un círculo de radio {radio}, el área resultante es {area:.2f}") # dos decimales
