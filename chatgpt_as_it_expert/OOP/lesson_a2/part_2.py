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
        super().__init__(make, model, year)  # Передаём переменные в метод суперкласса Vehicle
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def park(self):
        print("Parking the car...")

    def lock(self):
        print("Locking the car...")


my_car = Car("Toyota", "Corolla", 2020, 4, 5)
my_car.start()  # calls the start method inherited from Vehicle
my_car.drive()  # calls the drive method inherited from Vehicle
my_car.park()  # calls the park method specific to Car
my_car.lock()  # calls the lock method specific to Car
