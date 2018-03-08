"""
Ödev 1


a=int(input("Bir 1değer giriniz:"))
b=int(input("Bir 1değer giriniz:"))
c=int(input("Bir 1değer giriniz:"))

print("Girdiğiniz sayıların çarpımları:{}".format(a*b*c))


"""
""""
Ödev 2

print("Beden Kitle İndeksi Ölçme Programı")
boy=float(input("Lütfen Boyunuzu Sayı Olarak Giriniz:"))
kilo=float(input("Lütfen Kilonuzu Sayı Olarak Giriniz:"))

print("Beden Kitle İndeksiniz Şu Şekildedir:{}".format(kilo/(boy**2)))

"""
"""
print("Aracınızın Ödemesi Gereken Tutar Ölçme Aracı")
a=float(input("Aracınızın 1 KM 'de gittikten sonra ödenen tutarı giriniz:"))
b=float(input("Aracınızın Toplam gittiği mesafe"))

print("Aracınızın toplan ödemesi gereken tutar:",a*b)

"""
"""
ad=str(input("Lütfen Adınızı Giriniz:"))
soyad=str(input("Lütfen Soyadınızı Giriniz:"))
numara=int(input("Lütfen Telefon Numaranızı Giriniz"))
bilgiler=[ad,soyad,numara]
print("Adınız: {}\nSoyadınız: {}\nTelefon Numaranız: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
"""
"""
print("Değer değiştirme programı")
a=int(input("Lütfen bir değer giriniz:"))
b=int(input("Lütfen başka bir değer giriniz:"))
a,b=b,a
print("İlk girdiğiniz değer:",a)
print("İkinci girdiğiniz değer",b)
"""
"""
print("Dik Üçgenin hipotenüs uzunluğu hesaplama programı")

a=int(input("Dik Üçgenin Bir Kenarını Giriniz:"))
b=int(input("Dik Üçgenin Diğer Bir Kenarını Giriniz:"))

hipotenüs = (a**2+b**2)**0.5

print(hipotenüs)
"""
"""
a=int(input("a değerini giriniz:"))
b=int(input("b değerini giriniz"))
if a==2:
    print("a 2 ye eşittir")
if b==2:
    print("b 2 ye eşittir")
if a!=2:
    print("a 2 ye eşit değildir")
if b!=2:
    print("b 2 ye eşit değildir")
"""
"""
for i in range(0,20):
    print("Sanaツ"*i)
"""
