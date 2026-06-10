# multiplication table 

number = int(input("enter the number:"))
for i in range(1,11):
    if i==5:
        continue
    print(number , 'x', i , '=', number*i)

