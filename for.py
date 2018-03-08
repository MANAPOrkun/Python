sayı=tuple(input("Lütfen sayı değeri giriniz: "))

for a in sayı:
    a = int(a)
    if a % 2 == 0:
        print("Girdiğiniz şu değer çifttir:",a)
    else:
        print("Girdiğiniz şu değer tektir:",a)