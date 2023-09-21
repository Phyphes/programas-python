# Calcular el número mayor de una serie de números introducidos por el enter
# El proceso se detiene al introducir 0, el programa debe poder repetirse lo que el usuario decida

import os

while True:
    os.system("cls")
    mayor = 0

    while True:
        num = int(input("Dame los números: "))
        if num == 0: break
        
        if num > mayor:
            mayor = num
    
    print(f"El número mayor es {mayor}")
    res = input("¿Deseas continuar? (S/N) ").upper()
    if res == "N" : break

print("\nProceso terminado.")