# Dados tres números enteros, verificar si son consecutivos y  mandar mensaje confirmándolo sino, mandar mensaje de error

import os ; os.system("cls")

print("Verificando si tres números son consecutivos\n")

print("Dame tres números enteros separados por teclado: ")
n1, n2 , n3 = input().split()
n1, n2 , n3 = int(n1), int(n2), int(n3)

if n1 + 1 ==  n2 and n1 + 2 == n3:
    print("Los números son consecutivos")
else:
    print("Los números no son consecutivos")
