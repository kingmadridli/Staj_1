class Ogrenci:
    def __init__(self,ad,soyad,tc,sinif,okul):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.SetSinif(sinif) 
        self.SetOkul(okul)

    def BilgiVer(self):
        if self.__sinif == -1:
            return "ÜZgünüm Sınıf seviyesi 9-12 dışında kayıt kabul edilemez."
        elif self.__okul == -1:
            return "Üzgünüm Kadıköy dışı kayıt kabul edilemez"
        return f"Adı: {self.ad}\nSoyadı: {self.soyad}\nTc No: {self.tc}\nSınıf: {self.__sinif}\nOkul: {self.__okul}"

    def SetSinif(self,arg):
        if 8 < arg < 13:
            self.__sinif = arg
        else:
            self.__sinif = -1

    def SetOkul(self,arg):
        if arg == "Kadıköy Lisesi":
            self.__okul = arg
        else:
            self.__okul = -1


    def GetSinif(self):
        return self.__sinif    

ogrenci_1 = Ogrenci("Ali","Kemal",12345,12,"Kadıköy Lisesi")


#  ogrenci_1.SetSinif(11) ==> Override işlemi
print(ogrenci_1.BilgiVer())



