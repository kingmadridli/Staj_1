# class Sistem:
#     def __init__(self):
#         self.__ad = None
    
#     @property
#     def Ad(self):
#         return self.__ad

#     @Ad.setter
#     def Ad(self,value):
#         self.__ad = value

#     # @Ad.getter         # Gereksiz
#     # def Ad(self):
#     #     return self.__ad



# o1 = Sistem()

# print(o1.Ad)
# result = o1.Ad("Linux")
# print(result)



class Ogrenci:
    def __init__(self,ad,soyad):
        self.__ad = ad
        self.__soyad = soyad

    @property
    def Ad(self):
        return self.__ad
    
    @Ad.setter
    def Ad(self,value):
        self.__ad = value

    @property
    def Soyad(self):
        return self.__soyad

    @Soyad.setter
    def Soyad(self,value):
        self.__soyad = value

    @property
    def AdSoyad(self):
        return self.__ad + " " + self.__soyad


o1 = Ogrenci("Özgür","Çetin")
print(o1.Ad)
print(o1.Soyad)
print(o1.AdSoyad)

