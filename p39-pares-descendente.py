# Imprimir los números pares desde 100 hasta el número que el usuario decida (n) 
# Imprimir la suma de esos pares, el proceso debe repetirse hasta que el usuario lo decida

import os

while True: 
    
    os.system("cls")
    
    n = int(input("¿Hasta dónde quieres el conteo? "))
    c = 100
    suma = 0
    
    while c >= n :
        if c % 2 == 0:
            print(c, end=" ")
            suma = suma + c
        c = c - 1
    
    print(f"\nLa suma de todos los números es {suma}")
    
    res = input("¿Deseas continuar? (S/N) ").upper()
    if res == "N" : break

print("\nProceso terminado.")