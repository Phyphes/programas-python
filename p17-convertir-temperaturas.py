# Convertir grados celcius a grados farenheit y viceversa

print("Convertir grados Celcius a grados Farenheit y viceversa\n")
opcion = str.upper(input("[C]entigrados a Farenheit\n[F]arenheit a Centigrados\nElije: "))
# opcion = str.upper(opcion) # función que guarda la letra en mayúsculas

if opcion == "C" :
    print("\nConvirtiendo de Farenheit a Centigrados")
    temp = float(input("Grados Farenheit: "))
    res = (temp - 32) * 5 / 9
    print(f"{temp} grados Farenheit equivalen a {res:.2f} grados Centigrados")
else:
    print("\nConvirtiendo de Centigrados a Farenheit")
    temp = float(input("Grados Centigrados: "))
    res = (temp * 9 / 5) + 32
    print(f"{temp} grados Centigrados equivalen a {res:.2f} grados Farenheit")

print("\nProceso terminado...")