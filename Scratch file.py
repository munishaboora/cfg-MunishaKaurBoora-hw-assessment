# #Polymorphism
# class VehicleDetails:
#
#     def __init__(self, brand, colour, model):
#         self.brand = brand
#         self.colour = colour
#         self.model = model
#
#     def print_vehicle_details(self):
#         print(f"Vehicle brand: {self.brand}")
#         print(f"Vehicle colour: {self.colour}")
#         print(f"Vehicle model: {self.model}")
#
# class Cycle(VehicleDetails):
#     def print_vehicle_details(self):
#         print(f"The cycle's brand is {self.brand} and its model name is {self.model}. The cycle is also {self.colour} in colour.")
#
# class Car(VehicleDetails):
#     def print_vehicle_details(self):
#         print(f"The car's brand is {self.brand} and its model name is {self.model}. The car is also {self.colour} in colour.")
#
#
# munishas_cycle = Cycle('Raleigh', 'blue', 'stowaway folding bike')
# munishas_cycle.print_vehicle_details()
#
# munishas_car = Car('BMW', 'purple', 'BMW X5')
# munishas_car.print_vehicle_details()


class Lion:
    def diet(self):
        print("carnivore")


class Giraffe:
    def diet(self):
        print("herbivore")


object_lion = Lion()
object_lion.diet()

object_giraffe = Giraffe()
object_giraffe.diet()



