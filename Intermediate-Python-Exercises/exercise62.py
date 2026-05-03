from math import pi as PI
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    @property
    def area(self):
        return PI*self.radius**2
if __name__ == "__main__":
    c = Circle(5)
    print(c.area)
    c.radius = 10
    print(c.area)
