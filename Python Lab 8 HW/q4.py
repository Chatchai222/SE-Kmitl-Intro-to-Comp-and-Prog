# Q4
def get_ISBN(user_num):
    sum = 0
    output = user_num
    for i, num in enumerate(user_num):
        sum += int(num) * (i + 1)

    checksum = sum % 11
    if checksum == 10:
        return output + 'X'
    else:
        return output + str(checksum)

user_input = input("Enter the first 9 digits of an ISBN-10 as a string: ")
print(f"Your ISBN-10 number is {get_ISBN(user_input)}")
user_input = input("Enter the first 9 digits of an ISBN-10 as a string: ")
print(f"Your ISBN-10 number is {get_ISBN(user_input)}")