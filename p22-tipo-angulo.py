# Muestra el tipo de angulo
# <90 agudo, =recto, <90 y <100 obtuso, -180 llano, >100 y <360 concavo, =360 completo

import os ; os.system("cls")

angulo = int(input("Dame el ángulo: ")) 

if angulo >= 0 and angulo <= 360:
    print("continuando...\n")
    if angulo < 90:
        print("tipo de ángulo: agudo")
    elif angulo == 90:
        print("tipo de ángulo: recto")
    elif angulo > 90 and angulo < 180:
        print("tipo de ángulo: obtuso")
    elif angulo == 180:
        print("tipo de ángulo: llano")
    elif angulo > 180 and angulo < 360:
        print("tipo de ángulo: concavo")
    else: 
        print("tipo de ángulo: completo")
else: 
    print("\nángulo fuera de rango")