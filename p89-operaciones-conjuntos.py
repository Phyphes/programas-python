# Nos permite ejemplificar las operaciones lógicas sobre conjuntos

import os ; os.system("cls")

c1 = {1,2,3,4,5}
c2 = {5,6,7,8,9,10}
c3 = {9,10,11,12,13}
c4 = {3,4,5}
print(c1,c2,c3,c4)
# unir conjuntos, se juntan y los repetidos sólo aparecen una vez
print("\nUnión")
print("c1 unión c2", c1.union(c2))
print("c1 unión c3", c1 | c3)
# aparecen sólo los repetidos
print("\nIntersección")
print("c1 intersección c2", c1.intersection(c2))
print("c2 intersección c3", c2 & c3)
# un conjunto quitarle los conjuntos del otro
print("\nDiferencia")
print("c1 diferencia c4", c1.difference(c4))
print("c2 diferencia c3", c2 - c3)
# si no se repiten en ningún conjunto, aparecen
print("\nDiferencia simétrica")
print("c1 dif simétrica c2", c1.symmetric_difference(c2))
print("c2 dif simétrica c3", c2 ^ c3)
# si es más chico un conjunto que otro, todos los conjuntos del tal están en el tal
print("\nComprobamos subconjuntos")
print("c4 es subconjunto c1", c4.issubset(c1))
print("c3 es subconjunto c2", c3 <= c2)
# al revés de súperconjunto
print("\nComprobamos súperconjuntos")
print("c1 es súperconjunto c4", c1.issuperset(c4))
print("c2 es súperconjunto c3", c2 >= c3)
# verificar si está un número en un conjunto
print("\nVerificar")
print("2 está en c1", 2 in c1)
print("6 no está en c1", 6 is not c1)
