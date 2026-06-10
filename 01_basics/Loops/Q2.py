# Sum of even numbers

number = int(input("give the number n:"))
sum = 0

for num in range(1 ,number+1):
    if num % 2==0:
       sum +=num

print("the sum of even number is :", sum)