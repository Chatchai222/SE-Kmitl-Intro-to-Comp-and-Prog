# Question 4

sum = 0
prev = 0

old_input = 1

for x in range(5):
    new_input = int(input("Enter an integer: "))
    if (new_input > 0) != (old_input > 0):
        sum = 0
        sum += new_input
    else:
        sum += new_input

    old_input = new_input
    print("Current sum: " + str(sum))