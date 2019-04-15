length=float(input("Enter length as meter: "))
weight=int(input("Enter weight as kilogram: "))
BMI=weight/(length**2)
if(BMI<18.5):
    print("Thin")
elif(18.5<BMI<25):
    print("Ideal")
elif(25<BMI<30):
    print("Overweight")
else:
    print("Obese")

print("Your body mass index is : ",BMI)