""" For this task, let's say we want to create a class hierarchy for different types of animals. We'll start with
 a superclass Animal, which will have some basic attributes and methods that all animals share. Then we'll create two
 subclasses Mammal and Bird, each with their own unique attributes and methods. """


# My solution
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Mammal(Animal):
    def __init__(self, name, age, sound, num_legs):
        super().__init__(name, age, sound)
        self.num_legs = num_legs

    def nurse_young(self):
        print("This mammal is nursing its young.")


class Bird(Animal):
    def __init__(self, name, age, sound, flight_altitude):
        super().__init__(name, age, sound)
        self.flight_altitude = flight_altitude

    def fly(self):
        print("This bird is flying at an altitude of", self.flight_altitude, "meters.")


# Tests
dog = Mammal("Rufus", 3, "Woof!", 4)
bird = Bird("Tweety", 1, "Chirp chirp!", 1000)

dog.make_sound()  # prints "Woof!"
bird.make_sound()  # prints "Chirp chirp!"

dog.nurse_young()  # prints "This mammal is nursing its young."
bird.fly()  # prints "This bird is flying at an altitude of 1000 meters."
