# class Animal:
#     def __init__(self):
#         print("Animal is Created")

#     def toString(self):
#         print("Animal")

#     def Walk(self):
#         print("Animal is walking")


# class Monkey(Animal):

#     def __init__(self):
#         super().__init__()      # Use init of Parent(Animal) class
#         print("Monkey is Created")

#     def toString(self):
#         print("Monkey")

#     def Climb(self):
#         print("Monkeys can climb")

# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Bird is Created")

#     def Fly(self):
#         print("Birds can fly")



# m1 = Monkey()
# m1.toString()
# m1.Walk()
# m1.Climb()

# b1 = Bird()
# b1.Walk()
# b1.Fly()


class Website:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def LoginInfo(self):
        print(self.name + " " + self.surname)



class Website1(Website):
    def __init__(self, name, surname,ids):
        Website.__init__(self,name, surname)
        self.ids = ids

    def Login1(self):
        print(self.name + " " + self.surname + " " + self.ids)


class Website2(Website):
    def __init__(self, name, surname,email):
        Website.__init__(self,name, surname)
        self.email = email

    def Login2(self):
        print(self.name + " " + self.surname + " " + self.email)


user_1_account_1 = Website("name","surname")
user_1_account_1.LoginInfo()

user_1_account_2 = Website1("name","surname","123")
user_1_account_2.LoginInfo()
user_1_account_2.Login1()

user_1_account_3 = Website2("name","surname","ns@gmail.com")
user_1_account_3.LoginInfo()
user_1_account_3.Login2()
