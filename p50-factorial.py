# Imprime el factorial de un número

import os
os.system("cls")
n = int(input("Dame el número del cuál deseas el factorial: "))

f = 1
for h in range (1,n+1):
    print(h, end="*")
    f = f * h

print(" =",f)
