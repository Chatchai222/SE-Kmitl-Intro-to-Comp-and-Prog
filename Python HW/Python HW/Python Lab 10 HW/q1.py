from turtle import *
def get_freq_list(user_input):
    frequency_list = []
    for each_num in user_input:

        new_num = True
        for each_set in frequency_list:
            if (each_set[0] == each_num):
                each_set[1] += 1
                new_num = False
                break

        if new_num:
            frequency_list.append([each_num, 1])

    frequency_list.sort(key=lambda x: x[0])
    return frequency_list

def draw_pie_slice(radius, angle, color):
    pencolor('Black')
    fillcolor(color)
    begin_fill()
    forward(radius)
    left(90)
    circle(radius, angle)
    left(90)
    forward(radius)
    left(180)
    end_fill()
    pass

def pie_chart(user_list):
    RADIUS = 200
    COLOR_LIST = ['Red', 'Blue', 'Green', 'Yellow']
    freq_list = get_freq_list(user_list)
    total_freq = len(user_list)

    draw_list = [(each_set[1] / total_freq) * 360 for each_set in freq_list]
    showturtle()
    left(90)
    for i, each_angle in enumerate(draw_list):
        draw_pie_slice(RADIUS, each_angle, COLOR_LIST[i % len(COLOR_LIST)])
    done()

list1 = [3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3]
pie_chart(list1)
