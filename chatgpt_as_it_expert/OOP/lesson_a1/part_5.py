""" For this task, you will create a class called Rectangle that represents a rectangle shape. The class should have the
    following methods:
    1. __init__(self, length, width): Initializes a new rectangle object with the given length and width.
    2 area(self): Returns the area of the rectangle.
    3. perimeter(self): Returns the perimeter of the rectangle.
    4. is_square(self): Returns True if the rectangle is a square (length and width are equal), False otherwise."""


# My solution
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def is_square(self):
        return self.width == self.length
