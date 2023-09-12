# Dados tres números enteros, verificar cuál es el mayor

import os ; os.system("cls")

print("Verificando cuál número es el mayor de tres números\n")

print("Dame tres números enteros separados por teclado: ")
n1, n2 , n3 = input().split()
n1, n2 , n3 = int(n1), int(n2), int(n3)

if n1 >= n2 and n1 >= n3:
    print ("El número mayor es:",n1)
elif n2 >= n1 and n2 >= n3:
    print ("El número mayor es:",n2)
elif n3 >= n1 and n3 >= n2:
    print ("El número mayor es:",n3)

print("\nProceso terminado.")