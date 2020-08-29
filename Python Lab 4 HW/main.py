# This is the homework for Intro to computers and programming
# This homework is assigned on 28 Aug 2020
# This is homework #4
# Code in github: https://github.com/Chatchai222/SE-Kmitl-Intro-to-Comp-and-Prog
# The code is inside the branch

### Question 1 ###
"""

x0 = float(input("Please enter x0: "))
y0 = float(input("Please enter y0: "))
x1 = float(input("Please enter x1: "))
y1 = float(input("Please enter y1: "))
x2 = float(input("Please enter x2: "))
y2 = float(input("Please enter y2: "))

left_bound = min(x1, x2)
right_bound = max(x1, x2)

# Check for edge case
p0_same_as_p1 = (x0 == x1) and (y0 == y1)
vertical_line = x0 == x1
p0_same_as_p2 = (x0 == x2) and (y0 == y2)
p1_same_as_p2 = (x1 == x2) and (y1 == y2)


if p0_same_as_p1:
    print("P0 and P1 is the same, no line is created")
    if x2 < left_bound:
        print("P2 is on the left")
    elif x2 > right_bound:
        print("P2 is on the left")
    elif y2 > y0 or y2 < y0:
        print("P2 is directly above or below P0 and P1")
    else:
        print("All 3 points are the same")
elif vertical_line:
    print("PO and P1 forms a vertical line")
    if x2 < x1:
        print("P2 is on the left")
    elif x2 > x1:
        print("P2 is on the right")
    else:
        y_list = [y0, y1, y2]
        y_list.sort()
        if y_list[1] == y2:
            print("P2 is on the line")
        else:
            print("P2 is NOT on the line")
else:
    if x2 < left_bound:
        print("P2 is on the left")
    elif x2 > right_bound:
        print("P2 is on the left")
    elif p0_same_as_p2 or p0_same_as_p1:
        print("P2 is on the line from P0 to P1")
    else:
        try:
            line_gradient = (y1 - y0) / (x1 - x0)
            P0toP2_gradient = (y2 - y0) / (x2 - x0)
            if line_gradient == P0toP2_gradient:
                print("P2 is on the line from P0 to P1")
            else:
                print("P2 is NOT on the line from P0 to P1")
        except ZeroDivisionError:
            print("P2 is NOT on the line from P0 to P1")
"""

### Question 2 ###
x1 = float(input("Please enter x1: "))
y1 = float(input("Please enter y1: "))
w1 = float(input("Please enter w1: "))
h1 = float(input("Please enter h1: "))

x2 = float(input("Please enter x2: "))
y2 = float(input("Please enter y2: "))
w2 = float(input("Please enter w2: "))
h2 = float(input("Please enter h2: "))

# Defining the line
r1_top = y1 + (h1 / 2)
r1_bottom = y1 - (h1 / 2)
r1_left = x1 - (w1 / 2)
r1_right = x1 + (w1 / 2)

r2_top = y2 + (h2 / 2)
r2_bottom = y2 - (h2 / 2)
r2_left = x2 - (w2 / 2)
r2_right = x2 + (w2 / 2)

# Check for points if inside the rect
r1_top_left_in_r2 = (r2_bottom <= r1_top <= r2_top) and (r2_left <= r1_left <= r2_right)
r1_bottom_right_in_r2 = (r2_bottom <= r1_bottom <= r2_top) and (r2_left <= r1_right <= r2_right)
r1_bottom_left_in_r2 = (r2_bottom <= r1_bottom <= r2_top) and (r2_left <= r1_left <= r2_right)
r1_top_right_in_r2 = (r2_bottom <= r1_top <= r2_top) and (r2_left <= r1_right <= r2_right)

r2_bottom_left_in_r1 = (r1_left <= r2_left <= r1_right) and (r1_bottom <= r2_bottom <= r1_top)
r2_top_right_in_r1 = (r1_left <= r2_right <= r1_right) and (r1_bottom <= r2_top <= r1_top)


if r2_bottom_left_in_r1 and r2_top_right_in_r1:  # Since if bottom left point and top right, the whole rect is inside
    print("Rect 2 is inside Rect 1")
elif r1_bottom_left_in_r2 and r1_top_right_in_r2:
    print("Rect 1 is inside Rect 2")
elif r1_top_left_in_r2 or r1_bottom_left_in_r2 or r1_top_right_in_r2 or r1_bottom_right_in_r2:
    print("The rectangle overlaps")






