class Ogrenci:
    def __init__(self,ad,soyad,vize,final):
        self.ad = ad
        self.soyad = soyad
        self.vize = vize
        self.final = final

    def NotHesapla(self,vize,final):
        return (0.4*vize + final*0.6)

adi = input("Öğrenicinin Adı : ")
soyAdi = input("Öğrencinin Soyadı : ")
not1 = int(input("Öğrencinin vize notu : "))
not2 = int(input("Öğrencinin Final Notu :"))

o1 = Ogrenci(adi,soyAdi,not1,not2)
print(f"{adi}-{soyAdi}; Ortalama Not = ",o1.NotHesapla(not1,not2))
