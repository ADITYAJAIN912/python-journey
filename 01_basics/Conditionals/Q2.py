# Movie ticket pricing 
# Movie tickets are priced based on the age: $12 for the adult (age>18 and over), 8$ for children.Everyone gets a 2$ discount on wednesday 

age = int(input("please enetr the age:"))
day = str(input("please enter the day: "))

if age < 8 and day == "wednesday":
    print("discounted price: 6$")

elif age < 8 and day!= "wednesday":
    print("Ticket price:8$ ")

elif age >=18 and day == "wednesday":
    print("tickets price: 10$")

else:
    print("tickets price : 10$")