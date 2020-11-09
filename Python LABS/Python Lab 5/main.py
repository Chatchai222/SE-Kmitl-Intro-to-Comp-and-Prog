# This is Intro to comp and prog lab 6
# Done on 11 Sep 2020

from turtle import *

# Question 1
# def get_grade():
#     score_input = float(input("Please enter a number: "))
#     if 80 <= score_input <= 100:
#         return "A"
#     elif 70 <= score_input < 80:
#         return "B"
#     elif 60 <= score_input < 70:
#         return "C"
#     elif 50 <= score_input <60:
#         return "D"
#     elif score_input < 50:
#         return "F"
#
# print(get_grade())

# Question 2
# def is_prime_number(user_input):
#     if user_input <= 1:
#         return False
#     else:
#         num_is_prime = True
#         for x in range(2, user_input):
#             if user_input % x == 0:
#                 num_is_prime = False
#                 break
#
#         if num_is_prime:
#             return True
#         else:
#             return False
# print(is_prime_number(111))


# Question 3
# showturtle()
# user_x = int(input("Please input x: "))
#
#
# def square(length):
#     for x in range(4):
#         forward(length)
#         right(90)
#
# def second_function(x):
#     length = x * 8
#     square(length)
#     # For drawing the 2 lines cutting across the square
#     # Vertical line
#     forward(length / 2)
#     right(90)
#     forward(length)
#     right(90)
#
#     # Horizontal line
#     forward(length / 2)
#     right(90)
#     forward(length / 2)
#     right(90)
#     forward(length)
#     left(90)
#
#     # Going back to top left
#     forward(length/2)
#     left(90)
#     forward(length)
#     left(180)
#
#
#
#
#
#     for y in range(3):
#         penup()
#         forward(x)
#         right(90)
#         forward(x)
#         left(90)
#         pendown()
#
#         length -= 2 * x
#         square(length)
#
#
#
# second_function(user_x)
# done()

# Question 4
# showturtle()
#
# def draw_polygon(x=0, y=0, side=4, size=100):
#     total_internal_angle = (side - 2) * 180
#     each_internal_angle = total_internal_angle / side
#     supplement_angle = 180 - each_internal_angle
#
#     # Sending turtle to initial coord
#     penup()
#     goto(x,y)
#     pendown()
#
#     # Drawing the actual polygon
#     for i in range(side):
#         forward(size)
#         left(supplement_angle)
#
#
#
# draw_polygon(50, 50, 6)
# draw_polygon(0,0)
# draw_polygon(10,10, size=300)

# Question 5
def sum_of_digits(input_num):
    the_sum = 0
    string_num = str(input_num)
    for each_num in string_num:
        the_sum += int(each_num)

    return the_sum

print(sum_of_digits(11119))






