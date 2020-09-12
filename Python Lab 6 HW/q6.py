# Question 6
def my_reverse(user_input):
    str_digits = str(user_input)
    reversed_str_digits = ""
    for each_digit in reversed(str_digits):
        reversed_str_digits += each_digit

    reversed_digits = int(reversed_str_digits)
    return reversed_digits

print(my_reverse(12345))