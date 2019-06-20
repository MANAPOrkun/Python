def Even(number):
    if(number % 2 == 0):
        return number
    else:
        raise ValueError

print(Even(2))

list = [34,2,1,3,33,100,61,1800]

for i in list:
    try:
        print(Even(i))
    except ValueError:
        pass
