def name_list():
    output_list = []
    for x in range(1000):
        user_input = input(f"Enter name {x+1}: ")
        if (user_input == ""):
            break
        output_list.append(user_input)

    return output_list

print(name_list())


