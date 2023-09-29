# Imprime la suma y el promedio de n numeros introducidos por el usuario

n = int(input("Cuántos números deseas procesar? "))
suma = 0
promedio = 0

for c in range ( 1, n+1 ):
    num = int(input(f"Número {c}: "))
    suma = suma + num

promedio = suma / n
print("\nLa suma es",suma)
print("El promedio es",promedio)