# Uso de las funciones trigonométricas básicas

import math

print("Cálculo de las funciones trigonométricas básicas\n")
angulo = float(input("Dame un ángulo en grados: "))
ang_rad = math.radians(angulo)

seno     = math.sin(ang_rad)
coseno   = math.cos(ang_rad)
tangente = math.tan(ang_rad)

#print(f"Seno: {seno} \nCoseno: {coseno} \nTangente: {tangente}")

salida = ("\nResumen de funciones\n"
          f"El seno es: {seno}\n"
          f"El coseno es: {coseno}\n"
          f"La tangente es: {tangente}\n"
          f"\nEl ángulo de {angulo} grados, equivale a {ang_rad} radianes")
print(salida)
