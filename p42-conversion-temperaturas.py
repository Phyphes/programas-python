# El usuario introduce la temperatura inicial y la temperatura final en grados centígrados 
# El programa realiza la conversión a farenheit incrementando el valor inicial en 1
# hasta llegar al valor final, el proceso debe poder repetirse hasta que el usuario lo decida

import os

while True:
    os.system("cls")
    vi = int(input("Valor inicial de la temperatura (°C): "))
    vf = int(input("Valor final de la temperatura (°C): "))
    
    print("\nGrados Celsius\tGrados Fahrenheit")
    while vi <= vf :
        print(f"     {vi}                {vi * 9/5 + 32}")
        vi = vi + 1 
    res = input("Deseas continuar? (S/N): ").upper()
    if res == "N" : break

print("\nProceso terminado.")