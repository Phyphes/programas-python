# Función con parámetros con valores por defecto o valores preestablecidos

import os ; os.system("cls")

def saluda(nombre="Juan", edad=18):
    print(f"Hola {nombre}, tu edad es {edad}")

saluda()
saluda("Rocío")
saluda("Carlos", 51)