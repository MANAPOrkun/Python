def GCD(x,y):

    gcd=1
    i=2

    while(x!=1 and y!=1):

        if(x % i == 0 and y % i == 0):

            x /= i
            y /= i
            gcd*=i

        elif(x % i == 0):

            x /= i

        elif (y % i == 0):

            y /= i

        i+=1

    return gcd

print("Greatest Common Divisor : ",GCD(24,18))
