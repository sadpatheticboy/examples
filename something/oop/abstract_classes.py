from abc import ABC, abstractmethod


class Dog(ABC):
    @abstractmethod
    def work(self): pass

    def bark(self):
        print('bork')


class HuntingDog(Dog):
    # def work(self): pass
    def work(self):
        super().work()


class ShepherDog(Dog): pass

d = HuntingDog()
d.work()
