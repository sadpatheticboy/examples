s = 'Строка'
s_itr = iter(s)
print(s_itr)  # <str_iterator object at 0x000001C89EB63EB0>

s_itr.__next__()  # == next(s_itr)
s_itr.__next__()
s_itr.__next__()
print(s_itr.__reduce__())  # (<built-in function iter>, ('Строка',), 3). 3 - индекс следующего элемента

s_itr.__next__()
print(s_itr.__reduce__())  # (<built-in function iter>, ('Строка',), 4)


class Iter:
    def __init__(self, n):
        self.n = n
        self.current = -1

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current


some_iter = Iter(5)
for i in some_iter:
    print(i)
