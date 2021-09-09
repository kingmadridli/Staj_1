def NotHesapla(satir):
    liste = satir.split(":")
    print(liste[0])
    print(liste[1])


def NotlariOku():
    with open("Sınav_Notları.txt","r",encoding="UTF-8") as file:
        for satir in file:
            print(NotHesapla(satir),end="")



def NotGir():
    ad = input("Öğrencinin Adı : ")
    soyad = input("Öğrencinin Soyadı : ")
    not1 = input("Öğrencinin 1.Notu : ")
    not2 = input("Öğrencinin 2.Notu : ")
    not3 = input("Öğrencinin 3.Notu : ")
    with open("Sınav_Notları.txt", "a+", encoding="UTF-8") as file:
        file.write(ad + " " + soyad + ": " + not1 + ", " + not2 + ", " + not3 + "\n")
        print(file.read())


def NotKayit():
    pass


while True:
    menu = """
        1.) Notları Oku
        2.) Not Gir
        3.) Notları Kayıt Et
        4.) Çıkış    
        """
    islem = int(input(menu))

    if islem == 1:
        NotlariOku()
    elif islem == 2:
        NotGir()
    elif islem == 3:
        NotKayit()
    elif islem == 4:
        break
