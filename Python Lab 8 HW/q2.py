# Q2
def get_frequency(string):
    frequency_list = []
    for letter in string:
        letter_is_unique = True
        for each_set in frequency_list:
            if each_set[0] == letter:
                each_set[1] += 1
                letter_is_unique = False
                break

        if letter_is_unique:
            frequency_list.append([letter, 1])

    return frequency_list


user_input = input("Please input a string: ")
frequency_list = get_frequency(user_input)
string_length = len(user_input)

print("-- Character Frequency table -")
print("char percentage (character count / string length)")
for letter, frequency in frequency_list:
    print(str(letter) + "{:9.2f}".format(frequency * 100 / string_length) + "%")







