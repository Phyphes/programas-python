# Calcular la suma de números introducidos por el usuario hasta que la suma sea >=200
# Mostrar cuántos números fueron introducidos y la suma

import os

while True:
    os.system("cls")
    
    suma = 0
    cuenta = 0

    while True:
        num = int(input("Dame los números: "))
        cuenta = cuenta + 1
        suma = suma + num
        if suma >= 200: break
    print(f"La suma de los {cuenta} números introducidos es {suma}")
    
    res = input("¿Deseas continuar? (S/N) ").upper()
    if res == "N" : break
    
print("\nProceso terminado.")