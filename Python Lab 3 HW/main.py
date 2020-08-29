# This is the Intro to programming and computers homework 3
# Assigned on the 27 Aug 2020
# To be submitted on the on the Friday 4 September 2020
from turtle import *
import math

### Question 1 ###
"""
name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
federal_tax_rate = float(input("Enter federal tax withholding rate: "))
state_tax_rate = float(input("Enter state tax withholding rate: "))

gross_pay = hours_worked * hourly_pay_rate
federal_withholding = gross_pay * federal_tax_rate
state_withholding = gross_pay * state_tax_rate
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction



print("Employee Name: " + name)
print("Hours Worked: " + str(hours_worked))
print("Pay Rate: $" + str(hourly_pay_rate))
print("Gross Pay: $" + str(gross_pay))
print("Deductions:")
print("  Federal Withholding (20.0%): $" + str(federal_withholding))
print("  State Withholding (9.0%): $" + '{:.5f}'.format(state_withholding)[:-3])
print("  Total Deduction: $" + '{:.2f}'.format(total_deduction))
print("Net pay: $" + '{:.2f}'.format(net_pay))

"""


### Question 2 ###
"""
mystring = input("Input number: ")
newstring = ""
for eachchar in reversed(mystring):
    newstring = newstring + str(eachchar)

print(newstring)

"""

### Question 3 ###
"""

length_star = int(input("Please enter the length: "))

showturtle()
speed(5)
right(36)


for x in range(5):
    forward(length_star)
    left(144)
done()

"""


### Question 4 ###
"""

user_radius = int(input("Please enter the radius: "))

showturtle()

pensize(2)
pencolor("Blue")
circle(user_radius)
right(45)
penup()
forward(user_radius * 1.5)
pendown()
left(45)
pencolor("Black")
circle(user_radius)
left(45)
penup()
forward(user_radius * 1.5)
pendown()
right(45)
pencolor("Red")
circle(user_radius)
right(45)
penup()
forward(user_radius * 1.5)
pendown()
left(45)
pencolor("Yellow")
circle(user_radius)
left(45)
penup()
forward(user_radius * 1.5)
pendown()
right(45)
pencolor("Green")
circle(user_radius)
done()

"""


### Question 5 ###
"""

x1 = float(input("Please enter x1"))
y1 = float(input("Please enter y1"))
x2 = float(input("Please enter x2"))
y2 = float(input("Please enter y2"))
x3 = float(input("Please enter x3"))
y3 = float(input("Please enter y3"))

# Finding length of triangle
a1to2 = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
b2to3 = math.sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2))
c3to1 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

# Using Heron's formula
s = (a1to2 + b2to3 + c3to1) / 2
area = math.sqrt(s * (s - a1to2) * (s - b2to3) * (s - c3to1))

# Search for lowest point
min_x = min(x1, x2, x3)
min_y = min(y1, y2, y3)

showturtle()
penup()
goto(x1, y1)
pendown()
goto(x2, y2)
goto(x3, y3)
goto(x1, y1)
penup()

goto(min_x - 10, min_y - 10)
write('{:.2}'.format(area))
done()
"""




























