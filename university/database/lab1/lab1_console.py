try:
    lst = [int(input('Элемент массива:')) for i in range(int(input('Количество элементов в массиве:')))]
    count = sum([1 for i in lst if i < 0])

    c, d = int(input('Левая граница отрезка:')), int(input('Правая граница отрезка:'))
    new_lst = [i for i in range(len(lst)) if c <= lst[i] <= d]

    print(f'Исходный массив: {lst}')
    print(f'Количество отрицательных элементов в исходном массиве: {count}')
    if len(new_lst) != 0:
        print(f'Новый массив из индексов элементов исходного массива, принадлежащих отрезку [{c}, {d}]: {new_lst}')
    else:
        print(f'Новый массив не сформулировался, нет подходящих значений.')
except:
    print('Неккоректные значения.')
