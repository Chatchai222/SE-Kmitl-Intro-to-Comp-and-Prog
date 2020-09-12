from turtle import *

# This is intro to computers and programming homework #5
# Issued on 10th Sep 2020

# Question 1 (The newtons method for square root)
user_number = float(input("Please enter a number to find sqrt of: "))
guess = user_number / 2

# guess = initial_guess
for x in range(10):
    temp = user_number / guess
    guess = (guess + temp) / 2

print(guess)

# Question 2

showturtle()
screensize(3000,3000)
speed(0)

def rectangle(width=60, height=30, text="Hello"):
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width * 0.9)
    write(text)
    forward(width * 0.1)
    right(90)
    forward(height)
    right(90)
    forward(width)

def row_day_name(rect_width=60, rect_height=30):
    weekdays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    for each_weekday in weekdays:
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


def month_calendar(start_date, num_of_day, month_name="Monthly",row_amount=6, column_amount=7, rect_width=40, rect_height=20):
    # Draws the month header
    rectangle(rect_width * 7, rect_height, month_name)
    back(rect_width * 7)
    right(90)
    forward(rect_height)
    left(90)

    # Draws the weekday header
    row_day_name(rect_width, rect_height)

    # Draws the date table
    table(start_date, num_of_day, row_amount, column_amount, rect_width, rect_height)


# This is literally for that purpose to fit the screen
def re_adjust():
    penup()
    forward(280)
    left(90)
    forward(640)
    right(90)
    pendown()



jan = month_calendar(3, 31, "Month#1")
feb = month_calendar(6, 29, "Month#2")
mar = month_calendar(0, 31, "Month#3")
apr = month_calendar(3, 30, "Month#4")
re_adjust()
may = month_calendar(5, 31, "Month#5")
jun = month_calendar(1, 30, "Month#6")
jul = month_calendar(3, 31, "Month#7")
aug = month_calendar(6, 31, "Month#8")
re_adjust()
sep = month_calendar(2, 30, "Month#9")
oct = month_calendar(4, 31, "Month#10")
nov = month_calendar(0, 30, "Month#11")
dec = month_calendar(2, 31, "Month#12")

done()

# Question 3
user_input = int(input("Please enter an integer: "))

for each_mountain in reversed(range(user_input)):  # For creating each mountain
    height = each_mountain + 1  # Compensate for counting from zero

    # Generate going up part of the mountain
    for each_line_rise in range(height):  # For eachline of rising
        rise_mountain = ""
        for each_asterisk in range(each_line_rise + 1):  # For creating * in eachline rise
            rise_mountain = rise_mountain + "*"
        print(rise_mountain)

    # Generate going down part of the mountain
    for each_line_drop in reversed(range(height - 1)):  # For eachline of going drop
        down_mountain = ""
        for each_asterisk in range(each_line_drop + 1):  # For creating * in eachline drop
            down_mountain = down_mountain + "*"
        print(down_mountain)
