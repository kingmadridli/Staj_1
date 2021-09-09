# region Class Tanımı
# class A1:
#     pass
#
# class A2():
#     pass
#
# class A3(object):
#     pass
#
# # Bu nesne tanımlamaları aynıdır.
# #A1-A3 arasında fark yoktur object yazmak ile yazmamak bir şey değiştirmez
# endregion

#
# region Insan() sınıfı
# class Insan:    # class
#     ad = ""     # attribute 1
#     soyad = ""  # attribute 2
#
# i1 = Insan()    #Nesne ( Object )   i1 = Insan sınıfına ait bir nesnedir.
# i1.ad = "Ali"
# i1.soyad = "Usta"
# i2 = Insan()
# i2.ad = "Kemal"
# i3= Insan()
# print(i1.ad,i1.soyad)
# print(i2.ad,i2.soyad)
# print(i3.ad,i3.soyad)
# endregion

class Ogrenci:
    adSoyad = ""
    not1 = 0
    not2 = 0

o1 = Ogrenci()
o1.adSoyad = input("Lütfen ad soyad giriniz : ")
o1.not1 =int(input("Öğrencinin birinci notu : "))
o1.not2 = int(input("Öğrenicinin 2. notu : "))
ortalama = (o1.not1 + o1.not2 ) / 2
print(ortalama)
