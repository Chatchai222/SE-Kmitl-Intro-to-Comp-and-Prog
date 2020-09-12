# Question 1

def time24hourTo12hour(user_input):
    str_hour = user_input[:2:]
    int_hour = int(str_hour)

    colon_minute = user_input[2::]

    if int_hour > 13:
        int_hour -= 12
        newtime = str(int_hour) + str(colon_minute) + " PM"
    else:
        newtime = str(int_hour) + str(colon_minute) + " AM"

    return newtime

print(time24hourTo12hour("11:24"))
print(time24hourTo12hour("23:56"))