class Ogrenci:
    ogrenciNotlari = []

    def __init__(self, adSoyad, not1, not2):
        self.adSoyad = adSoyad
        self.not1 = not1
        self.not2 = not2
        Ogrenci.GenelOrtalama(self)

    @classmethod
    def GenelOrtalama(cls,ogrenciNesnesi):
        Ogrenci.ogrenciNotlari.append(ogrenciNesnesi.NotHesapla())


    def NotHesapla(self):
        return (self.not1 + self.not2) / 2

o1 = Ogrenci("Ali Veli",34,55)
o2 = Ogrenci("Özgür Çetin",95,70)
for item in Ogrenci.ogrenciNotlari:
    print(item)