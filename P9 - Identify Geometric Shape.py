choice=input("Choose triangle or quadrangle: ")
if(choice=="Triangle" or choice=="triangle"):
    a = int(input("Enter length of first edge: "))
    b = int(input("Enter length of second edge: "))
    c = int(input("Enter length of third edge: "))
    if(abs(a-b)<c<abs(a+b) or abs(a-c)<b<abs(a+c) or abs(c-b)<a<abs(c+b)):
        if(a==b==c):
            print("It's a equilateral triangle!")
        elif((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
            print("It's a isosceles triangle!")
        else:
            print("I do not know it's shape sorry. Maybe it's just a triangle.")
    else:
        print("It's impossible to have such a triangle.")

elif(choice=="Quadrangle" or choice=="quadrangle"):
    a = int(input("Enter length of first edge: "))
    b = int(input("Enter length of second edge: "))
    c = int(input("Enter length of third edge: "))
    d = int(input("Enter length of fourth edge: "))

    if(a==b==c==d):
        print("It's a square!")
    elif((a==b and c==d and a!=c) or (a==c and b==d and a!=b) or (a==d and b==c and a!=b)):
        print("It's a rectangle!")
    else:
        print("I do not know it's shape sorry. Maybe it's just a quadrangle.")

else:
    print("Wrong choice.")