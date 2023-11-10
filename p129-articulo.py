import os ; os.system("cls")

class Articulo:
    def __init__(self, id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
    
    def obtenerTotal(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"ID : {self.id}, Descripción : {self.descripcion}, Cantidad : {self.cantidad}, Precio : {self.precio}, Total = {self.obtenerTotal():.2f}"
    
# Programa principal
# Primer objeto
print("Artículo 1")
art1 = Articulo("A101", "Pluma Roja", 888, 0.08)
print(art1)
art1.cantidad = 999
art1.precio = 0.99
print("ID          :  ",art1.id)
print("Descripción :  ",art1.descripcion)
print("Cantidad    :  ",art1.cantidad)
print("Precio      :  ",art1.precio)
print("Total       =  ",art1.obtenerTotal())
# Segundo objeto
art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print("\nArtículo 2")
print(art2)
# Tercer objeto
art3 = Articulo("P103", "Lápiz del 12", 456, 0.5)
print("\nArtículo 3")
print(art3)
# Total de los tres artículos
total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print("\nTotal de los tres artículos = ", total)
