# encapsulation

class Car:
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"The brand of the car is {self.__brand} and the model of the car is {self.model} "
    
class Electric_vehicle(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


        

my_Car = Car("toyota", "corrola")
my_tesla = Electric_vehicle("tesla","S","185kwh")

print(my_tesla.get_brand())

# just revise , how to encapsulate any attribute in the class usin "__" and for that using getter to acces it and how t oacces after creating the object by calling the getter function.
# and also study about the setter