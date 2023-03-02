""" Условие задачи - https://stepik.org/lesson/701986/step/5?unit=702087 """


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    _id_instance = 1

    def __init__(self, name, weight, price):
        self.id = Product._id_instance
        Product._id_instance += 1

        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        d = {'id': type(value) is int, 'name': type(value) is str, 'weight': type(value) in (int, float) and value > 0,
             'price': type(value) in (int, float) and value > 0}
        if d[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)
