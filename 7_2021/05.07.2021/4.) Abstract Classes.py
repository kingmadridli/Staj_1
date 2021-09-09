from abc import ABC
from abc import abstractmethod
  
class Animal(ABC):              # Bu class şablon niteliği taşımaktadır.
 
    @abstractmethod             # Bunun için sadece bir tane abstractmethod yetrlidir.
    def Walk(self): 
        pass

                                # Child classa ait bir nesne oluşturmak için, oluşturtuğumuz child classta abstract classtaki bütün methotları kullanmak zorundayız.
    def Run(self):              # Bu şekilde ise Run Methot-dunu kullanmak zorunda değiliz.
        pass


class Bird(Animal):
    def __init__(self):
        print("Bird")

    def Walk(self):
        print("walk")
    def Run(self):
        print("run")
        


b1 = Bird()