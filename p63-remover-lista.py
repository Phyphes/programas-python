# Remover elementos de la lista 

import os; os.system("cls")

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]

print(nums,len(nums))
nums.remove(99) # elimina el elemento que especificas
print(nums,len(nums))
nums.pop(8) # elimina el elemento en esa posición
print(nums,len(nums))
nums.pop() # elimina el elemento de la última posición
print(nums,len(nums))
nums.clear()
print(nums,len(nums))
