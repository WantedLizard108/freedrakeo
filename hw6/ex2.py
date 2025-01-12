class Vehicle:
    make = None
    model = None

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info (self):
        print(self.make, '\n', self.model ,sep = '')

class Car(Vehicle):
    fuel_type = None

    def __init__ (self, make, model, fuel_type):
        super(Car, self).__init__(make, model)
        self.fuel_type = fuel_type
        self.get_info()

    def get_info (self):
        super().get_info()
        print(self.fuel_type)

my_car = Car('BMW', 'x5', 'бензин')