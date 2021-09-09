class BankAccount:
    def __init__(self,name,money,address):
        self.name = name
        self.__money = money        # Money değişkeni private oldu
        self.address = address


    def GetMoney(self):          # Pivate değişkene bu şekilde ulaştık
        return self.__money

    def SetMoney(self,amount):  # Pivate değişkeni bu şekilde ayarladık
        self.__money = amount

    def __Increase(self,a):        #Bu şekilde de methot private olmuş oldu     
        self.__money = self.__money + a


person_1_account = BankAccount("özgür",5000,"istanbul")

#  print(person_1_account.__money)


person_1_account.SetMoney(4000)
print(person_1_account.GetMoney())
person_1_account.Increase(500)
print(person_1_account.GetMoney())

