""" In this lesson, we will focus on the following magic methods:
     1. __repr__: defines the string representation of an object (used for debugging and development)
     2. __eq__: defines the equality comparison between two objects
     3. __lt__ and __gt__: define the less than and greater than comparisons between two objects
     4. __len__: defines the behavior when the len built-in function is called on an object. """


class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyClass(name='{self.name}')"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return False

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return False
