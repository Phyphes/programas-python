# Regresa la estación del año con letra dado un número del 1 al 4

import os ; os.system("cls")

def estacion(n):
    est = ""
    if n == 1:
        est = "Primavera"
    elif n == 2:
        est = "Verano"
    elif n == 3:
        est = "Otoño"
    elif n == 4:
        est = "Invierno"
    else:
        est = "Error"
    return est
    
n = int(input("Dame la estación del año (1-4): "))
print(f"La estación del año es {estacion(n)} ")