from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass


    def toString(self):
        pass
        

# Child Class        
class Square(Shape):
    def __init__(self,edge): 
        self.__edge = edge      #Encapsulation ==> Private Attribute
    
    def Area(self):
        result = self.__edge**2
        print("Square Area : ",result)


    def Perimeter(self):
        result = self.__edge * 4
        print("Square Perimeter",result)

    #override and polymorphism

    def toString(self):
        print("Square Edge : ",self.__edge)

        
class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius

    def Area(self):
        result =pi * self.__radius**2
        print("Circle Area : ",result)

    def Perimeter(self):
        result = 2*pi*self.__radius
        print("Circle Perimeter : ",result)

    #Overriding and Polymorphism
    def toString(self):
        print("Circle Radius : ",self.__radius)


c = Circle(5)
c.Area()
c.Perimeter()
c.toString()

s = Square(5)
s.Area()
s.Perimeter()
s.toString()