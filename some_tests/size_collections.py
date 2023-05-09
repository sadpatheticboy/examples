from pympler import asizeof

tuples = [('Python', 1991) for _ in range(1_000_000)]
dicts = [{'Python': 1991} for _ in range(1_000_000)]

tuples_size = asizeof.asizeof(tuples)
dicts_size = asizeof.asizeof(dicts)

print('Размер списка с кортежами', tuples_size, 'байт')
print('Размер списка с словарями', dicts_size, 'байт')
