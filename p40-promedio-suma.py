# Calcular la suma y el promedio de una serie de números introducidos por enter hasta introducir 0
# Deberá contar cuántos números se introdujeron, el proceso debe repetirse hasta que el usuario lo decida

import os

while True:
    os.system("cls")

    suma = 0
    cuenta = 0

    while True:
        num = float(input("Dame los números: "))
        cuenta = cuenta + 1
        suma = suma + num
        if num == 0: break
    print(f"Se introdujeron {cuenta} números")
    print(f"La suma de todos los números es {suma}")
    print(f"El promedio es {suma/cuenta}")
    
    res = input("¿Deseas continuar? (S/N) ").upper()
    if res == "N" : break
    
print("\nProceso terminado.")
