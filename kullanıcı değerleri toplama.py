toplam=0
while True:
    deger=(input("Lütfen değer giriniz: "))
    if deger=="q":
        print("Programdan çıkılıyor...")
        break
    deger=int(deger)
    toplam+=deger
print("Toplam: ", toplam)