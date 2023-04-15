class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        print(f"{self.name} says {sound}")


class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        super().speak(sound)


dog = GoldenRetriever('Sharik', 12)

dog.speak()
