# Question 3
import math
from turtle import *

def uk_flags(user_input):
    s = user_input
    sixty = s  # 60
    thirty = s / 2  # 30
    six = s / 10  # 6
    two = s / 30  # 2
    seven = s / (60 / 7)  # 7
    five = s / 12  # 5
    one = s / 60
    three = s / 20
    eight = s / 7.5

    twenty_five = s / 2.4  # 25
    twenty = s / 3  # 20
    ten = s / 6  # 10
    eighteen = s / (10 / 3)  # 18
    nine = eighteen / 2  # 9
    fourteen = s / (30 / 7)  # 14
    four = s / 15  # 4

    # Color
    RED = "#CC0000"
    BLUE = "#000066"

    showturtle()
    screensize(2000, 2000)
    def rectangle_fill(width=480, height=480, rect_color="Green"):
        begin_fill()
        color(rect_color)
        forward(width)
        right(90)
        forward(height)
        right(90)
        forward(width)
        right(90)
        forward(height)
        right(90)
        end_fill()

    # The mini flag design base prototype is based on top left
    def triangle(base, height, tri_color="Black"):
        color(tri_color)
        begin_fill()
        initial_pos = pos()
        forward(base)
        right(90)
        forward(height)
        goto(initial_pos)
        left(90)
        end_fill()

    # This is based on the bottom left parallelogram
    def parallelogram(base, long_side, height, par_color, reversed=1):
        long_side *= reversed
        height *= reversed
        color(par_color)
        begin_fill()
        forward(base)
        tip_x = xcor()
        tip_y = ycor()
        goto(tip_x + long_side, tip_y + height)
        back(base)
        trough_x = xcor()
        trough_y = ycor()
        goto(trough_x - long_side, trough_y - height)
        end_fill()




    def mini_flag_top_left():  # This is the miniflag for top left
        # Draws the big triangle
        penup()
        forward(seven)
        pendown()
        triangle(eighteen, nine, BLUE)
        penup()
        back(seven)
        pendown()


        # Draw the left triangle
        penup()
        forward(twenty_five - five)
        right(90)
        forward(ten)
        right(90)

        triangle((fourteen + two + four), ten, RED)
        forward(four)
        triangle((fourteen + two),eight,"White")
        forward(two)
        triangle(fourteen, seven, BLUE)

        forward(fourteen)
        right(90)
        forward(ten)
        right(90)

    def mini_flag_bottom_left(reversed=1):
        # Draw parallelogram
        parallelogram(four, twenty, ten, RED, reversed)

        # Transition to big triangle
        penup()
        forward(seven)

        # Big triangle
        triangle(eighteen, -nine, BLUE)

        # Transition to small triangle
        penup()
        back(seven)
        forward(fourteen)
        left(90)
        forward(ten)
        left(90)
        pendown()

        # Small triangle
        triangle(fourteen,  -seven, BLUE)

        # Transition to edge
        penup()
        forward(fourteen)
        left(90)
        forward(ten)
        left(90)

    def cross():
        # Drawing of cross
        rectangle_fill(six, thirty, RED)
        penup()
        back(twenty_five + two)
        right(90)
        forward(ten + two)
        left(90)
        pendown()
        rectangle_fill(sixty, six, RED)

        # Go back to top left
        penup()
        left(90)
        forward(ten + two)
        right(90)
        pendown()




    cross()
    mini_flag_top_left()

    # Transition to bottom right mini flag
    penup()
    forward(sixty)
    right(90)
    forward(thirty)
    right(90)
    pendown()

    # Drawing bottom_right mini flag
    mini_flag_top_left()

    # Transition to bottom left
    penup()
    forward(sixty)
    right(180)

    # Drawing bottom left mini flag
    mini_flag_bottom_left()

    # Transition to top right mini flag
    penup()
    forward(sixty)
    left(90)
    forward(thirty)
    left(90)

    # Drawing top right mini flag
    mini_flag_bottom_left(-1)




uk_flags(1000)
done()