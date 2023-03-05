""" Условие задачи - https://stepik.org/lesson/701988/step/7?unit=702089 """


class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.real**2 + self.img**2)**1/2


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
