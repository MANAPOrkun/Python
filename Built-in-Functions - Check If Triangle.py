edges = [(3,4,5),(6,8,10),(3,10,7)]

def CheckTriangle(x):

    if(abs(x[0]-x[1]) < x[2] < x[0]+x[1] or abs(x[2]-x[1]) < x[0] < x[2]+x[1] or abs(x[0]-x[2]) < x[1] < x[0]+x[2]):

        return True

    else:

        return False


triangles = list(filter(CheckTriangle,edges))

print(triangles)