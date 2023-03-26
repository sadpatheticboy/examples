""" In this lesson, we'll explore another powerful concept in object-oriented programming: polymorphism.
 Polymorphism is the ability of objects to take on many forms. In object-oriented programming, it means that different
 objects can be treated as if they were of the same class, even if they are instances of different subclasses. This is
 possible because of inheritance and method overriding.
 Method overriding is the process by which a subclass can provide a different implementation of a method that is already
 defined in its parent class. When a method is called on an object, Python looks for the method in the class of
 the object. If it's not found there, it looks in the parent class, and so on, until it finds the method or reaches the
 top of the class hierarchy. """


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"


animals = [Dog("Rufus"), Cat("Fluffy"), Cow("Bessie")]

for animal in animals:
    print(animal.name + ": " + animal.make_sound())
