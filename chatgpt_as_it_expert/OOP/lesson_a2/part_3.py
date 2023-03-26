class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the engine...")

    def stop(self):
        print("Stopping the engine...")

    def drive(self):
        print("Driving the vehicle...")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, num_passengers):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start(self):
        print("Starting the car engine...")

    def park(self):
        print("Parking the car...")

    def lock(self):
        print("Locking the car...")

    def honk_horn(self):
        print("Honking the car horn...")


my_car = Car("Toyota", "Corolla", 2020, 4, 5)
my_car.start()  # calls the start method specific to Car
my_car.honk_horn() # calls the honk_horn method specific to Car
