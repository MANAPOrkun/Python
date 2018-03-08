print("""
    *******************************
    ARMSTRONG SAYISI BULMA PROGRAMI
    *******************************
""")
while True:
    sayi=int(input("Lütfen bir sayı giriniz: "))
    a=0
    b=sayi
    liste=[]
    if 1000>sayi>99:
        sayi=str(sayi)
        sayi = list(sayi)
        for i in sayi:
           i=int(i)
           i=i**3
           liste.append(i)
        a=liste[0]+liste[1]+liste[2]

        if a==b:
            print("Girdiğiniz {} sayısı bir armstrong sayısıdır.".format(b))
        elif a!=b:
            print("Girdiğiniz {} sayısı bir armstrong sayısı değildir.".format(b))

    elif 10000>sayi>999:
        sayi = str(sayi)
        sayi = list(sayi)
        for i in sayi:
            i=int(i)
            i=i**4
            liste.append(i)
        a = liste[0] + liste[1] + liste[2]+liste[3]

        if a == b:
            print("Girdiğiniz {} sayısı bir armstrong sayısıdır.".format(b))
        elif a != b:
            print("Girdiğiniz {} sayısı bir armstrong sayısı değildir.".format(b))