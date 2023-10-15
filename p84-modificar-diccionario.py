# Crear diccionario de llaves de cadena países

import os ; os.system("cls")

paises = {
    'Argentina' : 100,
    'Brasil' : 200,
    'Colombia' : 300,
    'Chile' : 400,
    'Ecuador' : 500,
    'Bolivia' : 600,
    'Jamaica' : 700 
}

print(f"\nDiccionario original: \n{paises}",len(paises))
paises['Brasil'] = 250              # modificando usando []
paises['Chile'] = 450               # modificando usando []
paises.update({'Bolivia' : 650})    # modificando usando update
paises.update({'Jamaica' : 750})    # modificando usando update
print(f"\nDiccionario modificado: \n{paises}",len(paises))