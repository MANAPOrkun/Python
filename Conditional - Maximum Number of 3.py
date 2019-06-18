a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

max=a

if(max<b):
    max=b
elif(max<c):
    max=c

print("Maximum number is : ",max)