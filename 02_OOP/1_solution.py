# Basic class and object 

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

my_Car = Car("toyota", "corrola")
print(my_Car.brand)
print(my_Car.model)

# # remeber to how make the class - clarr name:
#                                         def __init__(self, brand ,model)
# and how to create objects(instance of the class) and remember the assigning some varibale to the object and how to acces the object using .(dot) operator!