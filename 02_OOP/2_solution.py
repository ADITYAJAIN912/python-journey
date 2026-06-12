# class method and self

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"The brand of the car is {self.brand} and the model of the car is {self.model} "
        

my_Car = Car("toyota", "corrola")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())