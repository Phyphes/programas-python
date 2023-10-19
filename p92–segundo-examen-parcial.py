# Se desea procesar el pedido de una pizza en base a sus ingredientes, cada ingrediente tiene un precio

import os ; os.system("cls")

print("Bienvenidx a Chisi Pizza")

ingredientes = {
    'T' : 1.50, # tomate
    'P' : 3.50, # peperonni
    'A' : 0.40, # aguacate
    'Q' : 3.74, # queso
    'I' : 2.10, # piña
}

subtotal = 0
total = 0
orden = (input("\nIngredientes de tu pizza: ")).upper()

if orden == "" :
    print("Su precio base es de $15, ¡una compra de más de $30 obtienes descuento del 5%!")
    print("-------------------------------M E N Ú----------------------------------------")
    for k,v in ingredientes.items():
        print(f"{k:<1} - $ {v} ")
else:
    for ing in orden:
        if ing not in 'TPAQI':
            print("\n¡No seleccionaste ingredientes válidos!")
            exit()
        if ing in 'TPAQI':
            subtotal += ingredientes[ing]
    subtotal = subtotal + 15
            
    if subtotal >= 30:
        total = subtotal - (subtotal * 0.05)
        print(f'Subtotal : {subtotal:.2f}')
        print(f'Total con descuento del 5% : {total:.2f}')
    else:
        total = subtotal
        print(f'Total : {total:.2f}')


