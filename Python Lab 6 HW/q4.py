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
