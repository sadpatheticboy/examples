""" The init method is called a constructor method in Python. It is executed automatically when an object is created
from a class. It initializes the attributes of the object with default or user-defined values. """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)


p1 = Person("Alice", 25)
p1.display()  # Output: Name: Alice Age: 25
