print("""
    ******************
     FAKTORİYEL BULMA
    ******************

""")
while True:
    sayi=int(input("Lütfen bir sayı giriniz:"))
    faktoriyel=1
    for i in range(2,sayi+1):
        faktoriyel*=i
    print("Faktöriyel: ",faktoriyel)
