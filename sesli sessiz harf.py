while True:
    harf=input("Lütfen harf giriniz: ")
    harf=list(harf)
    sesli="aeıioöuü"
    sessiz="bcçdfgğhjklmnprsştvyz"
    for i in harf:
        if i in sesli:
            print("Sessli harftir: ",i)
        elif i in sessiz:
            print("Sessiz harftir: ",i)
        else:

            print("{} Dışında lütfen tanımlanabilir değer giriniz.".format(i))
            continue