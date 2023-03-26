""" Inheritance is a fundamental feature of object-oriented programming. It allows you to create a new class that is
 a modified version of an existing class. The new class inherits all the attributes and methods of the existing class,
 and you can add new attributes and methods or modify the existing ones. """


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!")
