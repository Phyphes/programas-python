import p120funciones as pf

l1 = pf.leer()
may = pf.mayor(l1)
men = pf.menor(l1)
sum = pf.suma(l1)
pro = pf.promedio(l1)

print("La lista es :", l1)
print("El mayor es", may, ", el menor es", men)
print("La suma es", sum, ", el promedio es", pro)