sayi=int(input("Lütfen değer giriniz: "))
i=1
toplam=0
while (i<sayi):
    if sayi%i==0:
        toplam+=i
    i += 1
if toplam==sayi:
    print("mükemmel sayı")
else:
    print("mükemmel sayı değil.")