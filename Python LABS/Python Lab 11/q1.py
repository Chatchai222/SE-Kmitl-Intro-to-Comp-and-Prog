import math

class Point(object):
    def __init__(self, x=0.00, y=0.00):
        self.x = x
        self.y = y

    def printInfo(self):
        print(f"Position:{self.x},{self.y}")


class Circle(Point):
    def __init__(self, x=0.00, y=0.00, radius=0.00):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def printInfo(self):
        print(f"Position:{self.x},{self.y};Radius:{self.radius};Area:{self.area()}")


class Cylinder(Circle):
    def __init__(self, x=0.00, y=0.00, radius=0.00, height=0.00):
        super().__init__(x, y, radius)
        self.height = height

    def area(self):
        return (super().area() * 2) + (self.height * self.radius * math.pi * 2)

    def volume(self):
        return super().area() * self.height

    def printInfo(self):
        print(f"Position:{self.x},{self.y};Radius:{self.radius};Area:{self.area()};Height:{self.height};Volume:{self.volume()}")


me = Cylinder(5,5,5,10)
me.printInfo()

