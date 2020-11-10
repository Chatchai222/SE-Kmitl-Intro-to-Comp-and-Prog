from turtle import *

user_input = float(input("Please enter the flag size: "))

my_unit = user_input / 9

showturtle()
color("Black")
forward(my_unit * 9)
right(90)
forward(my_unit * 6)
right(90)
forward(my_unit * 9)
right(90)
forward(my_unit * 6)
right(90)

color("Red")
begin_fill()
forward(my_unit * 9)
right(90)
forward(my_unit * 1)
right(90)
forward(my_unit * 9)
right(90)
forward(my_unit * 1)
right(90)
end_fill()

penup()
right(90)
forward(my_unit * 2)
left(90)
pendown()

color("Blue")
begin_fill()
forward(my_unit * 9)
right(90)
forward(my_unit * 2)
right(90)
forward(my_unit * 9)
right(90)
forward(my_unit * 2)
right(90)
end_fill()

penup()
right(90)
forward(my_unit * 3)
left(90)
pendown()

color("Red")
begin_fill()
forward(my_unit * 9)
right(90)
forward(my_unit * 1)
right(90)
forward(my_unit * 9)
right(90)
forward(my_unit * 1)
right(90)
end_fill()

done()


















