import math
from abc import ABC, abstractmethod
from turtle import *

class TwoDShape(ABC):
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0

    @abstractmethod
    def draw(self):
        print("Draw something")

class Line(TwoDShape):
    def __init__(self, x0, y0, x1, y1):
        super().__init__(x0, y0)
        self.x1 = x1
        self.y1 = y1

    def draw(self):
        penup()
        goto(self.x0, self.y0)
        pendown()
        goto(self.x1, self.y1)

class Rectangle(TwoDShape):
    def __init__(self, x0, y0, length, width):
        super().__init__(x0, y0)
        self.length = length
        self.width = width

    def draw(self):
        for _ in range(2):
            forward(self.width)
            right(90)
            forward(self.length)
            right(90)

class Circle(TwoDShape):
    def __init__(self, x0, y0, radius):
        super().__init__(x0, y0)
        self.radius = radius

    def draw(self):
        penup()
        goto(self.x0, self.y0)
        pendown()
        circle(self.radius)

class Square(TwoDShape):
    def __init__(self, x0, y0, length):
        super().__init__(x0, y0)
        self.length = length

    def draw(self):
        penup()
        goto(self.x0, self.y0)
        pendown()
        for _ in range(4):
            forward(self.length)
            right(90)

r1 = Rectangle(0,0,50,100)
l1 = Line(0,0,100,100)
c1 = Circle(0,0, 100)
l2 = Line(-100, -100, -100, 100)
c2 = Circle(0,0, 200)
s1 = Square(0,0, 100)
s2 = Square(100,100, 200)

mylist = [r1,l1,c1,l2,c2, s1, s2]
showturtle()
speed(3)
for eachshape in mylist:
    eachshape.draw()

done()



