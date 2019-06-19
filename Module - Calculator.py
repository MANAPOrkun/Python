import math
def Square(number):
    return math.sqrt(number)
def Cube(number):
    return math.pow(number,3)
def Power(number,pow):
    return math.pow(number,pow)
def Sin(angle):
    return math.sin(math.radians(angle))
def Cos(angle):
    return math.cos(math.radians(angle))
def Tan(angle):
    return math.tan(math.radians(angle))
def Root(number,root):
    return math.pow(number,1/root)
def Log(number,base):
    return math.log(number,base)
def Factorial(number):
    return math.factorial(number)
def Sum(number1,number2):
    return number1+number2
def Substraction(number1,number2):
    return number1-number2
def Multiplication(number1,number2):
    return number1*number2
def Division(number1,number2):
    return number1/number2

print("\n\t\tCalculator 1.0\n\n")
print("Operations:\n")
print("1.Summation\t\t\t2.Substraction\n3.Multiplication\t4.Division\n5.Square\t\t\t6.Cube\n7.Power\t\t\t\t8.Sin\n9.Cos\t\t\t\t10.Tan\n11.Root\t\t\t\t12.Log\n13.Factorial")
decision=int(input("\nSelect an operation: "))

if(decision==1):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Sum : ",Sum(a,b))
elif(decision==2):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Substraction : ", Substraction(a, b))
elif(decision==3):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication : ", Multiplication(a, b))
elif(decision==4):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division : ", Division(a, b))
elif(decision==5):
    a = int(input("Enter a number: "))
    print("Square : ",Square(a))
elif(decision==6):
    a = int(input("Enter a number: "))
    print("Cube : ", Cube(a))
elif(decision==7):
    a = int(input("Enter a number: "))
    b = int(input("Enter a power: "))
    print("Power : ", Power(a,b))
elif(decision==8):
    a = int(input("Enter an angle: "))
    print("Sin : ", Sin(a))
elif(decision==9):
    a = int(input("Enter an angle: "))
    print("Cos : ", Cos(a))
elif(decision==10):
    a = int(input("Enter an angle: "))
    print("Tan : ", Tan(a))
elif(decision==11):
    a = int(input("Enter a number: "))
    b = int(input("Enter a power of root: "))
    print("Root : ", Root(a, b))
elif(decision==12):
    a = int(input("Enter a number: "))
    b = int(input("Enter a base: "))
    print("Log : ", Log(a, b))
elif(decision==13):
    a = int(input("Enter a number: "))
    print("Factorial : ", Factorial(a))
else:
    print("Error")