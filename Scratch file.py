class VehicleDetails:

    def __init__(self, brand, colour, model):
        self.brand = brand
        self.colour = colour
        self.model = model

class Cycle(VehicleDetails):
    def print_cycle_details(self):
        print(f"Cycle brand: {self.brand}")
        print(f"Cycle colour: {self.colour}")
        print(f"Cycle model: {self.model}")

class Car(VehicleDetails):
    def print_car_details(self):
        print(f"Car brand: {self.brand}")
        print(f"Car colour: {self.colour}")
        print(f"Car model: {self.model}")


munishas_cycle = Cycle('Raleigh', 'Blue', 'Stowaway folding bike')
munishas_cycle.print_cycle_details()

munishas_car = Car('BMW', 'Purple', 'BMW X5')
munishas_car.print_car_details()


