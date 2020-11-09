### This is Homework #2 14th Aug 2020 Intro to Computers and Programming
import random

### Questions 1 ###
a = float(input("First no."))
b = float(input("Second no."))
c = float(input("Third no."))
d = float(input("Fourth no."))
e = float(input("Fifth no."))

summation = a + b + c + d + e
average = summation / 5
print("Summation is " + str(summation))
print("Average is " + str(average))

### Question 2 ###

from turtle import *
initial_x = -100
initial_y = -200
showturtle()
getscreen().bgcolor('#ADFAFD')
screensize(canvwidth=1000, canvheight=1300)
speed(2)
up()
setx(initial_x)
sety(initial_y)
down()


# Drawing the main house
color('Black', 'Red')
begin_fill()
for x in range(4):
    down()
    forward(150)
    left(90)
end_fill()

# For drawing the roof
up()
left(90)
forward(150)
right(90)

down()
color('Black', 'Yellow')
begin_fill()
for y in range(3):
    forward(150)
    left(120)
end_fill()

# For drawing door
up()
forward(50)
right(90)
forward(150)
left(90)

down()
color('Black', '#D0943A')
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

# For drawing clouds
left(180)
up()
forward(400)
left(90)
forward(300)
down()
left(180)
color('White', 'White')

def cloud():
    down()
    begin_fill()
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    up()
    end_fill()

# Connect cloud
cloud()
up()
forward(70)
right(90)
forward(30)
left(90)
cloud()

# Middle cloud
up()
forward(250)
left(90)
forward(30)
right(90)
cloud()


# Sun cloud
forward(70)
left(90)
forward(40)
right(90)
cloud()


# Drawing the sun
up()
left(90)
forward(100)

down()
begin_fill()
color('Red', 'Orange')
circle(60)
end_fill()

up()
goto(initial_x, initial_y)
done()

























