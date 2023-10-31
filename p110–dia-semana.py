# Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra

import os ; os.system("cls")

def dia(n):
    dia = ""
    if n == 1:
        dia = "Lunes"
    elif n == 2:
        dia = "Martes"
    elif n == 3:
        dia = "Miércoles"
    elif n == 4:
        dia = "Jueves"
    elif n == 5:
        dia = "Viernes"
    elif n == 6:
        dia = "Sábado"
    elif n == 7:
        dia = "Domingo"
    else:
        dia = "Error"
    return dia
    
n = int(input("Dame el día de la semana (1-7): "))
print(f"El día de la semana es {dia(n)} ")