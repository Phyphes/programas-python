# Calcula la paga de un trabajador, las horas extras se pagan el doble

print("Calcula la paga de un trabajador, las horas extras se pagan el doble\n")

nombre = input("Nombre: ")
horas = int(input("Horas trabajadas: "))
paga = float(input("Paga por hora: "))
extra = 0

if horas > 40:
    extra = horas - 40
    total = (40 * paga) + (2 * paga * extra)
else:
    total = horas * paga

print(f"{nombre} trabajó {horas} horas, con una paga de {paga} con horas extra de {extra}, dando un total de paga de {total:.2f}")
