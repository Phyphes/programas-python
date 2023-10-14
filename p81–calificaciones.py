# Juntar dos listas a un diccionario

import os ; os.system("cls")

materias = ['Física', 'Química', 'Matemáticas', 'Geografía', 'Estadística']
calificaciones = [10, 9, 8, 7.5, 6]

print('Lista de materias        :',materias)
print('Lista de calificaciones  :',calificaciones)
notas = dict(zip(materias,calificaciones))
print("\nLas notas:",notas,len(notas))
notas.update({'Inglés': 10})
notas.update({'Programación': 7})
print("\nDiccionario actualizado: ",notas,len(notas))
notas.pop('Física')
notas.popitem()
print("\nDiccionario actualizado: ",notas,len(notas))
notas.update({'Química': 10})
notas.update({'Matemáticas': 10})
print("\nDiccionario actualizado: ",notas,len(notas))

s = p = 0
for m, c in notas.items():
    print(f"{m:<12} - {c:>5.2f}")
    s = s + c
p = s / len(notas)
print(f"\nLa suma es {s} y el promedio es {p}")
