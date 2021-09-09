# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


#     def GetAge(self):
#         return self.age

#     def GetName(self):
#         return self.name


# a1 = Animal("Dog",6)
# print(a1.GetAge())
# print(a1.age)
# a2 = Animal("cat",5)
# a3 = Animal("bird",2)

# print(a2.GetName())




# Calculater Project

class Calc:

    def __init__(self,a,b):
        self.value_1 = a
        self.value_2 = b

    def Sum(self):
        return self.value_1 + self.value_2

    def Multiply(self):
        return self.value_1 * self.value_2

secim = input("Toplama için (1), Çarpma için (2)")

s1 = int(input("Birinici Sayıyı giriniz :")) 
s2 = int(input("İkinci Sayıyı giriniz :")) 

c1 = Calc(s1,s2)



if secim == "1":
    print(c1.Sum())
elif secim == "2":
    print(c1.Multiply())

