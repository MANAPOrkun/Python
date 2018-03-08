sayi=int(input("Sayi giriniz: "))
liste=[*range(2,sayi)]
for i in liste:
    if(sayi%i==0):
        print(sayi,"Asal sayı değildir.")
        break
    elif sayi%i!=0:
        print("Asal sayıdır.")
        break