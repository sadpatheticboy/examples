from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    """
     Функция принимающая итерируемый объект, с любым уровнем вложенности другими итерируемыми
      объектами, и формирующая плоскую последовательность
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8, ('A', {'B', 'C'})]

for x in flatten(items):
    print(x)
