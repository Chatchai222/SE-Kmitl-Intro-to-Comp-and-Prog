from turtle import *
import math


user_input = 480
s = user_input
flag_width = s  # 60
flag_height = s / 2  # 30
cross_width = s / 10  # 6
white_border = s / 30  # 2
edge_to_triangle_top = s / (60 /7)  # 7
edge_to_triangle_bottom = s / 12  # 5

flag_mini_width = s / 2.4  # 25
flag_mini_height = s / 6  # 10
tri_big_base = s / (10 / 3)  # 18
tri_big_height = tri_big_base / 2  # 9
tri_small_base = s / (30 / 7)  # 14
tri_small_height = tri_small_base / 2  # 7
parallel_base = s / 15  # 4

# Color
RED = "#FF0000"
BLUE = "#0900FF"

showturtle()
screensize(2000, 2000)
def rectangle(width=480, height=480, rect_color="Green"):
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

def trapezoid():
    pass


def mini_flag():  # This is the miniflag for top left
    # Draws the big triangle
    forward(edge_to_triangle_top)
    triangle(tri_big_base, tri_big_height, "Blue")
    back(edge_to_triangle_top)

    # Draw the left triangle
    penup()
    forward(flag_mini_width - edge_to_triangle_bottom)
    right(90)
    forward(flag_mini_height)
    right(90)


    triangle((tri_small_base + white_border + parallel_base), flag_mini_height, RED)
    forward(parallel_base)
    triangle((tri_small_base + white_border),(flag_mini_height))





