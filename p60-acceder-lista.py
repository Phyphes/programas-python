# Acceder a los elementos de una lista

import os ; os.system("cls")
#       0    1   2  3   4   5   6   7   8
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
#       -9  -8  -7  -6  -5  -4  -3  -2  -1
print(nums, len(nums)) # imprime la lista y su longitud
print(nums[0], nums[8]) 
print(nums[2:6])
print(nums[:3])
print(nums[6:])
print(nums[5], nums[-4])