import os
from abc import ABC, abstractmethod


# ABC enforces that all classes that inherit
# from it implement all of the same methods that Shape has
class Shape(ABC):

    def area(self):
        pass

    def print(self):
        print("Area not defined for this shape")


class Square(ABC):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
    def print(self):
        print("This square has an area of", self.area())
    
class Rectangle(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def print(self):
        print("This rectangle has an area of", self.area())


def main():
    mysquare = Square(10)
    mysquare.print()

    rectangle = Rectangle(10, 20)
    rectangle.print()

main()