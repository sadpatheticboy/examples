""" Create a class Shape with a method area that returns 0, and a class Square that inherits from Shape and has
 a constructor that takes a side length and sets it as an attribute. Override the area method in the Square class
 to return the area of the square (i.e., side length squared). """


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


square = Square(5)
print(square.area()) # Output: 25

