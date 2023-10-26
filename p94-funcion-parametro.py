# Función con parámetros

import os ; os.system("cls")

def saluda(nombre, edad):
    print(f"Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres y tu edad es {edad}")

# Programa principal 
saluda("Carlos Castañeda", 30)
saluda("Juan Perez Díaz", 10)
saluda("María Soto García", 25)
saluda("AMLO", 76)
# print(nombre) - los parámetros no son accesibles fuera de la función