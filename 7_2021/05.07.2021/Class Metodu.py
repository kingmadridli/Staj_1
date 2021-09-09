# class Insan:
#     insanlar = []
#
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         Insan.Ekle(self)
#     @classmethod
#     def Ekle(cls,insanNesnesi):
#         Insan.insanlar.append(insanNesnesi)
#
#     def __str__(self):
#         return "{} {}".format(self.ad,self.soyad)
#
#     @classmethod
#     def Parcala(cls,isim):
#         liste = isim.split(",")
#         return cls(liste[0],liste[1])
#
#
#
# Insan.Parcala("Ali,Veli")
# Insan.Parcala("Özgür,Çetin")
# Insan.Parcala("İnci,Yirmibes")
#
# for item in Insan.insanlar:
#     print(item)




