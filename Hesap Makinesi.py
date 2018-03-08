print("Hesap Makinesi")



while True:

    deger1=float(input("1.Değeri Giriniz: "))
    deger2=float(input("2.Değeri Giriniz: "))


    toplama = deger1 + deger2
    cikarma = deger1 - deger2
    carpma = deger1 * deger2
    bolme = deger1 / deger2

    girdi=input("Lütfen hangi işlemi yapacağınızı yazınız: ")

    if girdi == "toplama":
        print("Değer 1 + Değer 2 = ",toplama)
    elif girdi == "çıkarma":
        print("Değer 1 - Değer 2 = ", cikarma)
    elif girdi == "çarpma":
        print("Değer 1 * Değer 2 = ", carpma)
    elif girdi== "bölme":
        print("Değer 1 / Değer 2 = ", bolme)
    else:
        print("Lütfen tanımlanabilir işlem seçiniz.")
        break



