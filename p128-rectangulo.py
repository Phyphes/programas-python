import os ; os.system("cls")

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def obtenerArea(self):
        return self.largo * self.ancho
    def obtenerPerimetro(self):
        return 2 * self.largo + 2 * self.ancho
    def __str__(self):
        return f"Largo = {self.largo}, Ancho = {self.ancho}, Área = {self.obtenerArea():.2f}, Perímetro = {self.obtenerPerimetro():.2f}"

r1 = Rectangulo(12, 3.4)
print(r1)
print(f"Largo = {r1.largo}, Ancho = {r1.ancho}")
print(f"El área      = {r1.obtenerArea():.2f}")
print(f"El perímetro = {r1.obtenerPerimetro():.2f}")

r2 = Rectangulo(5.6, 7.8)
print(f"\n{r2}")
print(f"Largo = {r2.largo}, Ancho = {r2.ancho}")
print(f"El área      = {r2.obtenerArea():.2f}")
print(f"El perímetro = {r2.obtenerPerimetro():.2f}")

rectangulos = []
rectangulos.append(r1)
rectangulos.append(r2)
print(rectangulos)