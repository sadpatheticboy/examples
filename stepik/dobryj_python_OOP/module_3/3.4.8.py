""" Условие задачи - https://stepik.org/lesson/701989/step/8?unit=702090 """


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.book_list)
