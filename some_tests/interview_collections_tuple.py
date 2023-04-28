"""
1. Можно ли  изменить элемент кортежа?
2. Может ли кортеж являться ключом словаря?
"""
from copy import copy, deepcopy


# 1
a = [5, 6, 7]
lst = [a, 2, 3, True]
new_lst = deepcopy(lst)
print(lst)
a[0] = 'new_value'
print(lst)
print(new_lst)

# 2
dct = {(1, 2): 3}
print(dct)
