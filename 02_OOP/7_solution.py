# Static method - useful when it does not need any object , example all the cars have 4 wheels , so we dont have to make the object for it just write it on the Class like Car.wheels, dont need any self.

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"The brand of the car is {self.brand} and the model of the car is {self.model} "
    
    @staticmethod
    def general_description():
        return "cars have 4 wheels "
    
class Electric_vehicle(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

        

my_Car = Car("toyota", "corrola")
my_tesla = Electric_vehicle("tesla","S","185kwh")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_name())

# print(my_tesla.full_name())
# print(my_tesla.battery_size)

print(Car.general_description()) # calling the static method , also keep note of normal method vs self method