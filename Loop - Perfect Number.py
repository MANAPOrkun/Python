numb=int(input("Enter a number: "))
sum=0
for i in range(1,numb):
    if(numb%i==0):
        sum+=i

if(sum==numb):
    print("Perfect number.")
elif(sum!=numb):
    print("It's not a perfect number.")