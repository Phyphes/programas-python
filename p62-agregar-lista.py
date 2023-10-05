# Agregar elementos a una lista

import os ; os.system("cls")

nums = [80.3, 12.5, 60.2, 30.4]
otros = [110, 120, 130]

print(nums, len(nums))
nums.append(90) # agrega número a la lista al final
nums.append(100)
print(nums, len(nums))
nums.insert(4,80) # agrega número a la lista en la posición que quieras
print(nums, len(nums))
nums.extend(otros) # agrega una lista al final a otra lista
print(nums,len(nums))
