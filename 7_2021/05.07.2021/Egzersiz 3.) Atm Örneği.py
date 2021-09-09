class Kart:
    def __init__(self, ad, soyad, bankaAdi, para):
        self.ad = ad
        self.soyad = soyad
        self.bankaAdi = bankaAdi
        self.para = para

    def BilgiVer(self):
        return f"Kart sahibi ad: {self.ad}\nSoyad: {self.soyad}\nBanka Adı :{self.bankaAdi}\nMiktar :{self.para}"


class Atm:
    def __init__(self, ad, para):
        self.ad = ad
        self.para = para

    def AyniMi(self, kart):
        if self.ad == kart.bankaAdi:
            return True
        else:
            return False

    def ParaCek(self, kart, miktar):
        if self.para >= miktar:
            if kart.para >= miktar:
                kart.para -= miktar
                self.para -= miktar
                if not self.AyniMi(kart):
                    kart.para -= miktar * 0.03
                    self.para += miktar * 0.03
                    print(" {} Tl işlem ücreti alındı".format(miktar * 0.03))
                print("{} TL çekildi\nATM'de {} TL kaldı".format(miktar, self.para))
            else:
                print("Karttaki bakiye yetersiz. Mevcut bakiye  = {}".format(kart.para))
        else:
            print("Atm'de bu kadar para yok, Atm'deki para miktarı = {}".format(self.para))

    def ParaYatir(self, kart, miktar):
        kart.para += miktar
        self.para += miktar
        if not self.AyniMi(kart):
            kart.para -= miktar * 0.03
            self.para += miktar * 0.03
        print("{} TL yatırıldı\nAtm'de {} TL oldu.".format(miktar, self.para))

    def BilgiVer(self):
        return f"Banka Adı = {self.ad}\n Atm'deki Para= {self.para}"


k1 = Kart("Özgür", "Çetin", "Garanti", 150)
atm1 = Atm("Garanti", 350)
atm1.ParaCek(k1, 100)
print(k1.BilgiVer())
