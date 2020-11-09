# Question 3
import math
from turtle import *
import pygame

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = 2 * (width + height)

    def getArea(self):
        self.area = self.width * self.height
        return self.area
        # print("Area of rect is " + str(self.area))

    def getPerimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
        # print("Perimeter of rect is " + str(self.perimeter))

    def move(self, newX, newY):
        # print("Changed coordinates of x and y")
        self.x = newX
        self.y = newY

    def intersect(self, rec):
        rec_intersect = False

        cur_top_left = [self.x, self.y]
        cur_top_right = [self.x + self.width, self.y]
        cur_bottom_left = [self.x, self.y - self.height]
        cur_bottom_right = [self.x + self.width, self.y - self.height]

        rec_top_left = [rec.x, rec.y]
        rec_top_right = [rec.x + rec.width, rec.y]
        rec_bottom_left = [rec.x, rec.y - rec.height]
        rec_bottom_right = [rec.x + rec.width, rec.y - rec.height]

        # For checking if any of the point
        if rec.x < cur_top_left[0] < (rec.x + rec.width) and (rec.y - rec.height) < cur_top_left[1] < rec.y:
            rec_intersect = True
        if rec.x < cur_top_right[0] < (rec.x + rec.width) and (rec.y - rec.height) < cur_top_right[1] < rec.y:
            rec_intersect = True
        if rec.x < cur_bottom_left[0] < (rec.x + rec.width) and (rec.y - rec.height) < cur_bottom_left[1] < rec.y:
            rec_intersect = True
        if rec.x < cur_bottom_right[0] < (rec.x + rec.width) and (rec.y - rec.height) < cur_bottom_right[1] < rec.y:
            rec_intersect = True

        if self.x < rec_top_left[0] < (self.x + self.width) and (self.y - self.height) < rec_top_left[1] < self.y:
            rec_intersect = True
        if self.x < rec_top_right[0] < (self.x + self.width) and (self.y - self.height) < rec_top_right[1] < self.y:
            rec_intersect = True
        if self.x < rec_bottom_left[0] < (self.x + self.width) and (self.y - self.height) < rec_bottom_left[1] < self.y:
            rec_intersect = True
        if self.x < rec_bottom_right[0] < (self.x + self.width) and (self.y - self.height) < rec_bottom_right[1] < self.y:
            rec_intersect = True

        new_rec = Rectangle(rec.b)


    def draw(self):
        showturtle()
        penup()
        goto(self.x, self.y)
        pendown()

        forward(self.width)
        right(90)
        forward(self.height)
        right(90)
        forward(self.width)
        right(90)
        forward(self.height)
        right(90)



class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def getArea(self):
        area = math.pi * (self.radius ** 2)
        return area

    def getPerimeter(self):
        perimeter = math.pi * (self.radius * 2)
        return perimeter

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def draw(self):
        showturtle()
        penup()
        goto(self.x, self.y - self.radius)
        pendown()
        circle(self.radius)

showturtle()
circle(100)









