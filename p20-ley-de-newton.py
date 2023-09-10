# Calcula la segunda ley de newton ( F = M * A )
import os

os.system("cls")
print("[F]uerza         F = M  * A ")
print("[M]asa           M = F  / A ")
print("[A]celeración    A = F  / M ")

opcion = input("Elige la operación: ").upper()

if opcion == "F":
    print("\nCalculando la Fuerza")
    m = float(input("\nDame la Masa: "))
    a = float(input("Dame la Aceleración: "))
    f = m * a
    print(f"\nLa Fuerza es: {f:.2}")
elif opcion == "M":
    print("\nCalculando la Masa")
    f = float(input("\nDame la Fuerza: "))
    a = float(input("Dame la Aceleración: "))
    m = f / a
    print(f"\nLa Masa es: {m:.2}")
elif opcion == "A":
    print("\nCalculando la Aceleración")
    f = float(input("\nDame la Fuerza: "))
    m = float(input("Dame la Masa: "))
    a = f / m
    print(f"\nLa Aceleración es: {a:.2}")
else:
    print("\nOpción Inválida")

print("\nProceso terminado...")