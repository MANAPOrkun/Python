numb=input("Enter a number: ")
digit=0
sum=0
for i in numb:
    digit+=1
for i in numb:
    sum+=int(i)**digit
if(sum==int(numb)):
    print("It's a armstrong number.")
elif(sum!=int(numb)):
    print("It's not a armstrong number.")