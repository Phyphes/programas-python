# Calcular el promedio de 3 calificaciones

print("Calcular el promedio de 3 calificaciones\n")
print("Dame 3 calificaciones separadas por espacio entre ellas: ")
c1, c2, c3 = input().split()
c1, c2, c3 = (float(c1), float(c2), float(c3))

suma = (c1 + c2 + c3)
promedio = suma / 3

print(f"\nLas calificaciones son {c1}, {c2} y {c3}, la suma es {suma:.2f} y el promedio es {promedio:.2f}")
