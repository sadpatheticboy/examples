""" In this lesson, we will cover the basics of magic methods, also known as dunder methods or special methods, in
 Python object-oriented programming.
 Magic methods are special methods in Python that allow you to define how your objects will behave in certain
 situations, such as when they are compared, added, subtracted, printed, or indexed. """


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
#
# print(person1 == person2) # False. This is because the == operator compares the memory addresses of the two objects,
# not their attributes. To make the comparison work based on the attributes of the objects, we can define a magic
# method called __eq__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1 == person2)  # False. This time, the comparison returns False because the name and age attributes of
# the two objects are different.
