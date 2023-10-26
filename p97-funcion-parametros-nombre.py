# Función que al ser invocada usa el nombre del parámetro

import os ; os.system("cls")

def saluda(apaterno, amaterno, nombre):
    print(f"Paterno: {apaterno}, Materno: {amaterno}, Nombre: {nombre}")

saluda("Castañeda", "Ramírez", "Carlos")
saluda(nombre="Carlos", apaterno="Castañeda", amaterno="Ramírez")
saluda(amaterno="Bernal", nombre="Rocío", apaterno="Soto")