""" Условие задачи - https://stepik.org/lesson/701988/step/8?unit=702089 """


class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self, vector):
        return len(vector.__coords)

    def __abs__(self, vector):
        return sum(map(lambda x: x**2, self.__coords)) ** 0.5
