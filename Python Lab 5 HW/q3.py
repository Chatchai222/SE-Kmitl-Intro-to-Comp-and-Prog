# Question 3
user_input = int(input("Please enter an integer: "))

for each_mountain in reversed(range(user_input)):  # For creating each mountain
    height = each_mountain + 1  # Compensate for counting from zero

    # Generate going up part of the mountain
    for each_line_rise in range(height):  # For eachline of rising
        rise_mountain = ""
        for each_asterisk in range(each_line_rise + 1):  # For creating * in eachline rise
            rise_mountain = rise_mountain + "*"
        print(rise_mountain)

    # Generate going down part of the mountain
    for each_line_drop in reversed(range(height - 1)):  # For eachline of going drop
        down_mountain = ""
        for each_asterisk in range(each_line_drop + 1):  # For creating * in eachline drop
            down_mountain = down_mountain + "*"
        print(down_mountain)