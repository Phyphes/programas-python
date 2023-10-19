# Crear dos conjuntos y mostrar lo que se pide

import os ; os.system("cls")

A = {'Juan', 'María', 'Pedro', 'José', 'Rocío'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print("\nLos conjuntos son:")
print("A =", A, len(A))
print("B =", B, len(B))

print("\nUnión:")
print("A | B =", A.union(B), len(A | B))

print("\nIntersección:")
print("A & B =", A.intersection(B), len(A & B))

print("\nDiferencia:")
print("A - B =", A.difference(B), len(A - B))

print("\nDiferencia simétrica:")
print("A ^ B =", A.symmetric_difference(B), len(A ^ B))

print("\nComprobamos subconjunto:")
print("{'Pablo', 'Mateo'} subconjunto de B =", {'Pablo', 'Mateo'}.issubset(B))

print("\nComprobamos súperconjunto:")
print("A súperconjunto de {'Reynaldo', 'Angélica'} =", A >= {'Reynaldo', 'Angélica'})

print("\nVerificar:")
print("Si Pedro está en A =", 'Pedro' in A)
print("Si Lilia no está en B =", 'Lilia' is not B)
