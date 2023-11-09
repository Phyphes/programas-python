import os ; os.system("cls")

class Empleado: # clase
    def __init__(self, nombre, edad, sexo, casado): # constructor y  parámetros
        self.nombre = nombre # atributo y parámetro
        self.edad = edad
        self.sexo = sexo
        self.casado = casado

    def __str__(self): # regresa una cadena de las variables para imprimir en la pantalla
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {'Mujer' if self.sexo == 'M' else 'Hombre'}, Casado: {'Casado' if self.casado else 'No casado'}"
    
# Programa principal
# Primer objeto
emp1 = Empleado("José Díaz", 35, "H", True)
print(emp1)
# Segundo objeto
emp2 = Empleado("María López", 22, "M", False)
print(emp2)
# Tercer objeto
emp3 = Empleado("Rosario Valenzuela", 15, "M", True)
print(emp3)
# Cuarto objeto
emp4 = Empleado("Juan Perez", 20, "H", False)
print(emp4)

prom = (emp1.edad + emp2.edad + emp3.edad) / 4
print("\nPromedio de edades de los empleados : ", prom)

print(f"\nLos nombres son : {emp1.nombre}, {emp2.nombre}, {emp3.nombre}, {emp4.nombre}")

if(emp2.casado == False and emp4.casado == False):
    print (f"\n{emp2.nombre} se puede casar con {emp4.nombre} ambos son solteros")
if(emp1.casado == True and emp3.casado == True):
    print (f"{emp1.nombre} no se puede casar con {emp3.nombre} ambos son casados")