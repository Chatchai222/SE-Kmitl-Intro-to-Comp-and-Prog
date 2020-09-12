# Question 1 (The newtons method for square root)
user_number = float(input("Please enter a number to find sqrt of: "))
guess = user_number / 2


for y in range(5,8):
    for x in range(y):
        temp = user_number / guess
        guess = (guess + temp) / 2
    print("{:.3f}".format(guess))

