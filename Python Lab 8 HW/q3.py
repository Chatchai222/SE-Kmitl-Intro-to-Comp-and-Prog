import turtle as tur

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

def draw_chart(frequency_list, x_scale=50):
    bar_chart = [[letter, frequency * 20] for letter, frequency in frequency_list]
    max_height = max([height for letter, height in bar_chart])


    x_axis = (len(bar_chart) + 1) * x_scale



    y_tur = tur.Turtle()
    x_tur = tur.Turtle()

    x_tur.showturtle()
    x_tur.speed(10)
    # Drawing axis
    y_tur.left(90)
    y_tur.forward(max_height)

    x_tur.forward(x_axis)
    x_tur.backward(x_axis)

    for each_bar in bar_chart:
        # Moving onto the next bar and writing letter
        x_tur.forward(x_scale * 0.6)
        x_tur.penup()
        x_tur.right(90)
        x_tur.forward(20)
        x_tur.write(each_bar[0], font=("Arial", 15, "normal"))
        x_tur.backward(20)
        x_tur.left(90)
        x_tur.pendown()

        # Bar Chart
        x_tur.left(90)
        x_tur.forward(each_bar[1])
        x_tur.right(90)
        x_tur.forward(x_scale * 0.4)
        x_tur.right(90)
        x_tur.forward(each_bar[1])
        x_tur.left(90)

    # For the arrow at the end of x-axis
    x_tur.forward(x_scale)

    tur.done()

user_input = input("Enter some text: ")
draw_chart(get_frequency(user_input))