def PTriangle(number):

    for i in range(1,number):
        for j in range(i,number):
            k = (i**2+j**2)**0.5
            if(k % 1 == 0):
                print (i,j,k)

PTriangle(100)
