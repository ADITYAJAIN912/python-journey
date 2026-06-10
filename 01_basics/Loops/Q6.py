# factorial using while loop 

number = int(input("enter the number:"))
fact =1

while number>0:
    fact =fact *number
    number = number -1

print("factorial is:",fact)