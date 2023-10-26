# Convierte de grados centígrados a farenheit y viceversa

import os ; os.system("cls")

def farenheit(temp):
    return (temp * (9/5)) + 32

def centigrados(temp):
    return (temp-32) * (5/9)

# Programa principal
print("[ F ] arenheit")
print("[ C ] entígrados")
op = input("Elije: ").upper()
if op == "F":
    temp = int(input("Dame los Centígrados: "))
    print(f"Los Farenheit son {farenheit(temp)}")
elif op == "C":
    temp = int(input("Dame los Farenheit: "))
    print(f"Los Centígrados son {farenheit(temp)}")
else:
    print("Opción incorrecta")