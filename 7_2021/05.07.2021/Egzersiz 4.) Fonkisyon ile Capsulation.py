import datetime
class Ogrenci:
    def __init__(self,ad,soyad,tc,sinif,dTarihi):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.sinif = sinif
        self.SetDTarihi(dTarihi)

    def BilgiVer(self):
        return f"{self.ad}\n{self.soyad}\n{self.tc}\n{self.sinif}\n{self.__dTarihi}"

    def SetDTarihi(self,arg):
        if arg <= datetime.datetime.now().year:
            self.__dTarihi = arg
        else:
            self.__dTarihi = datetime.datetime.now().year
    def GetDTarihi(self):
        return self.__dTarihi

    def YasHesapla(self):
        return datetime.datetime.now().year - self.GetDTarihi()

ogr1 = Ogrenci("Ali","Kemal",12345,10,1998)
print(ogr1.BilgiVer())
#print(ogr1.YasHesapla())