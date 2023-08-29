# Lee datos del usuario y envia un saludo a pantalla

print("Leyendo datos y enviando un mensaje a pantalla \n")

nombre = input("Dame tu nombre: ")
edad   = int(input("Dame tu edad: "))
peso   = float(input("Dame tu peso: "))

print(f"\nTu nombre es {nombre}, tu edad es {edad} y tu peso es {peso} \n")

print(type(nombre))
print(type(edad))
print(type(peso))
