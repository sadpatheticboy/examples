""" In this part, we will learn about inheritance in Python. Inheritance is a way of creating a new class by using
 an existing class's methods and attributes. The existing class is called the parent class, while the new class is
  called the child class. """


# class Animal:
#     def speak(self):
#         print("Animal is speaking")
#
#
# class Dog(Animal):
#     pass
#
#
# my_dog = Dog()
# my_dog.speak() # Output: "Animal is speaking"


class Animal:
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def speak(self):
        print("Dog is barking")


my_dog = Dog()
my_dog.speak()  # Output: "Dog is barking"
