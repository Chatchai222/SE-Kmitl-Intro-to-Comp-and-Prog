from turtle import *
from abc import abstractmethod, ABC

class Char(ABC):
    def draw(self, x, y):
        pass

    def getWidth(self):
        return 10

class Char0(Char):
    def __init__(self):
        self.digit = '0'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        pendown()
        forward(self.seg_length)
        left(90)
        forward(self.seg_length * 2)
        left(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length * 2)
        left(90)
        penup()

    def getWidth(self):
        return self.seg_length

class Char1(Char):
    def __init__(self):
        self.digit = '1'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        forward(self.seg_length)
        pendown()
        left(90)
        forward(self.seg_length * 2)
        penup()
        goto(x, y)
        right(90)

    def getWidth(self):
        return self.seg_length

class Char2(Char):
    def __init__(self):
        self.digit = '2'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        left(90)
        forward(self.seg_length * 2)
        right(90)
        pendown()
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        backward(self.seg_length)
        penup()

    def getWidth(self):
        return self.seg_length

class Char3(Char):
    def __init__(self):
        self.digit = '3'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        pendown()
        forward(self.seg_length)
        left(90)
        forward(self.seg_length * 2)
        left(90)
        forward(self.seg_length)
        penup()
        left(180)
        goto(x, y + self.seg_length)
        pendown()
        forward(self.seg_length)
        penup()
        goto(x,y)

    def getWidth(self):
        return self.seg_length


class Char4(Char):
    def __init__(self):
        self.digit = '4'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        forward(self.seg_length)
        left(90)
        pendown()
        forward(self.seg_length * 2)
        penup()
        goto(x, y + self.seg_length * 2)
        pendown()
        left(180)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        penup()
        goto(x,y)

    def getWidth(self):
        return self.seg_length

class Char5(Char):
    def __init__(self):
        self.digit = '5'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        pendown()
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        penup()
        goto(x,y)

    def getWidth(self):
        return self.seg_length

class Char6(Char):
    def __init__(self):
        self.digit = '6'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        pendown()
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        penup()
        goto(x, y)
        left(90)
        pendown()
        forward(self.seg_length)
        right(90)
        penup()
        goto(x,y)

    def getWidth(self):
        return self.seg_length

class Char7(Char):
    def __init__(self):
        self.digit = '7'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        forward(self.seg_length)
        pendown()
        left(90)
        forward(self.seg_length * 2)
        left(90)
        forward(self.seg_length)
        penup()
        goto(x, y)
        right(180)

    def getWidth(self):
        return self.seg_length

class Char8(Char):
    def __init__(self):
        self.digit = '8'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        pendown()
        forward(self.seg_length)
        left(90)
        forward(self.seg_length * 2)
        left(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length * 2)
        left(90)
        penup()
        goto(x,y + self.seg_length)
        pendown()
        forward(self.seg_length)
        penup()
        goto(x,y)

    def getWidth(self):
        return self.seg_length

class Char9(Char):
    def __init__(self):
        self.digit = '9'
        self.seg_length = 20

    def draw(self, x, y):
        penup()
        goto(x, y)
        pendown()
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        left(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        right(90)
        forward(self.seg_length)
        left(90)
        penup()
        goto(x, y)

    def getWidth(self):
        return self.seg_length

def drawNum(x):
    string_digit = str(x)
    mydict = {'0':Char0(), '1':Char1(), '2':Char2(), '3':Char3(), '4':Char4(), '5':Char5(),
              '6':Char6(), '7':Char7(), '8':Char8(), '9':Char9()}
    list_to_draw = [mydict[digit] for digit in string_digit]
    x_pos = -100
    y_pos = 0
    showturtle()
    for char in list_to_draw:
        char.draw(x_pos, y_pos)
        x_pos += char.getWidth() + 5
    done()

drawNum('0123456789')
