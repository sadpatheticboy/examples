class Name:
    def __get__(self, obj, objtype=None):
        if obj:
            return obj.__name.capitalize()

    def __set__(self, obj, name):
        obj.__name = name.lower()


class Color:
    __colors = ['unset', 'black', 'white', 'mixed']

    def __set__(self, obj, color):
        try:
            color = Color.__colors.index(color)
        except ValueError:
            if isinstance(color, int) and 0 <= color <= len(Color.__colors) - 1:
                pass
            else:
                color = 0

        obj.__color = color

    def __get__(self, obj, objtype=None):
        return Dog.__colors[obj.__color]

    def __delete__(self, obj):
        obj.color = 0


class Breed:
    was_set = False

    def __get__(self, obj, objtype=None):
        if obj:
            return obj.__breed

    def __set__(self, obj, breed):
        if not self.was_set:
            obj.__breed = breed
            self.was_set = not self.was_set
        else:
            raise AttributeError


class Dog:
    name = Name()
    color = Color()
    breed = Breed()

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed


some_dog = Dog('Sharik', 'color', 'wss')
some_dog.name = 'Rex'
print(some_dog.name)
