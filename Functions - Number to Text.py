def ToText(number):

    a = number % 10
    b = (number - a)

    one_to_twenty={0:"",1:" one",2:" two",3:" three",4:" four",5:" five",6:" six",7:" seven",8:" eight",9:" nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    tens = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

    if(number < 20):

        if(number == 0):
            return "zero"

        return one_to_twenty[number]

    elif(number >= 20 and number < 100):

        return (tens[b]+one_to_twenty[a])


print("Only 2 digit number:\n")

print(ToText(39))


