# Q1
def bin_to_int(binary):
    output = 0
    for i, each_digit in enumerate(reversed(binary)):
        output += 2 ** int(i) * int(each_digit)

    return output

def int_to_bin(num):
    altered_num = num
    output = ""
    while altered_num > 0:
        if altered_num % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output

        altered_num = altered_num // 2

    return output

for _ in range(3):
    user_input = int(input("Please enter an integer: "))
    if user_input == 0:
        print("Integer is zero")
    elif user_input < 0:
        print("Integer is negative")
    else:
        print(f"Binary of user_input is {int_to_bin(user_input)}")
        user_input = int_to_bin(user_input)
        print(f"Int of user is {bin_to_int(user_input)}")

