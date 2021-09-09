class Calisan:
    def __init__(self, ad, soyad, tc, maas):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.maas = maas

    def ZamYap(self, zamMiktari):
        if int(zamMiktari) >= int(self.maas) / 2:
            islem = input("Emin misiniz = (e)/(h)")
            if islem.lower() == "e":
                self.Uygula(zamMiktari)
            else:
                print("Peki")
        else:
            self.Uygula(zamMiktari)

    def Uygula(self, miktar):
        self.maas += zam
        print("Zam yapıldı yeni maaşınız T: {}".format(self.maas))

    def BilgiVer(self):
        return f"Adı = {self.ad}\tSoyadı = {self.soyad}\tTC No : {self.tc}\tMaaşı = {self.maas}"


class Sirket:
    def __init__(self, ad, kurulusTarihi):
        self.ad = ad
        self.kurulusTarihi = kurulusTarihi
        self.calisanlar = []

    def AlimYap(self, c):
        self.calisanlar.append(c)
        print(f"{c.ad} {c.soyad} isimli çalışan işe alındı.")

    def IstenCikar(self, c):
        self.calisanlar.remove(c)
        print(f"{c.ad} {c.soyad} isimli çalışan işten çıkartıldı.")


c1 = Calisan("Özgür", "Çetin", "417", 7000)
c2 = Calisan("Barış", "Çetin", "418", 8000)
c3 = Calisan("Ender", "Çetin", "419", 9000)

# s1 = Sirket("Şirket Deneme", 2019)
# s1.AlimYap(c1)
# s1.AlimYap(c2)
# s1.AlimYap(c3)
# # s1.AlimYap(Calisan(input("ad : "), input("soyad : "), input("tc :"), int(input("maaş : :"))))
# for item in s1.calisanlar:
#     if item.ad == "Barış":
#         s1.IstenCikar(item)
# print("-" * 30)
# for item in s1.calisanlar:
#     print(item.BilgiVer())
#     #print(item.ad,item.soyad,item.maas,item.tc)

# region getattr,setattr,hasattr
# # getattr => Bir objenin attributelerine erişmek için kullanılır.
#
# print(getattr(c1, "ad"))
#
# # setattr => Bir objenin attributeünü set eder.
#
# print(setattr(c1, "ad", "Ali"))
# print(getattr(c1, "ad"))
#
# #hasattr  => Bu attribute var mı yok mu , True-False döner
#
# print(hasattr(c1,"name"))
# print(hasattr(c2,"ad"))
# endregion
print(c1.__doc__)     # obje hakkında documentation var mı, onu geriye döndürür
print(c1.__dict__)    # obje hakkındaki bilgileri dict veri tipinde geri döndürür.
print(c1.__module__)  # classın tanımlı olduğu modülü geri döndürür
print(c1.__name__)    # attribute arasında name var mı ? Olsaydı geri döndürürdü.

