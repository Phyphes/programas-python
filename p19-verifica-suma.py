# Verifica si la suma de dos números es igual a un tercero
# 4 5 9   5 9 4   3 3 3   6 6 7   9 5 2

print("Dame 3 números enteros separados por teclado: ")
n1, n2, n3 = input().split()
n1, n2, n3 = (int(n1),int(n2),int(n3))

if n1 + n2 == n3:
    print("n1 + n2 = n3")
elif n1 + n3 == n2:
    print("n1 + n3 == n2")
elif n2 + n3 == n1:
    print("n2 + n3 == n1")
elif n1 == n2 == n3:
    print("n1 == n2 == n3")
else:
    print("Hay dos números iguales o todos son diferentes")

print("\nProceso terminado...")