""" Polymorphism is the idea that objects of different classes can be treated as if they were of the same class.
 This allows us to write more flexible and reusable code. Polymorphism in Python is implemented using a combination of
 inheritance and method overriding. When a subclass inherits from a superclass, it can override methods in the
 superclass with its own implementation.
 This allows the subclass to provide a different behavior for the same method. """


class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

make_animal_sound(dog)  # Output: "Woof!"
make_animal_sound(cat)  # Output: "Meow!"
