class Employee:
    def Raise(self):
        raise_rate = 0.1
        result =   100 + 100 * raise_rate
        print("Employee",result)


class ComEng(Employee):                                    # Aynı metot parent ve child sınıflarında kullanılırsa buna overriding denir
    def Raise(self):                                       # Aynı metot parent ve child sınıflarında farklı şekilde kullanılırsa buna da polymorphism denir.
        raise_rate = 0.2
        result =   100 + 100 * raise_rate
        print("ComEng",result)



class EEE(Employee):
    def Raise(self):
        raise_rate = 0.3
        result =   100 + 100 * raise_rate
        print("EEE",result)

e1 = Employee()
ce1 = ComEng()
eee1 = EEE()

e1.Raise()
ce1.Raise()
eee1.Raise()

liste = [e1,ce1,eee1]
for i in liste:
    i.Raise()



    