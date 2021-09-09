import datetime


class Araba:
    def __init__(self, marka, model, motor, yil, renk="tanımsız"):
        self.marka = marka
        self.model = model
        self.motor = motor
        self.yil = yil
        self.renk = renk
        self.yas = datetime.datetime.now().year - int(self.yil)

    def Show(self):
        return f"Markası = {self.marka}\nModeli = {self.model}\nMotoru = {self.motor}\nYılı = {self.yil}\nRengi = {self.renk}\nYaşı = {self.yas}"


marka1 = input("Arabanın markasını giriniz : ")
model1 = input("Arabanın modelini giriniz : ")
motor1 = input("Arabanın motorunu giriniz : ")
yil1 = input("Arabanın yılını giriniz : ")
renk1 = input("Arabanın rengini giriniz = ")
a1 = Araba(marka1, model1, motor1, yil1,renk1)
print(a1.Show())
