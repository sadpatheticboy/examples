"""   In this lesson, we'll explore another key concept in object-oriented programming: inheritance.
 Inheritance is the process by which one class can inherit attributes and methods from another class. The class that
 is being inherited from is called the parent class, and the class that inherits from it is called the child class
 (or subclass).
 To create a subclass, we use the class keyword followed by the name of the subclass and the name of the parent class
 in parentheses. """


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed

    def make_sound(self):
        return "Woof!"


my_dog = Dog("Rufus", "Golden Retriever")
print(my_dog.name)      # This will print "Rufus"
print(my_dog.species)   # This will print "Canine"
print(my_dog.breed)     # This will print "Golden Retriever"
print(my_dog.make_sound())  # This will print "Woof!"
