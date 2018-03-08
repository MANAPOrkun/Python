print("""
    ****************************
    MÜKEMMEL SAYI BULMA PROGRAMI
    ****************************
    
     """)

while True:

    sayi = int(input("  Lütfen sayı giriniz:"))
    liste1 = []
    sayı = 0
    for i in range(1, sayi):
        liste1.append(i)
    for x in liste1:
        if sayi % x == 0:
            sayı += x
    if sayı == sayi:
        print("""
  Girdiğiniz değer ( {} ) bir mükemmel sayıdır.
        """.format(sayi))
    elif sayı != sayi:
        print("""
  Girdiğiniz değer ( {} ) bir mükemmel sayı değildir.
        """.format(sayi))
    else:
        print("Tanımlanamayan işlem.")


