# Remover lista

import os ; os.system("cls")
#        0    1    2    3    4    5    6    7    8    9
nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
#       -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(nums)             # Lista inicial
del nums[0:3]           # Remover 100, 123, 456
print(nums)             # Mostrar
nums.remove(322)        # Remover 322
nums.remove(988)        # Remover 988
print(nums)             # Mostrar
nums.pop(0)             # Remover 222
print(nums)             # Mostrar
nums.pop()              # Remover el último elemento de la fila
print(nums)             # Mostrar
nums.clear()            # Vaciar lista
print(nums,len(nums))   # Mostrar