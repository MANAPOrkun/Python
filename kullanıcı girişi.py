print("""
    ****************

    KULLANICI ÜYELİĞİ

    ****************
""")
a=("manap")
b=("12345")

sys_id=(input("Lütfen Kullanıcı adı belirleyiniz: "))
sys_password=(input("Lütfen parola belirleyiniz: "))
giris_hakki=3
while True:

    if a == sys_id:
     print("Kullanıcı adı kullanılmaktadır.")
     sys_id = (input("Lütfen Tekrardan Kullanıcı adı belirleyiniz: "))
     sys_password = (input("Lütfen tekrardan parola belirleyiniz: "))


    elif a!= sys_id:
        print("Kullanıcı adınız ve parolanız kaydedilmiştir...")
        break

while True:
    print("""    *****************

    KULLANICI GİRİŞİ

    *****************""")
    id = input("Lütfen Kullanıcı Adınızı Giriniz: ")
    password = input("Lütfen Parolanızı Giriniz: ")
    if id == sys_id and password!=sys_password:
        print("Parolayı yanlış girdiniz.")
        giris_hakki-=1
    elif id !=sys_id and password==sys_password:
        print("Kullanıcı adınızı yanlış girdiniz.")
        giris_hakki-=1
    elif id!=sys_id and password!=sys_password:
        print("Kullanıcı adınızı ve parolanızı yanlış girdiniz.")
        giris_hakki-=1
    else:
        print("Başarıyla giriş yaptınız.")
        break
    if giris_hakki == 2:
        print("2 tane giriş hakkınız kalmıştır.")
    elif giris_hakki==1:
        print("1 tane giriş hakkınız kalmıştır.")
    elif giris_hakki==0:
        print("Giriş hakkınız kalmamıştır daha sonra tekrar deneyiniz.")
        break

