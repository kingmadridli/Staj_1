class Kart:
    def __init__(self, ad, soyad, bankaAdi, para):
        self.ad = ad
        self.soyad = soyad
        self.bankaAdi = bankaAdi
        self.para = para

    def BilgiVer(self):
        return f"ad = {self.ad}, soyad = {self.soyad},banka adı = {self.bankaAdi}, Bakiye = {self.para}"


class Atm:
    def __init__(self, ad, para):
        self.ad = ad
        self.para = para

    def ParaCek(self, kart, miktar):
        if self.para >= miktar:
            if kart.para >= miktar:
                if Atm.AyniMi(kart) == True:
                    kart.para -= miktar
                    self.para -= miktar
                    return f"Kartta kalan para miktaru = {kart.para}\nAtm'de kalan para miktarı = {self.para}"
                elif Atm.AyniMi(kart) == False:
                    kart.para -= miktar
                    kart.para -= miktar * 0.03
                    self.para -= miktar
                    self.para -= miktar * 0.03
            else:
                print("Kartta yeterli bakiye yok.")
        else:
            print("Atm'de para yok")

    def ParaYatir(self, kart, miktar):
        if Atm.AyniMi(kart) == True:
            kart.para += miktar
            self.para += miktar
            return f"Atm'deki para miktarı = {self.para}\nKarttaki para miktarı = {kart.para}"
        elif Atm.AyniMi() == False:
            kart.para += miktar * (1 - 0.03)
            self.para += miktar * (1 + 0.03)

    def BilgiVer(self):
        return f"Atm adı = {self.ad}\nAtm'deki mevcut para = {self.para},"

    def AyniMi(self, kart):
        return self.ad == kart.bankaAdi


k1 = Kart("Özgür", "Çetin", "Garanti", 1000)
atm1 = Atm("Garanti", 1500)
print(k1.BilgiVer())
print(atm1.ParaYatir(k1, 500))
