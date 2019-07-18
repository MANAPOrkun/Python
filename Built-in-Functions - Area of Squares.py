edges =  [(3,4),(10,3),(5,6),(1,9)]

def SquareArea(x):

    return x[0]*x[1]

areas = list(map(SquareArea,edges))

count = 1

for square in edges:

    print("Area of Square ",square,":\t",areas[count-1])

    count += 1