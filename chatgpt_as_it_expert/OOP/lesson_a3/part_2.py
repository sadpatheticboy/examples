""" In the previous lesson, we explored the concept of encapsulation and how to use private attributes to hide
 the internal details of a class from the outside world. In this lesson, we'll explore how to use getters and setters
 to provide controlled access to private attributes. """


# Getters and setters are methods that allow us to access and modify private attributes in a controlled way.
# Here's an example class that uses getters and setters:
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

    def set_balance(self, new_balance):
        if new_balance < 0:
            print("Invalid balance")
        else:
            self.__balance = new_balance


account = BankAccount("1234", 1000)
print(account.get_balance())  # This will print 1000

account.set_balance(-500)  # This will print "Invalid balance"

account.set_balance(1500)
print(account.get_balance())  # This will print 1500
