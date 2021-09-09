class Ogrenci:
    def __init__(self,ad_soyad,not_1,not_2):
        self.ad_soyad = ad_soyad
        self.__not_1 = not_1
        self.__not_2 = not_2
        self.__gecerli_not = True


    @property
    def Not1(self):
        return self.__not_1

    @Not1.setter
    def Not1(self,value):
        self.KontrolEt(value)
        self.__not_1 = value
    

    @property
    def Not2(self):
        return self.__not_2

    @Not2.setter
    def Not2(self,value):
        self.KontrolEt(value)
        self.__not_2 = value

    @property
    def Ortalama(self):
        if not self.__gecerli_not == False:
            return (self.Not1 + self.Not2) / 2
        else:
            print("0-100 arası olmalı")

    def KontrolEt(self,arg):
        if not 0 <= arg <= 100:
            self.__gecerli_not = False
        


not1 = int(input("Lütfen 1.notunuzu giriniz : "))
not2 = int(input("Lütfen 2.notunuzu giriniz : "))
o1 = Ogrenci("Özgür çetin",not1,not2)

print(o1.Ortalama)