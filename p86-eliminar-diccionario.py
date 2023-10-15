# Cree un diccionario de llave de cadena municipios

import os ; os.system("cls")

municipios = {
    'Apozol' : 1863,
    'Calera' : 1868,
    'Fresnillo' : 1554,
    'Guadalupe' : 1821,
    'Jalpa' : 1824,
    'Jerez' : 1824,
    'Loreto' : 1931,
    'Mazapil' : 1824,
    'Momax' : 1857,
}

print(f"\nDiccionario inicial: \n{municipios}",len(municipios))
del(municipios['Apozol'])           # remover usando del
print(municipios,len(municipios))   
municipios.pop('Fresnillo')         # remover usando pop
print(municipios,len(municipios))
municipios.popitem()                # remover usando popitem
print(municipios,len(municipios))
municipios.clear()                  # vaciar diccionario
print(f"\nDiccionario final: \n{municipios}",len(municipios))
