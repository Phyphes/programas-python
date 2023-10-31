# Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos
# regrese la suma de números pares o impares en el rango de números especificados.
# El programa deberá́ mostrar un menú́ con las opciones correspondientes y llamara a la función según la opción
# seleccionada.

import os ; os.system("cls")

def suma_pares_impares(op):
    if op == "P":
        ini = int(input("Desde dónde la suma: "))
        fin = int(input("Hasta dónde la suma: "))
        suma = 0
        for i in range(ini, fin + 1):                                                                                                                                       
            if i % 2 == 0:
                suma += i
        print(f"La suma de los pares es {suma}")
    elif op == "I":
        ini = int(input("Desde dónde la suma: "))
        fin = int(input("Hasta dónde la suma: "))
        suma = 0
        for i in range(ini, fin + 1):
            if i % 2 != 0:
                suma += i
        print(f"La suma de los impares es {suma}")
    else:
        suma = print("Opción incorrecta.")
    return suma

print("[ P ] ares")
print("[ I ] mpares")
op = input("Elije: ").upper()
suma_pares_impares(op)


