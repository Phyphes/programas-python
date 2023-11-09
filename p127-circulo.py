import os ; os.system("cls")
import math

class Circulo:
    def __init__(self, radio): # constructor y un parámetro
        self.radio = radio
    
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Radio = {self.radio:.2f}, Área = {self.obtenerArea():.2f}, Circunferencia = {self.obtenerCircunferencia():.2f}"
    

circulo1 = Circulo(10.40)
print(circulo1)
print(f"El radio : {circulo1.radio:.2f}")
print(f"El área : {circulo1.obtenerArea():.2f}")
print(f"La circunferencia : {circulo1.obtenerCircunferencia():.2f}")

circulo2 = Circulo(12.45)
print(f"\n{circulo2}")
print(f"El radio : {circulo2.radio:.2f}")
print(f"El área : {circulo2.obtenerArea():.2f}")
print(f"La circunferencia : {circulo2.obtenerCircunferencia():.2f}")

circulo3 = Circulo(100)
print(f"\n{circulo3}")
print(f"El radio : {circulo3.radio:.2f}")
print(f"El área : {circulo3.obtenerArea():.2f}")
print(f"La circunferencia : {circulo3.obtenerCircunferencia():.2f}")

areatotal = circulo1.obtenerArea() + circulo2.obtenerArea() + circulo3.obtenerArea()
print(f"\nEl área total de los círculos es {areatotal:.2f}")