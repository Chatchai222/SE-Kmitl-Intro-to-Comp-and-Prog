# This is Intro to Comp and Prog Homework #6
# Issued on 11 Sep 2020
from turtle import *
import math

# Question 1

def time24hourTo12hour(user_input):
    str_hour = user_input[:2:]
    int_hour = int(str_hour)

    colon_minute = user_input[2::]

    if int_hour > 13:
        int_hour -= 12
        newtime = str(int_hour) + str(colon_minute) + " PM"
    else:
        newtime = str(int_hour) + str(colon_minute) + " AM"

    return newtime

print(time24hourTo12hour("11:24"))

# Question 2
showturtle()
screensize(3000,3000)
speed(0)

def rectangle(width=60, height=30, text="Hello", text_align=0.1):
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width * (1 - text_align))
    write(text)
    forward(width * text_align)
    right(90)
    forward(height)
    right(90)
    forward(width)

def row_day_name(rect_width=60, rect_height=30, day_name_start="Mo"):
    weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    day_name_start = weekdays.index(day_name_start)

    for each_weekday in weekdays[day_name_start::]:
        rectangle(rect_width, rect_height, each_weekday)
    for each_weekday in weekdays[:day_name_start:]:
        rectangle(rect_width, rect_height, each_weekday)

    # Move turtle to bottom left
    back(rect_width * 7)
    right(90)
    forward(rect_height)
    left(90)


def table(start_date, num_of_day, row_amount=5, column_amount=7, rect_width=60, rect_height=30):
    rect_id = 0
    for x in range(row_amount):
        for each_block in range(column_amount):
            rect_id += 1
            if rect_id > start_date and rect_id - start_date <= num_of_day:
                rectangle(rect_width, rect_height, str(rect_id - start_date))
            else:
                rectangle(rect_width, rect_height, "")
        back(column_amount * rect_width)
        right(90)
        forward(rect_height)
        left(90)


def month_calendar(start_date=1, num_of_day=30, month_name="Monthly", day_name_start="Mo", row_amount=6, column_amount=7, rect_width=40, rect_height=20):
    # Draws the month header
    rectangle(rect_width * column_amount, rect_height, month_name, 0.3)
    back(rect_width * column_amount)
    right(90)
    forward(rect_height)
    left(90)

    # Draws the weekday header
    row_day_name(rect_width, rect_height, day_name_start)

    # Draws the date table
    table(start_date, num_of_day, row_amount, column_amount, rect_width, rect_height)

def calendar_of_2020(user_input):
    user_input -= 1
    month_list = [
        [2, 31, "January 2020"],
        [5, 29, "February 2020"],
        [6, 31, "March 2020"],
        [2, 30, "April 2020"],
        [4, 31, "May 2020"],
        [0, 30, "June 2020"],
        [2, 31, "July 2020"],
        [5, 31, "August 2020"],
        [1, 30, "September 2020"],
        [3, 31, "October 2020"],
        [6, 30, "November 2020"],
        [1, 31, "December 2020"]
    ]

    new_start_date = month_list[user_input][0]
    new_num_of_day = month_list[user_input][1]
    new_month_name = month_list[user_input][2]


    month_calendar(new_start_date, new_num_of_day, new_month_name)

calendar_of_2020(6)
done()

# Question 3
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




uk_flags(500)
done()

# Question 4
def num_to_english(user_input):
    zero_to_nineteen = {
        0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen"
    }
    twenty_to_ninety = {
        20:"twenty",
        30:"thirty",
        40:"fourty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety"
    }
    needed_and = False
    eng_output = ""

    if user_input < 0 or user_input > 999:
        eng_output = "I don't know."
    else:
        if user_input >= 100:
            eng_output += zero_to_nineteen.get(user_input // 100) + " hundred "
            needed_and = True
            user_input %= 100
        if user_input >= 20:
            if needed_and:
                eng_output += "and "
            eng_output += twenty_to_ninety.get((user_input // 10) * 10)
            user_input %= 10
            if user_input != 0:
                eng_output += "-" + zero_to_nineteen.get(user_input)
        else:
            if needed_and and user_input != 0:
                eng_output += "and "
            if user_input != 0:
                eng_output += zero_to_nineteen.get(user_input)

    return eng_output

print(num_to_english(17))
print(num_to_english(20))
print(num_to_english(56))
print(num_to_english(100))
print(num_to_english(201))
print(num_to_english(-100))
print(num_to_english(5000))

# Question 5
user_input = int(input("Input your amount of money: "))
bank_notes_list = [[1000, 0],
                   [500, 0],
                   [100, 0],
                   [50, 0],
                   [20, 0],
                   [10, 0],
                   [5, 0],
                   [2, 0],
                   [1, 0]]
# This part is for the calculation of amount of banknotes for each bank notes
for each_bank_note in bank_notes_list:
    amount_of_notes = user_input // each_bank_note[0]  # // gives only quotient (int division)
    each_bank_note[1] = amount_of_notes
    user_input = user_input % each_bank_note[0]

# Printing out the amount
for each_bank_note in bank_notes_list:
    if each_bank_note[1] == 0:
        continue
    elif each_bank_note[0] > 10:
        text = str(each_bank_note[0]) + "-Baht notes: " + str(each_bank_note[1])
    else:
        text = str(each_bank_note[0]) + "-Baht coins: " + str(each_bank_note[1])

    print(text)

# Question 6
def my_reverse(user_input):
    str_digits = str(user_input)
    reversed_str_digits = ""
    for each_digit in reversed(str_digits):
        reversed_str_digits += each_digit

    reversed_digits = int(reversed_str_digits)
    return reversed_digits

print(my_reverse(12345))
