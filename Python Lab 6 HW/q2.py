# Question 2
import math
from turtle import *

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
