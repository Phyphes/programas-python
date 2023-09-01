# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos

print("Dada una cantidad de horas, calculando su equivalente en días, minutos y segundos\n")

horas = float(input("Dame las horas que quieras convertir: "))

dias = 1 / 24 * (horas)
minutos = horas * 60
segundos = minutos * 60

print(f"\n{horas} horas equivalen a {dias:.2f} días")
print(f"{horas} horas equivalen a {minutos:.2f} minutos")
print(f"{horas} horas equivalen a {segundos:.2f} segundos")
