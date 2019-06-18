def PerfectNumber(number):

    sum = 0
    temp_numb = number-1

    while(temp_numb>0):

        if(number % temp_numb == 0):

            sum += temp_numb

        temp_numb -= 1

    return sum

number=int(input("Enter an integer: "))

print(PerfectNumber(number))

if(PerfectNumber(number) == number):

    print("Perfect Number!")

else:

    print("Not Perfect Number.")