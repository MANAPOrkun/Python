print("""
    *********************
         ATM MAKİNESİ
    *********************

    İŞLEMLER:
    1.BAKİYE SORGULAMA
    2.BAŞKA HESABA PARA YATIRMA
    3.PARA ÇEKME
    4.HESABINIZA PARA YATIRMA
    5.ÇIKIŞ


""")

bakiye=100
while True:
    islem=(input("Lütfen işlem seçiniz: "))
    if islem == "1":
        print("Bakiyeniz:",bakiye,"TL")
    elif islem=="2":
        hesap=(input("Lütfen para yatırmak istediğiniz banka hesap numarasını giriniz: "))
        if len (hesap) !=16:
            print("Hesap numarası 16 karakter olmak zorundadır.")
        elif len(hesap)==16:
            hesaba_para=int(input("Lütfen hesaba yatıracağınız para miktarını giriniz: "))

            if hesaba_para>bakiye:
                print("Hesabınızda yeterli miktarda bakiye bulunmamaktadır.")
            elif hesaba_para<=bakiye:
                bakiye = bakiye - hesaba_para
                print("Diğer hesaba başarılıyla para aktarılmıştır.")
            else:
                print("Tanımlanabilir işlem giriniz.")
    elif islem=="3":
        para_cekme=int(input("Lütfen çekmek istediğiniz bakiyeyi giriniz: "))
        if para_cekme>bakiye:
            print("Hesabınızda yeterli miktarda bakiye bulunmamaktadır.")
        elif para_cekme<=bakiye:
            bakiye=bakiye-para_cekme
            print("Başarılı şekilde para çekiminiz gerçekleştirilmiştir.")
        else:
            print("Tanımlanabilir işlem giriniz.")
    elif islem=="4":
        para_yatırma=int(input("Yatırmak istediğiniz miktarı giriniz: "))
        bakiye=para_yatırma+bakiye
        print("Başarılıyla hesabınıza para yatırılmıştır.")

    elif islem=="5":
        print("Sistemden çıkılıyor...")
        break
    else:
        print("Geçersiz işlem.")

