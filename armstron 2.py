sayi=input("Değer giriniz:")
basamak_sayisi=len(sayi)
sayi=int(sayi)
basamak=0
toplam=0
gecici=sayi
while(0<gecici):
    basamak=gecici%10
    toplam+=basamak**basamak_sayisi
    gecici//=10
if toplam==sayi:
    print("Armstrong sayısı",sayi)
else:
    print("Armstrong değil")