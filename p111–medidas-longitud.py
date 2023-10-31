# Diseñar un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies

import os ; os.system("cls")

def centimetros(m):
    return (m * 2.54)

def pies(m):
    return (m * 3.281)

# Programa principal
print("[ C ] entímetros ")
print("[ P ] ies        ")
op = input("Elije: ").upper()
if op == "C":
    m = int(input("Dame las pulgadas: "))
    print(f"{m} pulgadas son {centimetros(m)} cm")
elif op == "P":
    m = int(input("Dame los metros: "))
    print(f"{m} metros son {pies(m)} pies")
else:
    print("Opción incorrecta")