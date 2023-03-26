class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print('Engine started.')

    def stop_engine(self):
        print('Engine stopped.')

    def drive(self):
        print('Driving')


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk_horn(self):
        print('Honk honk!')


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_doors = num_wheels

    def rev_engine(self):
        print('Vroom vroom!')


bibip = Car('BMV', 'X8', 2018, 4)
bibip.honk_horn()
