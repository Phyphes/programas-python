# Imprime los números desde x a 1 descendiendo en y

import os
os.system("cls") 

x = int(input("Desde dónde comenzar a descender: "))
y = int(input("De cuánto en cuánto desciende: "))

for n in range(x,0,-y):
    print(n, end=" ")