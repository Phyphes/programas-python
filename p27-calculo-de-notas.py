# Calcular el promedio de 5 calificaciones introducidas por el usuario e imprimir mensaje de acuerdo al promedio
import os ; os.system("cls")

print("Calculando el promedio de calificaciones\n")

print("Dame 5 calificaciones separadas por enter: ")
n1, n2 , n3, n4, n5 = float(input()), float(input()), float(input()), float(input()), float(input())

promedio = ( n1 + n2 + n3 + n4 + n5 ) / 5
print(f"El promedio es: {promedio:.2f}")

if promedio > 0 and promedio <= 6:
    print("\nREPROBADO")
if promedio > 6 and promedio <= 7:
    print("\nPASAS DE PANZAZO")
if promedio > 7 and promedio <= 8:
    print("\nMUY BIEN, PUEDES MEJORAR")
if promedio > 8 and promedio <= 9:
    print("\nEXCELENTE, SIGUE ASÍ")
if promedio > 9 and promedio <= 10:
    print("\nPERFECTO, TU ESFUERZO VALIÓ LA PENA")
