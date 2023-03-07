""" Условие задачи - https://stepik.org/lesson/701989/step/10?unit=702090 """


class Box3D:
    def __init__(self, width, height, depth ):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __sub__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __mul__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return Box3D(self.width / other, self.height / other, self.depth / other)

    def __floordiv__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        if not isinstance(other, (int, float,  Box3D)):
            raise ArithmeticError
        return Box3D(self.width % other, self.height % other, self.depth % other)
