""" In this lesson, we'll be exploring the concept of encapsulation in object-oriented programming. Encapsulation is
 the idea that an object should control its own state and behavior, and that its internal details should be hidden
 from the outside world.

 In Python, we can implement encapsulation using access modifiers, which control the visibility of class attributes and
 methods. There are two types of access modifiers in Python:
  1. Public: attributes and methods that are accessible from anywhere, using the dot notation (e.g. object.attribute or
 object.method()). In Python, all attributes and methods are public by default.
  2. Private: attributes and methods that are only accessible within the class that defines them, using the double
 underscore notation (e.g. self.__attribute or self.__method()). Private attributes and methods are not directly
 accessible from outside the class. """


# Example of encapsulation
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# account = BankAccount("1234", 1000)
# print(account.__balance)  # This will raise an AttributeError

account = BankAccount("1234", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # This will print 1300
