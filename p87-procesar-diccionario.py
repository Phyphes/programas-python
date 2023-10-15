# Lista nombres y lista sueldos, juntar en un diccionario

import os ; os.system("cls")

nombres = ['Juan', 'Pedro', 'Manuel', 'Elías', 'María', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

print('Lista de nombres : ',nombres)
print('Lista de sueldos : ',sueldos)

ns = dict(zip(nombres,sueldos))
print("\nNombre y sueldo: ",ns,len(ns))

# Iteraciones
print("\nLas llaves: ")
for k in ns.keys():
    print(k,end=" ")

s = p = 0
print("\nLos valores: ")
for v in ns.values():
    print(v,end=" ")
    s = s + v

print("\nLlaves y valores: ")
for k,v in ns.items():
    print(f"{k:<7} : {v}")

p = s / len(ns)
print(f"\nLa suma de los sueldos es {s} y el promedio es {p:.2f}")