""" Multiple levels of inheritance occur when a subclass inherits from a superclass that is itself a subclass of another
 superclass. This means that the subclass inherits from all the methods and attributes of its direct superclass as well
 as its indirect superclass. """


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the engine...")

    def stop(self):
        print("Stopping the engine...")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, num_passengers):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def park(self):
        print("Parking the car...")

    def lock(self):
        print("Locking the car...")


class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, num_passengers, battery_size):
        super().__init__(make, model, year, num_doors, num_passengers)
        self.battery_size = battery_size

    def charge(self):
        print("Charging the battery...")


my_electric_car = ElectricCar("Tesla", "Model S", 2021, 4, 5, 75)
my_electric_car.start()  # calls the start method from Vehicle
my_electric_car.charge()  # calls the charge method specific to ElectricCar
