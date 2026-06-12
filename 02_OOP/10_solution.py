# multiple inheritnace

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"The brand of the car is {self.brand} and the model of the car is {self.model} "
    
class Battery:
    def __init__(self , Battery_type):
        self.Battery_type= Battery_type

class Engine:
    def __init__(self , Engine_name):
        self.Engine_name = Engine_name
    
class Electric_vehicle(Car,Battery,Engine):
    def __init__(self, brand, model,Battery_size,Battery_type,Engine_name):
        Car.__init__(self, brand, model)
        Battery.__init__(self, Battery_type)
        Engine.__init__(self, Engine_name)

        self.Battery_size = Battery_size

        

my_Car = Car("toyota", "corrola")
my_tesla = Electric_vehicle("tesla","S","185kwh","portable","High-grid")
my_EV = Electric_vehicle("tata","Harrier","200kwh","chargable","torquefull ")

print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())

print(my_tesla.full_name())
print(my_tesla.Battery_size)

print(my_EV.Engine_name)
