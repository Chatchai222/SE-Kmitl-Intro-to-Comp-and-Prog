import math
from turtle import *

class Rectangle2D(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        penup()
        goto(self.x, self.y)
        pendown()
        for _ in range(2):
            forward(self.width)
            left(90)
            forward(self.height)
            left(90)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__radius = 5

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def draw(self):
        penup()
        goto(self.x, self.y - self.__radius)
        pendown()
        begin_fill()
        circle(self.__radius)
        end_fill()

def getRectangle():
    mylist = [float(x) for x in input("Please enter the point: ").split()]
    mylist = [Point(x,y) for x, y in zip(mylist[::2], mylist[1::2])]

    highest_point = max(mylist, key=lambda r: r.y)
    lowest_point = min(mylist, key=lambda r: r.y)
    leftest_point = min(mylist, key=lambda r: r.x)
    rightest_point = max(mylist, key=lambda r: r.x)

    myrect = Rectangle2D(leftest_point.x,lowest_point.y, (rightest_point.x - leftest_point.x), (highest_point.y - lowest_point.y))
    print(f"The bounding rectangle is centered at ({myrect.x + myrect.width/2},{myrect.y + myrect.height/2}) with width {myrect.width} and height {myrect.height}")
    screensize(2000, 2000)
    showturtle()
    myrect.draw()
    for eachpoint in mylist:
        eachpoint.draw()
    done()

# I scale up the point so it don't look too small
getRectangle()