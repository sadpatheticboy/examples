""" __add__: This method is used to define the behavior of the + operator in our class. It takes two arguments self
and other and should return the result of the addition. Here is an example: """


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


""" __sub__: This method is used to define the behavior of the - operator in our class. It takes two arguments self 
  and other and should return the result of the subtraction.
    __mul__: This method is used to define the behavior of the * operator in our class. It takes two arguments self
  and other and should return the result of the multiplication.
    __eq__: This method is used to define the behavior of the == operator in our class. It takes two arguments self
  and other and should return True if the two objects are equal and False otherwise. 
    __len__: This method is used to define the behavior of the len() function in our class. It takes one argument self
  and should return the length of the object.
    __getitem__: This method is used to define the behavior of indexing in our class. It takes two arguments self and
  index and should return the value at the given index.
    __setitem__: This method is used to define the behavior of setting values by indexing in our class. It takes three
  arguments self, index, and value and should set the value at the given index to the given value.
    __getattr__: This method is used to define the behavior when an attribute is not found in our class. It takes two
  arguments self and name and should return the value of the attribute if it exists or raise an AttributeError
  otherwise. """


class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __getattr__(self, name):
        if name == 'total':
            return sum(item.price for item in self.items)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def add_item(self, item):
        self.items.append(item)
