from abc import ABC, abstractmethod
from math import pi as PI

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by subclasses"""
        pass
class Circle(Shape):
    def __init__(self, radius: int = 1):
        self.radius = radius
    def area(self):
        return PI*self.radius**2
    def __str__(self):
        return f"Circle Area: {self.area()}"
class Square(Shape):
    def __init__(self, length: int=1):
        self.length = length
    def area(self):
        return self.length**2
    def __str__(self):
        return f"Square Area: {self.area()}"
class RandomShape(Shape):
    def __init_(self):
        self.v = 0
    
if __name__ == "__main__":
    shapes = [Circle(5), Square(4)]
    for shape in shapes:
        print(shape)
    RandomShape()
