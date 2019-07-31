names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

people = list(zip(names,surnames))

people.sort()

for person in people:

    print(person[0],person[1])
