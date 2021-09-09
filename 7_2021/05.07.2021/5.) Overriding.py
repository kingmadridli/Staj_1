# GEÇERSİZ KILMA


class Animal:
    def toSring(self):
        print("animal")

class Monkey(Animal):
    def toSring(self):
        print("Monkey")

a1 = Animal()
a1.toSring()

m1 = Monkey()
m1.toSring()         # Monkey calls overriding methot