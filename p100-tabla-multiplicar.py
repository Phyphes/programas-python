# Imprime la tabla de multiplicar que el usuario pida hasta donde la pida

import os ; os.system("cls")

def tabla(t,n):
    print(f"Tabla del {t} hasta el {n}")
    for i in range(1,n+1):
        print(f"{t} x {i} = {t*1}")
    print()

# Programa principal
t = int(input("Qué tabla quieres? "))
n = int(input("Hasta dónde quieres la tabla? "))
tabla(t,n)
tabla(5,4)
tabla(4,5)
