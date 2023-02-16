lst = [int(input('Элемент массива:')) for i in range(int(input('Количество элементов в массиве:')))]

count = sum([1 for i in lst if i < 0])

c, d = int(input('Левая граница отрезка:')), int(input('Правая граница отрезка:'))
new_lst = [lst.index(i) for i in lst if c < i < d]

print(f'Исходный массив: {lst}')
print(f'Количество отрицательных элементов в исходном массиве: {count}')
print(f'Новый массив из индексов элементов исходного массива, принадлежащих отрезку ({c}, {d}): {new_lst}')
