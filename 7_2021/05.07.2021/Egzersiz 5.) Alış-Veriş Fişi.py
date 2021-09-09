class Urun:
    def __init__(self, urunId, ad, birimFiyati, birimBasinaMiktar, kdv):
        self.urunId = urunId
        self.ad = ad
        self.birimFiyati = birimFiyati
        self.birimBasinaMiktar = birimBasinaMiktar
        self.kdv = kdv


class SepetUrunu:
    def __init__(self, urun, adet):
        self.urun = urun
        self.adet = adet

    def UrunFiyati(self):
        if self.urun.birimBasinaMiktar == "TL/Kg":
            return round(self.urun.birimFiyati * self.adet, 2)
        elif self.urun.birimBasinaMiktar == "GR. PKT":
            return round(self.urun.birimFiyati * self.adet / 1000, 2)


class Sepet:
    def __init__(self, musteriId, sUrunler):
        self.musterId = musteriId
        self.sUrunler = sUrunler

    def KDV(self):
        toplamKDV = 0
        for item in self.sUrunler:
            if item.urun.birimBasinaMiktar == "TL/Kg":
                toplamKDV += item.urun.birimFiyati * item.adet * item.urun.kdv
            elif item.urun.birimBasinaMiktar == "GR. PKT":
                toplamKDV += item.urun.birimFiyati * item.adet / 1000 * item.urun.kdv
        return round(toplamKDV, 2)

    def BilgiVer(self):
        for item in self.sUrunler:
            print("""
            {}      {}     {}     {}    {}    {}
            """.format(item.urun.ad,
                       str(item.adet),
                       str(item.urun.birimBasinaMiktar),
                       str(item.urun.birimFiyati),
                       str(item.urun.kdv),
                       str(item.UrunFiyati())))
        print("*"*80)

        print("""
        Toplam KDV =                          {}
        """.format(self.KDV()))

        toplam = 0
        for item in self.sUrunler:
            toplam += item.UrunFiyati()


        print("""
        Toplam =                              {}
        """.format(toplam))


# region Ürün Ekliyorum , Bu kısım aslında DataBase'den gelecek.
u1 = Urun(1, "Çay", 5.95, "TL/Kg", 0.08)
u2 = Urun(2, "Kahve", 8.99, "TL/Kg", 0.18)
u3 = Urun(3, "Mantar", 4.85, "GR. PKT", 0.18)
# endregion

sepetUrunleri = [SepetUrunu(u1, 1), SepetUrunu(u2, 2), SepetUrunu(u3, 400)]
s1 = Sepet("Özgür", sepetUrunleri)
s1.BilgiVer()
