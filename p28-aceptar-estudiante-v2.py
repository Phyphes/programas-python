# Dado el nombre del estudiante, sexo(h/m), su edad, y tres calificaciones, decidir si es aceptado
# La Universidad Kitty Kat SA es sólo para mujeres mayores de 21 con un promedio entre 8 y 9.5

import os ; os.system("cls")

print("Aceptando estudiantes de ingreso para Universidad Kitty Kat SA\n")

nombre = input("Dame tu nombre: ")
print("[H]ombre")
print("[M]ujer")
sexo = input("Dame tu sexo H/M: ").upper()

if sexo == "M":
    edad = int(input("Dame tu edad: "))
    if edad >= 21:
        print("Dame 3 calificaciones separadas por enter: ")
        n1, n2 , n3 = float(input()), float(input()), float(input())
        promedio = ( n1 + n2 + n3 ) / 3
        if promedio >= 8 and promedio <= 9.5:
            print(f"\nFelicidades {nombre}, fuiste aceptada en la Universidad Kitty Kat SA con tu promedio de {promedio:.2f}")
        else:
            print("\nLo sentimos, tu promedio no cumple con los requisitos de admisión")
    else:
        print("\nLo sentimos, tu edad no cumple con los requisitos de admisión")
else:
    print("\nLo sentimos, sólo se aceptan mujeres en la Universidad Kitty Kat SA")
