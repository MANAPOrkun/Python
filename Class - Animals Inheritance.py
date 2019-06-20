class Animal():

    def __init__(self,name="Unknown",type = "Unknown",species = "Unknown",number = 00,sex = "Unknown"):

        self.name = name
        self.type = type
        self.species = species
        self.number = number
        self.sex = sex

    def AddInfo(self):

        self.name = input("\nEnter name: ")
        self.species = input("Enter {} species name: ".format(self.type))
        self.sex = input("Enter sex: ")

    def Show(self):

        print("Name: ",self.name,"\nType: ",self.type,"\nSpecies: ",self.species,"\nSex:",self.sex,"\nNumber: ",self.number,"\n")

class Dog(Animal):

    dog_count = 0

    def __init__(self):

        self.type = "Dog"
        Dog.dog_count += 1
        self.number = Dog.dog_count

    def Show(self):
        super().Show()

    def Number_Dogs(self):
        print("Number of dog(s): ",Dog.dog_count)

class Cat(Animal):

    cat_count = 0

    def __init__(self):

        self.type = "Cat"
        Cat.cat_count += 1
        self.number = Cat.cat_count

    def Show(self):
        super().Show()

    def Number_Cats(self):
        print("Number of cat(s): ",Cat.cat_count)

print("ADD DOG")
D1 = Dog()
D1.AddInfo()
D2 = Dog()
D2.AddInfo()

print("\nADD CAT")
C1 = Cat()
C1.AddInfo()

print("\nANIMALS\n\n")

D1.Show()
D2.Show()
C1.Show()

print("\nINFORMATION\n")

D1.Number_Dogs()
C1.Number_Cats()