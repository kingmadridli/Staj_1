# region Örnek 1
# class Insan:
#     # ad = ""
#     # soyad = ""  # class içinde bir nesne kullanıldı.
#     ınsanSayısı = 0
#     # ozellik = []  # İleride tanımlanacak özellikler bütün sınıftaki nesneler için geçerli olacaktır.
#     def __init__(self,ad,soyad,ozellik):
#         self.ozellik = ozellik
#         self.ad = ad
#         self.soyad = soyad
#         Insan.ınsanSayısı += 1
#     def Yazdir(self):
#         print("{} {} {}".format(self.ad,self.soyad,self.ozellik))
# # i1 = Insan()
# # i1.ad = "Ali"
# # i1.soyad = "Usta"
# # i1.ozellik.append("Tembel")
# # i1.ozellik.append("Uzun")
# # i2 = Insan()
# # i2.ad = "Kemal"
# # i2.ozellik.append("Çalışkan")
# #
# # i3 = Insan()
# #
# # print(i1.ad, i1.soyad, i1.ozellik)
# # print(i2.ad, i2.soyad, i2.ozellik)
# # print(i3.ad, i3.soyad, i3.ozellik)
# # print(Insan.ınsanSayısı)
#
#
# i4 = Insan("Mustafa","Kemal",["Mavi Gözlü","Sarı Saçlı"])
# i4.Yazdir()
# endregion


class Ogrenci:
    def __init__(self, adSoyad="", not1=0, not2=0):# Attribute atanmayan öğrenciler için varsayılan değer girilmeli
        self.adSoyad = adSoyad
        self.not1 = not1
        self.not2 = not2

    def NotHesapla(self):
        return (self.not1 + self.not2) / 2

o2 = Ogrenci("Ali",5,95)
isim = input("Lütfen ad-soyad giriniz : ")
vize = int(input("Lütfen vize notunuzu giriniz : "))
final = int(input("Lütfen final notunuzu giriniz : "))

o1 = Ogrenci(isim, vize, final)
print(" Not ortalamanız = ", o1.NotHesapla())
print(o2.NotHesapla())
