# Question 2
user_input = input("Please enter a number: ")
isfloat = False

for each_char in user_input:
    if each_char == '.':
        isfloat = True

user_input = float(user_input)

if isfloat:
    second_input = input("Display in Floating point(type f) or scientific format(type e): ")
    if second_input == 'f':
        print(user_input)
    if second_input == 'e':
        print("{:e}".format(user_input))
else:
    user_input = int(user_input)
    second_input = input("Display in Binary(type b), Octal(type o), Hexadecimal(h), Decimal(d): ")
    if second_input == 'b':
        print("{:b}".format(user_input))
    if second_input == 'o':
        print("{:o}".format(user_input))
    if second_input == 'h':
        print("{:x}".format(user_input))
    if second_input == 'd':
        print("{:d}".format(user_input))






