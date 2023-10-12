# Crear lista y mostrar datos

import os ; os.system("cls")
#        0    1    2    3    4    5    6    7    8    9
nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
#       -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(nums[0])      # El primero elemento
print(nums[9])      # El último elemento
print(nums[4])      # El elemento : 999
print(nums[1:5])    # Los elementos entre: 123 a 999
print(nums[:4])     # Los elementos desde el inicio hasta el 222
print(nums[3:])     # Los elementos desde 222 hasta el final
print(nums[-3:])    # Los tres úlitmos elementos usando índice negativo
