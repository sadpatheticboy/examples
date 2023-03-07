""" Условие задачи - https://stepik.org/lesson/701989/step/9?unit=702090 """


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other

    def __radd__(self, other):
        return self.__add__(other)


class Budget:
    def __init__(self):
        self.bud = []

    def add_item(self, it):
        self.bud.append(it)

    def remove_item(self, indx):
        self.bud.pop(indx)

    def get_items(self):
        return self.bud

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    print(type(x))
    s = s + x

print(s)