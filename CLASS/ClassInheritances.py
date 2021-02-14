
class Mammals :  #super class

    def walk(self):
        print("!!!!!!!!!!Can WAlk!!!!!!!!!!!!!!!")


 class  Dog (Mammals) : #sub class of Mammals
    def Bark(self):
        print("!!!!!!!!!!!!Can Bark!!!!!!!!!!!!!!")

    def walk(self):
        print("Dog can Walk")

class Cat (Mammals) :  #sub class of Mammals
    pass               #pass is needed because class boby cannot be empty

Mammal =Mammals()
Mammal.walk()

Do=Dog()
Do.walk()
Do.Bark()

cat=Cat()
cat.walk()

