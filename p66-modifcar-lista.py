# Modificar lista y mostrar lista resultante

import os ; os.system("cls")
#        0    1    2    3    4    5    6    7    8    9
nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
#       -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(nums)                   # Lista inicial
nums[0] = 200                 # 100 por 200
nums[4] = nums[4] + 1         # 999 por 1000
nums[9] = 999                 # 999 por 1000
nums[1:4] = [555, 666, 777]   # 123,456,222 por 555,666,777
print(nums)                   # Lista resultante 