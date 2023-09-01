# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte
# Mostrar los dígitos individuales y el número de la suerte

print("Dado el año de nacimiento, mostrar los dígitos individualmente y el número de la suerte\n")

año_nac = int(input("Dime tu año de nacimiento: "))

unidad_mil = año_nac // 1000
centenas = (año_nac - unidad_mil * 1000) // 100
decenas = (año_nac - (unidad_mil * 1000 + centenas * 100)) // 10
unidades = año_nac - (unidad_mil * 1000 + centenas * 100 + decenas * 10)

print(f"\nPrimer dígito de tu año de nacimiento es: {unidad_mil}")
print(f"Segundo dígito de tu año de nacimiento es: {centenas}")
print(f"Tercer dígito de tu año de nacimiento es: {decenas}")
print(f"Cuarto dígito de tu año de nacimiento es: {unidades}")

print(f"\nTú numero de la suerte basado en tu año de nacimiento es {unidad_mil+centenas+decenas+unidades}")