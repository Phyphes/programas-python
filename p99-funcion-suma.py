# Función que recibe dos números y me regresa la suma

import os ; os.system("cls")

def suma(n1, n2, n3):
    s = n1 + n2 + n3
    return s

# Programa principal
sum = suma(200, 200, 100)
print("La suma es", sum)
print("La suma es", suma(900, 100, 100))

print("Dame tres números: ")
n1, n2, n3 = int(input()), int(input()), int(input())
sum = suma(n1, n2, n3)
print("La suma es",sum)