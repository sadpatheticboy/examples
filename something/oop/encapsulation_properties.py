class Dog:
    __colors = ['unset', 'black', 'white', 'mixed']

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.__breed = breed

    def get_name(self):
        return self.__name.capitalize()

    def set_name(self, name):
        self.__name = name

    @property  # 2 вариант
    def breed(self):
        return self.__breed

    def set_color(self, color):
        try:
            color = Dog.__colors.index(color)
        except ValueError:
            if isinstance(color, int) and 0 <= color <= len(Dog.__colors) - 1:
                pass
            else:
                color = 0

        self.__color = color

    def get_color(self):
        return Dog.__colors[self.__color]

    def del_color(self):
        self.color = 0

    name = property(get_name, set_name)  # 1 вариант
    color = property(get_color, set_color, del_color)



