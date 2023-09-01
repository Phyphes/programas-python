# calcular el volumen de un cilindro dado su radio y altura

import math

print("Calculando el volumen de un cilindro dado su radio y altura\n")
radio = float(input("Dame el radio del cilindro: "))
altura = float(input("Dame la altura del cilindro: "))

volumen = math.pi * (radio * radio) * altura

print(f"El volumen es: {volumen:.2f}")

print(f"\nUn cilindro con radio de {radio} y altura de {altura} su volumen es {volumen:.2f}")
