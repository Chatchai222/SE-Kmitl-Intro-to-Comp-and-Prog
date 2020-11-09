from turtle import *



def drawbar(thenum,height, width=50):
    begin_fill()
    left(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    left(90)
    end_fill()

    penup()
    backward(width/2)
    right(90)
    forward(30)
    write(str(thenum))
    backward(30)
    pendown()
    left(90)
    forward(width/2)


#user_input = [1,2,2,1,3,4,1,1,1,1]

def histogram(user_input):
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

    frequency_list = [[my_set[0],my_set[1] * 30] for my_set in frequency_list]
    frequency_list.sort(key=lambda x: x[0])
    print(frequency_list)

    max_list = [my2_set[1] for my2_set in frequency_list]
    y_axis = max(max_list)

    x_axis = len(frequency_list) * 50 + 100


    showturtle()

    # Drawing axis
    forward(x_axis)
    write("X")
    backward(x_axis)
    left(90)
    forward(y_axis)
    write("Y")
    backward(y_axis)
    right(90)

    #
    forward(50)
    for theset in frequency_list:
        drawbar(theset[0], theset[1])
 
    done()

histogram([-3,1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4])



