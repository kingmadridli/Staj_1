class User:
    userListe = []

    def __init__(self, kulNick, kulPw):
        self.kulNick = kulNick
        self.kulPw = kulPw
        User.Ekle(self)

    @classmethod
    def Ekle(cls, us):
        cls.userListe.append(us)

    @classmethod
    def Olustur(cls, string=str()):
        liste = string.split(",")
        return cls(liste[0], liste[1])


class Sistem:
    def __init__(self, ad):
        self.ad = ad

    def Login(self, kulAd, kulSifre):
        isLogin = False
        for item in User.userListe:
            if item.kulNick == kulAd and item.kulPw == kulSifre:
                isLogin = True
        if isLogin:
            print(" {} Sisteme Hoşgeldiniz {} ".format(self.ad, kulAd))
        else:
            print("Hatalı giriş")




User.Olustur("Ali,Veli")
User.Olustur("Özgür,Çetin")
s1 = Sistem("Windows")
ad = input("Lütfe Kullanıcı adı girin.")
pw = input("Lütfen şifre giriniz :")
s1.Login(ad,pw)

for item in User.userListe:
    print(item.kulNick, item.kulPw)
