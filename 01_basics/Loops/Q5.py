# find the first non repeated character

string = str(input("enter the string:"))

for char in string:
    print(char)
    if string.count(char) ==1:
        print("char is :", char)
        break