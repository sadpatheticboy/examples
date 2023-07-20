class Dog:
    __bark_sound = 'bark!'
    __count = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.__count += 1

    @classmethod
    def get_total_count(cls):
        return cls.__count

    @classmethod
    def bark(cls):
        print(cls.__bark_sound)

    @classmethod
    def create_from_string(cls, dog_string):
        name, breed = dog_string.split(':')
        return cls(name, breed)

    @staticmethod
    def calculate_age_in_dog_years(age):
        dog_years = age * 7
        return dog_years


# Dog.bark()
#
# d = Dog('Pushok', 'WSS')
# d.bark()
#
# d._Dog__bark_sound = 'woof!'
# d.bark()
# print(d._Dog__bark_sound)

some_dog = 'Buddy:Golden Retriever'
buddy = Dog.create_from_string(some_dog)
print(buddy.name)
