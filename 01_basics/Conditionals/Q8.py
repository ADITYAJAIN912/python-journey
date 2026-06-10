# LEAP YEAR 

year = int(input("enter the year :"))

if year %4 == 0:
    print( year,"year is leap year")

elif year % 400 == 0 and year % 100 ==0:
    print(year,":year is  a leap year")

else :
    print(year,":year is not a leap year")
     
    