# Calcular el tercer ángulo de un triángulo dados los dos ángulos restantes

print("Calcular el 3er ángulo de un triángulo dando los dos ángulos restantes\n")

angulo1 = float(input("Dame el primer ángulo: "))
angulo2 = float(input("Dame el segundo ángulo: "))

angulo3 = 180 - (angulo1 + angulo2)

if angulo3 < 0.01:
    print("\nLa suma de los tres ángulos de un triángulo no es mayor a 180 grados")
else:
    print(f"El valor del tercer ángulo es: {angulo3}")
    print("\nLa suma de los tres ángulos del triángulo son 180 grados")
