def LCM(x,y):

    i=2
    lcm=1

    while(x != 1 or y != 1):

        if(x % i == 0 and y % i == 0):

            x /= i
            y /= i
            lcm *= i

        elif (x % i == 0):

            x /= i
            lcm *= i

        elif(y % i == 0):

            y /= i
            lcm *= i

        else:

            i += 1


    return lcm

print("Least Common Multiple : ",LCM(15,20))