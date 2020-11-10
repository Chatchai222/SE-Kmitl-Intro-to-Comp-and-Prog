def my_count(thelist):
    counter = 0
    for x in thelist:
        if (x >= 0):
            counter += 1

    return counter

print(my_count([-3,2,0,1,-5]))
