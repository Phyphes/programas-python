# Examen Primer Parcial

import os
os.system("cls")

total = 0 ; importe_total = 0
alumno = 100 ; trabajador = 200 ; docente = 500 ; conferencias = 600 ; eventos_sociales = 800 ; kit_acceso = 900

while True:
    
    print("\nUniversidad Patito SA de CV")
    print("Sistema de Inscripción Congreso de Sistemas")

    tipo_usuario = int(input("\nTipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 = "))
    tipo_paquete = int(input("Tipo de paquete: [1] Conferencias $600, [2] Eventos Sociales $800, [3] Kit de Acceso $900 = "))
    cantidad = int(input("Cantidad de Inscripciones = "))
    subtotal = 0 ; descuento = 0 ; 

    # Tipo usuario 1 y tipo de paquete 1
    if tipo_usuario == 1 and tipo_paquete == 1:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Alumno $100, Tipo de paquete: Conferencias $600")
        subtotal = (alumno + conferencias) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.20
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (20%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    # Tipo usuario 1 y tipo de paquete 2
    if tipo_usuario == 1 and tipo_paquete == 2:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Alumno $100, Tipo de paquete: Eventos Sociales $800")
        subtotal = (alumno + eventos_sociales) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.20
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (20%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    # Tipo de usuario 1 y tipo de paquete 3
    if tipo_usuario == 1 and tipo_paquete == 3:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Alumno $100, Tipo de paquete: Kit de Acceso $900")
        subtotal = (alumno + kit_acceso) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.20
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (20%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    # Tipo de usuario 2 y tipo de paquete 1
    if tipo_usuario == 2 and tipo_paquete == 1:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Trabajador $200, Tipo de paquete: Conferencias $600")
        subtotal = (trabajador + conferencias) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.10
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (10%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    # Tipo de usuario 2 y tipo de paquete 2
    if tipo_usuario == 2 and tipo_paquete == 2:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Trabajador $200, Tipo de paquete: Eventos Sociales $800")
        subtotal = (trabajador + eventos_sociales) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.10
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (10%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    # Tipo de usuario 2 y tipo de paquete 3
    if tipo_usuario == 2 and tipo_paquete == 3:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Trabajador $200, Tipo de paquete: Kit de Acceso $900")
        subtotal = (trabajador + kit_acceso) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.10
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (10%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    # Tipo de usuario 3 y tipo de paquete 1
    if tipo_usuario == 3 and tipo_paquete == 1:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Docente $500, Tipo de paquete: Conferencias $600")
        subtotal = (docente + conferencias) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.05
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (5%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total
        
    # Tipo de usuario 3 y tipo de paquete 2
    if tipo_usuario == 3 and tipo_paquete == 2:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Docente $500, Tipo de paquete: Eventos Sociales $800")
        subtotal = (docente + eventos_sociales) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.05
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (5%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total
       
    # Tipo de usuario 3 y tipo de paquete 3
    if tipo_usuario == 3 and tipo_paquete == 3:
        print(f"Tu pedido fue = {cantidad} inscripciones, Tipo de usuario: Docente $500, Tipo de paquete: Kit de Acceso $900")
        subtotal = (docente + kit_acceso) * cantidad
        if subtotal >= 5000:
            descuento = subtotal * 0.05
            total = subtotal - descuento
            print(f"Subtotal: {subtotal}, con un descuento de {descuento} (5%) por lo que el total sería {total}")
        else:
            total = subtotal
            print(f"Total: {total}")
        importe_total = total + importe_total

    res = input("\n¿Deseas continuar? (S/N) ").upper()
    if res == "N" : break

print(f"\nImporte total de la venta: {importe_total}")
print("\nProceso terminado...")
