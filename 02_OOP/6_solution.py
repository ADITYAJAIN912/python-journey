# class variable:- 

class Car:
    total_car = 0
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
        Car.total_car +=1

    def full_name(self):
        return f"The brand of the car is {self.brand} and the model of the car is {self.model} "
    
class Electric_vehicle(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

        

my_Car = Car("toyota", "corrola")
my_tesla = Electric_vehicle("tesla","S","185kwh")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())

print(my_tesla.full_name())
print(my_tesla.battery_size)
print(Car.total_car)