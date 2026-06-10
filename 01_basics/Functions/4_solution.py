# functions that returns both circumference and area 

import math

def circle_stats(radius):
    area = math.pi *radius**2
    circumference = math.pi * 2 *radius
    return area , circumference

a ,c = circle_stats(3)
print("Area:",a,"circumference:",c)
