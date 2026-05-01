class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x:int):
        if type(x) is not int:
            raise TypeError("x must be a 'int'")
        self._x = x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y:int):
        if type(y) is not int:
            raise TypeError("y must be a 'int'")
        self._y = y
    def __str__(self):
        return f"({self._x}, {self._y})"
    def __add__(self, other):
        if type(other) is not Point:
            raise TypeError(f"{other} must be a 'Point'")
        return Point(self.x + other.x, self.y + other.y)
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p1+1
    print(p1 + p2)
