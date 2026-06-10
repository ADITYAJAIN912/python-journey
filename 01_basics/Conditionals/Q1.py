# 1. Age group categorization:-
# classify person's age group :child(age<13) , teenager(age 13-19) and adult(20-59) and senior citizen(60+)

age = int(input("please enter the age:"))

if age < 13:
    print("child")

elif age < 20:
    print("teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior citizen")