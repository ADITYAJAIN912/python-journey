# uniqueness checker

item = ["apple" , "banana","orange", "apple", "mango"]
checker =int(0)


for n in item:
    item[n]
    print(item[n])
    checker =checker + item[n]
    if item[n]==checker:
        break
    

        