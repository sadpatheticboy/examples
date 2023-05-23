from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple

# # OrderedDict
# # Нужен для действий со словарем, где необходим порядок элементов,
# # например, сравнение с учётом порядка, перестановка элементов с сохранением порядка.
# # Этот словарь занимает сильно больше памяти, чем встроенный
# first = {1: 1, 2: 2, 3: 3}
# second = {2: 2, 1: 1}
# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
# print(first == second)  # Встроенный словарь при сравнении не смотрит на порядок, только на значения
# print(order1 == order2)  # OrderedDict смотрит и на значения, и на порядок
# print(order1.popitem(last=False))  # Есть методы, которые нет у встроенного
#
# order1.move_to_end(1)  # также можно в начало перенести .move_to_end(key, last=False)
# print(order1)


# # ChainMap
# # Нужен для логического объединения нескольких словарей для поиска информации, но при любых изменениях
# # меняется только первый словарь
# first = {1: 1, 2: 2, 3: 3}
# second = {4: 4, 5: 5}
# chain = ChainMap(first, second) # Никакого копирования нет,  только ссылки
#
# print(chain)
# print(5 in chain)
# chain[5] = 200
# print(chain)


# # Counter
# # Counter считает только с hashable объекты. Нужен для подсчёта элементов в последовательности
# counter = Counter('hello')
# print(counter)
# counter.update('world')
# counter.most_common(1) # Наиболее повторяющийся элемент


# # defaultdict
# # Нужен для создания словаря со значением по умолчанию. Значение подставляется при обращении к несуществующему ключу
# a_dict = defaultdict(int)
# for char in 'hello':
#     a_dict[char] += 1
#
# print(a_dict)
# print('adad' in a_dict)


# # deque
# # deque потокобезопасна, быстро оперирует с обеими сторонами
# a_deque = deque()
# a_deque.append(1) # pop
# print(a_deque)
# a_deque.appendleft(2) # popleft
# print(a_deque)
#
# b_deque = deque([1, 2, 3], maxlen=3)
# print(b_deque)
# b_deque.append(4)
# print(b_deque)


# # namedtuple
# # Нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом
# # Неизменяемый, позволяет обращаться по имени атрибута и индексу
# Cat = namedtuple('Cat', 'name age color')
# tom = Cat('Tom', 4, 'black')
# print(tom)
# print(tom[0])
# print(tom.name)
