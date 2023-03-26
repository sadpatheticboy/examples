""" Encapsulation is the idea of bundling data and methods that operate on that data within a single unit, such as a
 class. This means that the data is kept private and can only be accessed through methods provided by the class.
 In Python, encapsulation is implemented using the following convention:
  1. Attributes and methods that are intended to be private should be prefixed with a double underscore (__).
  2. Attributes and methods that are intended to be protected should be prefixed with a single underscore (_). """


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
