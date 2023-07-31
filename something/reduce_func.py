from functools import reduce

ls = [1, 2, 3, 4, 5, 6]
dc = {0: 1, 1: 2, 2: 3}
ds = {'a': 'январь', 'b': 'февраль', 'c': 'март'}

print(sum(ls))

print(reduce(lambda a, b: (a + b), ls))
