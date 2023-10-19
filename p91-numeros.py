# Crear tres conjuntos y mostrar lo que se pide

import os ; os.system("cls")

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print("\nLos conjuntos son:")
print("A =", A, len(A))
print("B =", B, len(B))
print("C =", C, len(C))

print("\nUnión:")
print("A | B =", A.union(B), len(A | B))
print("B | C =", B.union(C), len(B | C))

print("\nDiferencia:")
print("A - C =", A.difference(C), len(A - C))

print("\nDiferencia simétrica:")
print("B ^ C =", B.symmetric_difference(C), len(B ^ C))

print("\nIntersección:")
print("B & C =", B.intersection(C), len(B & C))

print("\nComprobamos subconjunto:")
print("A subconjunto de B =", (A).issubset(B))
print("C subconjunto de A =", (C).issubset(A))

print("\nVerificar:")
print("Si 100 está en A =", 100 in A)
print("Si 60 está en A, B y C =", 60 in (A and B and C))
print("Si 900 no está en C =", 900 is not C)
