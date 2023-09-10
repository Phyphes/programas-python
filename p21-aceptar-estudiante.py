# Aceptar a un estudiante en base a la edad y sus calificaciones
import os
os.system("cls")

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

if edad >= 18:
    print("continuamos el proceso de aceptación...")
    print("Dame dos calificaciones separadas por enter: ")
    c1, c2 = int(input()), int(input())
    if c1 >=8 and c2 >= 8:
        print(f"{nombre} bienvenid@, tus calificaciones {c1}, {c2} y tu edad de {edad} años, han sido aprobadas")
    else:
        print("Sólo aceptamos promedios calificaciones mayores a 8")
else:
    print("Sólo aceptamos mayores de 18 años")

print("\nProceso terminado...")