""" Усвлоие задачи - https://stepik.org/lesson/701988/step/5?unit=702089 """


class WordString:
    def __init__(self, string=''):
        self.__word = string

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx):
        l = self.__word.split()
        return l[indx]

    @property
    def string(self):
        return self.__word

    @string.setter
    def string(self, s):
        self.__word = s
