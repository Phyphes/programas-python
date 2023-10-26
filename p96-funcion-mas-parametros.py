# Función que recibe un número arbitrario de parámetros

import os ; os.system("cls")

def saludatodos(*todos):
    print("Saludos a : ", todos)
    for nombre in todos:
        print("Hola", nombre)
    if len(todos) !=0:
        print("El primero es el primero y es", todos[0])
        print("El último es el último y es", todos[-1])

saludatodos("Juan", "Pedro", "Luis", "José")